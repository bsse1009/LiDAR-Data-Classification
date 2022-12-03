import os
import sys
from unittest import result

################ Configuration file for Traing and Tesing ##############
# start_index = 0
# end_index = 2
##########################################

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = BASE_DIR
log_dir = 'log'
root = 'data/s3dis/stanford_indoor3d/'
sys.path.append(os.path.join(ROOT_DIR, 'models'))

classes = ['ceiling', 'floor', 'wall', 'beam', 'column', 'window', 'door', 'table', 'chair', 'sofa', 'bookcase', 'board', 'clutter']
class2label = {cls: i for i, cls in enumerate(classes)}
seg_classes = class2label
seg_label_to_cat = {}

for i, cat in enumerate(seg_classes.keys()):
    seg_label_to_cat[i] = cat

model = 'pointnet_sem_seg'
epoch = 32
learning_rate = 0.001
optimizer = 'Adam'
decay_rate = 1e-4
lr_decay = 0.7
step_size = 10
NUM_CLASSES = 13
NUM_POINT = 4096
BATCH_SIZE = 16

version = '1.0'