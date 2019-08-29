from sklearn.model_selection import KFold
import pandas as pd
import sys
from generate_structure import TAG_ANNOTATIONS, K_FOLD_ANNOTATIONS, AUDIO
sys.path.append('utils')
from config_to_python import NUMBER_FOLD


def k_fold_cross_validation():
    data = pd.read_csv(TAG_ANNOTATIONS, header=None, delimiter='\t')
    data.rename(
        columns={
            0: 'song_name',
            1: 'song_tag'
        },
        inplace=True
    )

    kf = KFold(n_splits=NUMBER_FOLD, shuffle=False)
    for i in range(1, NUMBER_FOLD + 1):
        for train_index, test_index in kf.split(data):
            pd.set_option('mode.chained_assignment', None)

            train = data.iloc[train_index]
            train.loc[:, 'song_name'] = AUDIO + train['song_name']
            train.to_csv(K_FOLD_ANNOTATIONS + str(i) + '/train.txt', sep='\t', index=False, header=False)

            test = data.iloc[test_index]['song_name']
            test = AUDIO + test
            test.to_csv(K_FOLD_ANNOTATIONS + str(i) + '/test.txt', sep='\t', index=False, header=False)

            ground_truth = data.iloc[test_index]
            ground_truth.loc[:, 'song_name'] = AUDIO + ground_truth['song_name']
            ground_truth.to_csv(K_FOLD_ANNOTATIONS + str(i) + '/ground_truth.txt', sep='\t', index=False, header=False)


if __name__ == "__main__":
    k_fold_cross_validation()
