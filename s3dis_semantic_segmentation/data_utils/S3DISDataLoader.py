import os
import numpy as np
import torch
import time
import random
import json
from tqdm import tqdm
from torch.utils.data import Dataset


class S3DISDataset(Dataset):
    """Custom dataset class for standford indoor3d dataset which inherit pytorch Dataset class
    and override the default __getitem__ method to get the training data and __len__ method.
    * This class serves the training data and the validation data respectively
    * Transformation of training data is optional and can be customized

    Args:
        Dataset (_type_): Build in pytorch Dataset class which support multi-processing and give 
                        a standard pipeline support for training and testing our models.
    """
    def __init__(self, split='train', test_area=5, transform=None):
        super().__init__()
        """HYPER PARAMETERS LOADING"""
        PARAMS = json.loads(open('C:/Users/user/Desktop/SPL3/Project/LiDAR_Classification_APP/s3dis_semantic_segmentation/data_utils/dataset_config.json').read())
        self.num_point = PARAMS['num_point']
        self.block_size = PARAMS['block_size']
        self.transform = transform

        self.room_points, self.room_labels = [], []
        self.room_coord_min, self.room_coord_max = [], []
        num_point_all = []

        labelweights = np.zeros(PARAMS['num_classes'])
        rooms = sorted(os.listdir(PARAMS['data_root']))
        rooms = [room for room in rooms if 'Area_' in room]

        if split == 'train':
            rooms_split = [room for room in rooms if not 'Area_{}'.format(test_area) in room] # Training Areas without the Test_Area
        else:
            rooms_split = [room for room in rooms if 'Area_{}'.format(test_area) in room] # Test Area @ByDefault test Area_5

        for room_name in tqdm(rooms_split, total=len(rooms_split)):
            room_path = os.path.join(PARAMS['data_root'], room_name)
            room_data = np.load(room_path)
            # The room_data contains 7 columns vector ( N*7) : XYZ_RGB_L (cordinates, colors, labels)
            points, labels = room_data[:, 0:6], room_data[:, 6]

            # More Frequent Labels should be chosen more frequencies
            tmp, _ = np.histogram(labels, range(14))   
            labelweights += tmp
            coord_min, coord_max = np.amin(points, axis=0)[:3], np.amax(points, axis=0)[:3]

            # Store all room_data
            self.room_points.append(points) 
            self.room_labels.append(labels)
            self.room_coord_min.append(coord_min)
            self.room_coord_max.append(coord_max)
            num_point_all.append(labels.size)

        # Calculate sample selection probabilities
        labelweights = labelweights.astype(np.float32)
        labelweights = labelweights / np.sum(labelweights)
        self.labelweights = np.power(np.amax(labelweights) / labelweights, 1 / 3.0)
        print(self.labelweights)
        sample_prob = num_point_all / np.sum(num_point_all)
        num_iter = int(np.sum(num_point_all) * PARAMS['sample_rate'] / self.num_point)

        room_idxs = []  #Store all samples for train set and validation set
        for index in range(len(rooms_split)):
            room_idxs.extend(
                [index] * int(round(sample_prob[index] * num_iter)))
        self.room_idxs = np.array(room_idxs)
        print("Total {} samples in {} set.".format(len(self.room_idxs), split))

    def __getitem__(self, idx):
        """Returns the data points and labels for train set and validation set

        Args:
            idx (int): Which index need to be selected

        Returns:
            touple(points, labels): return the points and labels data for the given idx
        """
        room_idx = self.room_idxs[idx]          #Select a sample point cloud
        points = self.room_points[room_idx]     #Get all points XYZ_RGB (N*6) from the point cloud
        labels = self.room_labels[room_idx]     #Get the labels L(N*1) from the point cloud

        selected_point_idxs, center = self._get_fix_sized_sample_mask(points)

        # Normalize sample data points (XYZ_RGB)
        selected_points = points[selected_point_idxs, :] 
        current_points = np.zeros((self.num_point, 9))  # N * 9 (XYZ_RGB_normalXYZ)
        current_points[:, 6] = selected_points[:, 0] / self.room_coord_max[room_idx][0]
        current_points[:, 7] = selected_points[:, 1] / self.room_coord_max[room_idx][1]
        current_points[:, 8] = selected_points[:, 2] / self.room_coord_max[room_idx][2]
        selected_points[:, 0] = selected_points[:, 0] - center[0]
        selected_points[:, 1] = selected_points[:, 1] - center[1]
        selected_points[:, 3:6] /= 255.0
        current_points[:, 0:6] = selected_points
        current_labels = labels[selected_point_idxs]

        if self.transform is not None:
            current_points, current_labels = self.transform(
                current_points, current_labels)
        return current_points, current_labels

    def _get_fix_sized_sample_mask(self, points):
        """Get down-sample or up-sample mask to sample points to num_points_per_sample

        Returns:
            touple(list, list): return the selected_point_idxs (up_sampled or down_sampled) and the random centered points
        """
        N_points = points.shape[0]
        while (True):
            center = points[np.random.choice(N_points)][:3]
            block_min = center - [self.block_size *0.5, self.block_size*0.5, 0]
            block_max = center + [self.block_size *0.5, self.block_size*0.5, 0]
            point_idxs = np.where(
                                (points[:, 0] >= block_min[0]) & 
                                (points[:, 0] <= block_max[0]) & 
                                (points[:, 1] >= block_min[1]) & 
                                (points[:, 1] <= block_max[1])
                            )[0]
            if point_idxs.size > 1024:
                break

        if point_idxs.size >= self.num_point:
            selected_point_idxs = np.random.choice(point_idxs, self.num_point, replace=False)
        else:
            selected_point_idxs = np.random.choice(point_idxs, self.num_point, replace=True)
        return selected_point_idxs, center
    
    def __len__(self):
        """Returns the number of samples in the dataset (Train Data or Valid Data).

        Returns:
            int: length of room_idxs list
        """
        return len(self.room_idxs)


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
        PARAMS = json.loads(open('C:/Users/user/Desktop/SPL3/Project/LiDAR_Classification_APP/s3dis_semantic_segmentation/data_utils/dataset_config.json').read())
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
