import os
import numpy as np
import torch
import time
import random
import json
from tqdm import tqdm
from torch.utils.data import Dataset
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
DATA_PATH = os.path.join(ROOT_DIR, 'datasets')


class S3DISWholeScene(Dataset):
    """
    * This class serves only the training data during prediction
    * prepare to give prediction on each points

    Args:
        Dataset (Object): Build in pytorch Dataset class which support multi-processing and give 
                        a standard pipeline support for training and testing our models.
    """
    def __init__(self, split='test', test_area=5, stride=0.5, padding=0.001):
        super().__init__()
        """HYPER PARAMETERS LOADING"""
        PARAMS = json.loads(open(f'{DATA_PATH}/dataset_config.json').read())
        self.num_point = PARAMS['num_point']
        self.block_size = PARAMS['block_size']
        self.padding = padding
        self.stride = stride
        rooms = sorted(os.listdir(PARAMS['data_root']))
        rooms = [room for room in rooms if 'Area_' in room]

        assert split in ['train', 'test']
        if split == 'train':
            self.file_list = [room for room in rooms if not 'Area_{}'.format(test_area) in room] # Training Areas without the Test_Area
        else:
            self.file_list = [room for room in rooms if 'Area_{}'.format(test_area) in room] # Test Area @ByDefault test Area_5

        self.scene_points_num = []
        self.scene_points_list = []
        self.semantic_labels_list = []
        self.room_coord_min, self.room_coord_max = [], []

        for file in self.file_list:
            data = np.load(PARAMS['data_root'] + file)
            points = data[:, :3]
            self.scene_points_list.append(data[:, :6])
            self.semantic_labels_list.append(data[:, 6])
            coord_min, coord_max = np.amin(points, axis=0)[
                :3], np.amax(points, axis=0)[:3]
            self.room_coord_min.append(
                coord_min), self.room_coord_max.append(coord_max)
        assert len(self.scene_points_list) == len(self.semantic_labels_list)

        labelweights = np.zeros(PARAMS['num_classes'])
        for seg in self.semantic_labels_list:
            tmp, _ = np.histogram(seg, range(14))
            self.scene_points_num.append(seg.shape[0])
            labelweights += tmp
        labelweights = labelweights.astype(np.float32)
        labelweights = labelweights / np.sum(labelweights)
        self.labelweights = np.power(np.amax(labelweights) / labelweights, 1 / 3.0)

    def __getitem__(self, index):
        """Returns the data points and labels for train set and validation set

        Args:
            idx (int): Which index need to be selected

        Returns:
            touple(points, labels): return the points and labels data for the given idx
        """
        point_set_ini = self.scene_points_list[index]
        points = point_set_ini[:, :6]
        labels = self.semantic_labels_list[index]
        coord_min, coord_max = np.amin(points, axis=0)[:3], np.amax(points, axis=0)[:3]
        grid_x = int(np.ceil(float(coord_max[0] - coord_min[0] - self.block_size) / self.stride) + 1)
        grid_y = int(np.ceil(float(coord_max[1] - coord_min[1] - self.block_size) / self.stride) + 1)
        data_room, label_room, sample_weight, index_room = np.array([]), np.array([]), np.array([]),  np.array([])
        for index_y in range(0, grid_y):
            for index_x in range(0, grid_x):
                s_x = coord_min[0] + index_x * self.stride
                e_x = min(s_x + self.block_size, coord_max[0])
                s_x = e_x - self.block_size
                s_y = coord_min[1] + index_y * self.stride
                e_y = min(s_y + self.block_size, coord_max[1])
                s_y = e_y - self.block_size
                point_idxs = np.where(
                        (points[:, 0] >= s_x - self.padding) & 
                        (points[:, 0] <= e_x + self.padding) & 
                        (points[:, 1] >= s_y - self.padding) & 
                        (points[:, 1] <= e_y + self.padding)
                    )[0]
                if point_idxs.size == 0:
                    continue
                num_batch = int(np.ceil(point_idxs.size / self.num_point))
                point_size = int(num_batch * self.num_point)
                replace = False if (point_size - point_idxs.size <= point_idxs.size) else True
                point_idxs_repeat = np.random.choice(point_idxs, point_size - point_idxs.size, replace=replace)
                point_idxs = np.concatenate((point_idxs, point_idxs_repeat))
                np.random.shuffle(point_idxs)
                data_batch = points[point_idxs, :]
                normlized_xyz = np.zeros((point_size, 3))
                normlized_xyz[:, 0] = data_batch[:, 0] / coord_max[0]
                normlized_xyz[:, 1] = data_batch[:, 1] / coord_max[1]
                normlized_xyz[:, 2] = data_batch[:, 2] / coord_max[2]
                data_batch[:, 0] = data_batch[:, 0] - (s_x + self.block_size / 2.0)
                data_batch[:, 1] = data_batch[:, 1] - (s_y + self.block_size / 2.0)
                data_batch[:, 3:6] /= 255.0
                data_batch = np.concatenate((data_batch, normlized_xyz), axis=1)
                label_batch = labels[point_idxs].astype(int)
                batch_weight = self.labelweights[label_batch]

                data_room = np.vstack([data_room, data_batch]) if data_room.size else data_batch
                label_room = np.hstack([label_room, label_batch]) if label_room.size else label_batch
                sample_weight = np.hstack([sample_weight, batch_weight]) if label_room.size else batch_weight
                index_room = np.hstack([index_room, point_idxs]) if index_room.size else point_idxs
        data_room = data_room.reshape((-1, self.num_point, data_room.shape[1]))
        label_room = label_room.reshape((-1, self.num_point))
        sample_weight = sample_weight.reshape((-1, self.num_point))
        index_room = index_room.reshape((-1, self.num_point))
        return data_room, label_room, sample_weight, index_room

    def __len__(self):
        """Returns the number of samples in the dataset (Train Data or Valid Data).

        Returns:
            int: length of room_idxs list
        """
        return len(self.scene_points_list)


if __name__ == '__main__':
    """Test our Dataset by torch Dataloader
    """
    point_data = S3DISDataset(split='train', test_area=5, transform=None)
    print('point data size:', point_data.__len__())
    print('point data 0 shape:', point_data.__getitem__(0)[0].shape)
    print('point label 0 shape:', point_data.__getitem__(0)[1].shape)
    manual_seed = 123
    random.seed(manual_seed)
    np.random.seed(manual_seed)
    torch.manual_seed(manual_seed)
    torch.cuda.manual_seed_all(manual_seed)

    train_loader = torch.utils.data.DataLoader(point_data, batch_size=16, shuffle=True)
    end = time.time()
    for i, (input, target) in enumerate(train_loader):
        print('time: {}/{}--{}'.format(i+1,
                len(train_loader), time.time() - end))
        end = time.time()