import os
import open3d as o3d
import numpy as np
from semantic_dataset import train_full_file_prefixes


def view_point_cloud_data(pcd_file):
    pcd = o3d.io.read_point_cloud(pcd_file)
    o3d.visualization.draw_geometries([pcd],
                                      width=700,height=700,left=50,top=50,
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024])


def point_cloud_np_to_pcd(raw_dir, file_prefix, view=False):
    pcd_file = os.path.join(raw_dir, file_prefix + ".pcd")

    # Skip if already done
    if os.path.isfile(pcd_file):
        print("pcd {} exists, skipped".format(pcd_file))
        if view:
            view_point_cloud_data(pcd_file)
        return

    # converting .npz -> .pcd
    print("converting .npz->.pcd")
    print("pcd: {}".format(pcd_file))
    try:
        data_colors = np.load(os.path.join(
            raw_dir, file_prefix + "_colors.npz"))
        # data_labels = np.load(os.path.join(
        #     raw_dir, file_prefix + "_labels.npz"))
        data_points = np.load(os.path.join(
            raw_dir, file_prefix + "_vertices.npz"))
    except:
        print("File Not Found Error")

    data_colors = data_colors[data_colors.files[0]]
    # data_labels = data_labels[data_labels.files[0]]
    data_points = data_points[data_points.files[0]]

    # sort according to x to speed up computation of boxes and z-boxes
    # sort_idx = np.argsort(data_points[:, 0])
    # data_points = data_points[sort_idx]
    # data_labels = data_labels[sort_idx]
    # data_colors = data_colors[sort_idx]

    # Normalize RGB
    data_colors = data_colors.astype('float32')/255.0

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(data_points)
    pcd.colors = o3d.utility.Vector3dVector(data_colors)

    o3d.io.write_point_cloud(pcd_file, pcd)
    if view:
        view_point_cloud_data(pcd_file)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    dataset_dir = os.path.join(current_dir, "dataset")
    raw_dir = os.path.join(dataset_dir, "semantic_raw")
    # print(raw_dir)
    for file_prefix in train_full_file_prefixes:
        point_cloud_np_to_pcd(
            raw_dir=raw_dir, file_prefix=file_prefix, view=True)
