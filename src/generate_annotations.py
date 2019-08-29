import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from generate_structure import BINARY_ANNOTATIONS, TAG_ANNOTATIONS, SONG_ANNOTATIONS

convert_list = []


def create_one_hot_annotations():
    df = pd.read_csv(SONG_ANNOTATIONS, sep='\t', index_col='song_name')
    df['tags'] = df['tags'].apply(lambda x: list(set(x.split(','))))

    mlb = MultiLabelBinarizer()
    one_hot_vector = pd.DataFrame(
        mlb.fit_transform(df['tags']),
        index=df.index,
        columns=mlb.classes_
    )
    one_hot_vector.to_csv(BINARY_ANNOTATIONS, sep=',')


def create_annotations():
    fp = open(BINARY_ANNOTATIONS, 'r+')

    content = fp.read().split('\n')
    cab = content[0].split(',')
    content = content[1:]

    for i in range(len(content)):
        content[i] = content[i].split(',')
        tags = [i for i, x in enumerate(content[i]) if x == '1']
        for data in tags:
            convert_list.append('{0}\t{1}'.format(content[i][0].replace('.png', '.wav'), cab[data]))

    open(TAG_ANNOTATIONS, 'w+').write('\n'.join(convert_list))


if __name__ == '__main__':
    create_one_hot_annotations()
    create_annotations()
