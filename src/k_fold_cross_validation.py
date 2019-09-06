from sklearn.model_selection import KFold
import pandas as pd
import sys
import numpy as np
from generate_structure import TAG_ANNOTATIONS, K_FOLD_ANNOTATIONS, AUDIO
sys.path.append('utils')
from config_to_python import NUMBER_FOLD, SEED

np.random.seed(SEED)


def k_fold_cross_validation():
    data = pd.read_csv(TAG_ANNOTATIONS, header=None, delimiter='\t')
    data.rename(
        columns={
            0: 'song_id',
            1: 'song_tag'
        },
        inplace=True
    )
    data = data.sort_values(by=['song_id'])

    i = 0
    kf = KFold(n_splits=NUMBER_FOLD, shuffle=False)
    for train_index, test_index in kf.split(data):
        i += 1
        pd.set_option('mode.chained_assignment', None)

        train = data.iloc[train_index]
        train.loc[:, 'song_id'] = AUDIO + train['song_id']
        train.to_csv(K_FOLD_ANNOTATIONS + str(i) + '/train.txt', sep='\t', index=False, header=False)

        test = data.iloc[test_index]['song_id']
        test = AUDIO + test
        test.to_csv(K_FOLD_ANNOTATIONS + str(i) + '/test.txt', sep='\t', index=False, header=False)

        ground_truth = data.iloc[test_index]
        ground_truth.loc[:, 'song_id'] = AUDIO + ground_truth['song_id']
        ground_truth.to_csv(K_FOLD_ANNOTATIONS + str(i) + '/ground_truth.txt', sep='\t', index=False, header=False)


if __name__ == "__main__":
    k_fold_cross_validation()
