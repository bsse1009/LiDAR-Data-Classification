import sys
import open3d as o3d


def test_downsampled_pcd(pcd_file):
    pcd = o3d.io.read_point_cloud(pcd_file)
    o3d.visualization.draw_geometries([pcd],
                                      width=700,height=700,left=50,top=50,
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024])


if __name__ == '__main__':
    path = "C:/Users/user/Desktop/SPL3/Project/LiDAR_Classification_APP/3D-Semantic-Segmentation/dataset/semantic_downsampled/bildstein_station1_xyz_intensity_rgb.pcd"
    test_downsampled_pcd(path)