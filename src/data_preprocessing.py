import os
import sys
import numpy as np
import pandas as pd
import librosa
import librosa.display
from generate_structure import BINARY_ANNOTATIONS, AUDIO
sys.path.append('src/')
from config_to_python import EXT_AUDIO_WAV, EXT_AUDIO_MP3, AUDIO_THRESHOLD, SEED

np.random.seed(SEED)

annotation_list, song_list = [], []


def remove_short_audio():
    for file in os.listdir(AUDIO):
        y, sr = librosa.load(AUDIO + file)
        audio_duration = librosa.core.get_duration(y=y, sr=sr)
        if audio_duration < AUDIO_THRESHOLD:
            audio_name, _ = file.split(EXT_AUDIO_WAV)
            if os.path.isfile(AUDIO + file):
                os.remove(AUDIO + file)
                print('Audio removed: {} -- Audio time: {:.4}'.format(file, audio_duration))


def remove_missing_data():
    fp = open(BINARY_ANNOTATIONS, 'r+')

    content = fp.read().split('\n')
    cab = content[0].split(',')
    content = content[1:]

    for i in range(len(content)):
        content[i] = content[i].split(',')
        annotation_list.append(content[i][0].replace('.png', '.wav'))

    for file in os.listdir(AUDIO):
        song_list.append(file)

    annotation_remove = [item for item in annotation_list if item not in song_list]
    song_remove = [item for item in song_list if item not in annotation_list]

    print('Remove Annotation - ', annotation_remove)
    print(len(annotation_remove))

    print('Remove Song - ', song_remove)
    print(len(song_remove))

    df = pd.read_csv(BINARY_ANNOTATIONS)
    for file in annotation_remove:
        file = file.replace('.wav', '.png')
        df = df[df.song_name != file]
    df.to_csv(BINARY_ANNOTATIONS, sep=',', index=False)


if __name__ == '__main__':
    remove_short_audio()
    remove_missing_data()
