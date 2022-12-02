import open3d as o3d
import numpy as np
# import laspy as las
# import lidario as lio


def point_cloud_reader(path):
    # path = "../../DATA/Point Cloud Sample/2020_Drone_M.las"
    # path = "../../DATA/ALL_BUILDING_DATA/Strasbourg/all_buidings.tif"

    SUPPORTED_FILEFORMATS = ["xyz", "xyzn", "xyzrgb", "pts", "ply", "pcd"]
    extension = path.split("/")[-1].split(".")[1]
    pcd = o3d.geometry.PointCloud()

    if extension in SUPPORTED_FILEFORMATS:
        pcd = o3d.io.read_point_cloud(path)
    elif extension == "txt":
        pcd = o3d.io.read_point_cloud(path, format='xyz')
    # elif extension == "las":
    #     las = las.read(path)
    #     point_cloud = np.stack([las.X, las.Y, las.Z], axis=0).transpose((1, 0))
    #     pcd.points = o3d.utility.Vector3dVector(point_cloud)
    # elif extension == "tif":
    #     translator = lio.Translator("geotiff", "np")
    #     point_cloud = translator.translate(path)
    #     pcd.points = o3d.utility.Vector3dVector(point_cloud)
    elif extension == "obj":
        data = open(path, "r")
        lines = data.readlines()
        points = np.array([line.strip().split()[1:4] for line in lines if line[0] == "v"])
        colors = np.array([line.strip().split()[4:7] for line in lines if line[0] == "v"])
        pcd.points = o3d.utility.Vector3dVector(points.astype(np.float))
        pcd.colors = o3d.utility.Vector3dVector(colors.astype(np.float))
    else:
        point_cloud = np.loadtxt(path)
        pcd.points = o3d.utility.Vector3dVector(point_cloud[:3])
        pcd.colors = o3d.utility.Vector3dVector(point_cloud[3:6])

    return pcd

# print(list(las.point_format.dimension_names))
# print(las.X,
#       las.intensity)
# print(set(list(las.classification)))


# voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(
#     pcd, voxel_size=.5)
# print(voxel_grid)
# o3d.visualization.draw_geometries([voxel_grid])
