import os
import sys
sys.path.append('utils')
from config_to_python import NUMBER_FOLD

pwd = os.getcwdb().decode('utf8')
database_name = os.environ["database_name"]

AUDIO = '/mnt/Files/Database/' + database_name + '/audios/'
DATABASE = pwd + '/database/' + database_name

BINARY_ANNOTATIONS = '/mnt/Files/Database/' + database_name + '/annotations/binary_annotation.csv'
SONG_ANNOTATIONS = '/mnt/Files/Database/' + database_name + '/annotations/song_annotations.csv'
TAG_ANNOTATIONS = '/mnt/Files/Database/' + database_name + '/annotations/song_tag_annotations.txt'

HOLDOUT = DATABASE + '/holdout/'
HOLDOUT_ANNOTATIONS = HOLDOUT + 'annotations/'
HOLDOUT_OUT = HOLDOUT + 'out/'
HOLDOUT_EVALUATION = HOLDOUT_OUT + 'evaluation/'
HOLDOUT_STACKING = HOLDOUT_OUT + 'stacking/'

HOLDOUT_TRAIN = HOLDOUT_ANNOTATIONS + 'train.txt'
HOLDOUT_TEST = HOLDOUT_ANNOTATIONS + 'test.txt'
HOLDOUT_VALIDATION = HOLDOUT_ANNOTATIONS + 'ground_truth.txt'

HOLDOUT_TRAIN_ARFF = HOLDOUT_STACKING + 'train.arff'
HOLDOUT_TEST_ARFF = HOLDOUT_STACKING + 'test.arff'

K_FOLD = DATABASE + '/k_fold/'
K_FOLD_ANNOTATIONS = K_FOLD + 'annotations/'
K_FOLD_OUT = K_FOLD + 'out/'
K_FOLD_EVALUATION = K_FOLD_OUT + 'evaluation/'
K_FOLD_STACKING = K_FOLD_OUT + 'stacking/'


for i in range(1, NUMBER_FOLD + 1):
    K_FOLD_TRAIN = K_FOLD_ANNOTATIONS + str(i)
    K_FOLD_TEST = K_FOLD_ANNOTATIONS + str(i)
    K_FOLD_VALIDATION = K_FOLD_ANNOTATIONS + str(i)
    K_STACKING = K_FOLD_OUT + 'stacking/' + str(i)
    os.makedirs(K_FOLD_TRAIN, exist_ok=True)
    os.makedirs(K_FOLD_TEST, exist_ok=True)
    os.makedirs(K_FOLD_VALIDATION, exist_ok=True)
    os.makedirs(K_STACKING, exist_ok=True)


K_FOLD_TRAIN_ARFF = K_FOLD_STACKING + 'train.arff'
K_FOLD_TEST_ARFF = K_FOLD_STACKING + 'test.arff'

STAGE_1 = '/stage1_evaluation.txt'
STAGE_2 = '/stage2_evaluation.txt'

list_dir = [DATABASE, HOLDOUT, HOLDOUT_ANNOTATIONS, HOLDOUT_OUT, HOLDOUT_EVALUATION, HOLDOUT_STACKING,
            K_FOLD, K_FOLD_ANNOTATIONS, K_FOLD_OUT, K_FOLD_EVALUATION, K_FOLD_STACKING
            ]

for fold in list_dir:
    os.makedirs(fold, exist_ok=True)
