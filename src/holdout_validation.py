from sklearn.model_selection import train_test_split
import pandas as pd
import sys
from generate_structure import TAG_ANNOTATIONS, HOLDOUT_TRAIN, HOLDOUT_TEST, HOLDOUT_VALIDATION, AUDIO
sys.path.append('utils')
from config_to_python import SEED


def holdout():
    data = pd.read_csv(TAG_ANNOTATIONS, delimiter='\t', header=None)
    data.rename(
        columns={
            0: 'song_id',
            1: 'song_tag'
        },
        inplace=True
    )
    data = data.sort_values(by=['song_id'])

    train_index, test_index = train_test_split(data, test_size=0.3, shuffle=False, random_state=SEED)
    pd.set_option('mode.chained_assignment', None)

    train_index.loc[:, 'song_id'] = AUDIO + train_index['song_id']
    train_index.to_csv(HOLDOUT_TRAIN, sep='\t', index=False, header=False)

    test = AUDIO + test_index['song_id']
    test.to_csv(HOLDOUT_TEST, index=False, header=False)

    ground_truth = pd.DataFrame()
    ground_truth.loc[:, 'song_id'] = AUDIO + test_index['song_id'] + '\t' + test_index['song_tag']
    ground_truth.to_csv(HOLDOUT_VALIDATION, sep='\t', index=False, header=False)


if __name__ == "__main__":
    holdout()
