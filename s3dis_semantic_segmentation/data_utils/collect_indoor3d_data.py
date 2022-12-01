import os
import sys
from indoor3d_util import DATA_PATH, collect_point_label

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)

annotation_paths = [line.rstrip() for line in open(
    os.path.join(BASE_DIR, 'meta_data/annotation_paths.txt'))]
annotation_paths = [os.path.join(DATA_PATH, p) for p in annotation_paths]

output_folder = os.path.join(ROOT_DIR, 'data/stanford_indoor3d')
# if not os.path.exists(output_folder):
#     os.mkdir(output_folder)
output_folder.mkdir(exist_ok=True)

# Note: there is an extra character in the v1.2 data in Area_5/hallway_6. It's fixed manually.
for annotation_path in annotation_paths:
    print(annotation_path)
    try:
        elements = annotation_path.split('/')
        out_filename = elements[-3]+'_' + \
            elements[-2]+'.npy'  # Area_1_hallway_1.npy
        collect_point_label(annotation_path, os.path.join(
            output_folder, out_filename), 'numpy')
    except:
        print(annotation_path, 'ERROR!!')
