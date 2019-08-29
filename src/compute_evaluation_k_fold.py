import pandas as pd
import sys
from generate_structure import K_FOLD_EVALUATION, STAGE_1, STAGE_2, K_FOLD_STACKING
sys.path.append('utils')
from config_to_python import NUMBER_FOLD

fold_per_tag_stage_1, precision_per_tag_stage_1, recall_per_tag_stage_1, accuracy_per_tag_stage_1, f_score_per_tag_stage_1 = [], [], [], [], []
fold_global_stage_1, precision_global_stage_1, recall_global_stage_1, accuracy_global_stage_1, f_score_global_stage_1 = [], [], [], [], []
average_precision_stage_1, average_recall_stage_1, average_accuracy_stage_1, average_f_score_stage_1 = 0.0, 0.0, 0.0, 0.0

fold_per_tag_stage_2, precision_per_tag_stage_2, recall_per_tag_stage_2, accuracy_per_tag_stage_2, f_score_per_tag_stage_2 = [], [], [], [], []
fold_global_stage_2, precision_global_stage_2, recall_global_stage_2, accuracy_global_stage_2, f_score_global_stage_2 = [], [], [], [], []
average_precision_stage_2, average_recall_stage_2, average_accuracy_stage_2, average_f_score_stage_2 = 0.0, 0.0, 0.0, 0.0


per_tag_values_stage_1 = {
    'Fold': fold_per_tag_stage_1,
    'Precision': precision_per_tag_stage_1,
    'Recall': recall_per_tag_stage_1,
    'Accuracy': accuracy_per_tag_stage_1,
    'F-Score': f_score_per_tag_stage_1
}

global_values_stage_1 = {
    'Fold': fold_global_stage_1,
    'Precision': precision_global_stage_1,
    'Recall': recall_global_stage_1,
    'Accuracy': accuracy_global_stage_1,
    'F-Score': f_score_global_stage_1
}

per_tag_values_stage_2 = {
    'Fold': fold_per_tag_stage_2,
    'Precision': precision_per_tag_stage_2,
    'Recall': recall_per_tag_stage_2,
    'Accuracy': accuracy_per_tag_stage_2,
    'F-Score': f_score_per_tag_stage_2
}

global_values_stage_2 = {
    'Fold': fold_global_stage_2,
    'Precision': precision_global_stage_2,
    'Recall': recall_global_stage_2,
    'Accuracy': accuracy_global_stage_2,
    'F-Score': f_score_global_stage_2
}


def stage_1():
    count = 0
    for i in range(1, NUMBER_FOLD + 1):
        with open(K_FOLD_STACKING + str(i) + STAGE_1, 'rt') as lines:
            for line in lines:
                if line[0].isdigit():
                    count += 1
                    if count % 2 == 1:  # Per Tag Values
                        fold_per_tag_stage_1.append(i)
                        precision_per_tag_stage_1.append(
                            float(line.strip('\n').split(' ')[0]))
                        recall_per_tag_stage_1.append(
                            float(line.strip('\n').split(' ')[1]))
                        accuracy_per_tag_stage_1.append(
                            float(line.strip('\n').split(' ')[2]))
                        f_score_per_tag_stage_1.append(
                            float(line.strip('\n').split(' ')[3]))
                    elif count % 2 == 0:  # Global Values
                        fold_global_stage_1.append(i)
                        precision_global_stage_1.append(
                            float(line.strip('\n').split(' ')[0]))
                        recall_global_stage_1.append(
                            float(line.strip('\n').split(' ')[1]))
                        accuracy_global_stage_1.append(
                            float(line.strip('\n').split(' ')[2]))
                        f_score_global_stage_1.append(
                            float(line.strip('\n').split(' ')[3]))

    fold_per_tag_stage_1.append('Avg ' + str(NUMBER_FOLD) + ' folds')
    precision_per_tag_stage_1.append(
        sum(precision_per_tag_stage_1)/NUMBER_FOLD)
    recall_per_tag_stage_1.append(sum(recall_per_tag_stage_1)/NUMBER_FOLD)
    accuracy_per_tag_stage_1.append(sum(accuracy_per_tag_stage_1)/NUMBER_FOLD)
    f_score_per_tag_stage_1.append(sum(f_score_per_tag_stage_1)/NUMBER_FOLD)

    fold_global_stage_1.append(('Avg ' + str(NUMBER_FOLD) + ' folds'))
    precision_global_stage_1.append(sum(precision_global_stage_1)/NUMBER_FOLD)
    recall_global_stage_1.append(sum(recall_global_stage_1)/NUMBER_FOLD)
    accuracy_global_stage_1.append(sum(accuracy_global_stage_1)/NUMBER_FOLD)
    f_score_global_stage_1.append(sum(f_score_global_stage_1)/NUMBER_FOLD)

    df_stage_1_per_tag_values = pd.DataFrame(per_tag_values_stage_1, columns=[
                                             'Fold', 'Precision', 'Recall', 'Accuracy', 'F-Score'])
    df_stage_1_global_values = pd.DataFrame(global_values_stage_1, columns=[
                                            'Fold', 'Precision', 'Recall', 'Accuracy', 'F-Score'])

    df_stage_1_per_tag_values.to_csv(K_FOLD_EVALUATION + '/per_tag_values_stage_1.csv',
                                     sep=',', index=False, encoding='utf-8', float_format='%.4f')
    df_stage_1_global_values.to_csv(K_FOLD_EVALUATION + '/global_values_stage_1.csv',
                                    sep=',', index=False, encoding='utf-8', float_format='%.4f')


def stage_2():
    count = 0
    for i in range(1, NUMBER_FOLD + 1):
        with open(K_FOLD_STACKING + str(i) + STAGE_2, 'rt') as lines:
            for line in lines:
                if line[0].isdigit():
                    count += 1
                    if count % 2 == 1:  # Per Tag Values
                        fold_per_tag_stage_2.append(i)
                        precision_per_tag_stage_2.append(
                            float(line.strip('\n').split(' ')[0]))
                        recall_per_tag_stage_2.append(
                            float(line.strip('\n').split(' ')[1]))
                        accuracy_per_tag_stage_2.append(
                            float(line.strip('\n').split(' ')[2]))
                        f_score_per_tag_stage_2.append(
                            float(line.strip('\n').split(' ')[3]))
                    elif count % 2 == 0:  # Global Values
                        fold_global_stage_2.append(i)
                        precision_global_stage_2.append(
                            float(line.strip('\n').split(' ')[0]))
                        recall_global_stage_2.append(
                            float(line.strip('\n').split(' ')[1]))
                        accuracy_global_stage_2.append(
                            float(line.strip('\n').split(' ')[2]))
                        f_score_global_stage_2.append(
                            float(line.strip('\n').split(' ')[3]))

    fold_per_tag_stage_2.append('Avg' + str(NUMBER_FOLD) + ' folds')
    precision_per_tag_stage_2.append(
        sum(precision_per_tag_stage_2)/NUMBER_FOLD)
    recall_per_tag_stage_2.append(sum(recall_per_tag_stage_2)/NUMBER_FOLD)
    accuracy_per_tag_stage_2.append(sum(accuracy_per_tag_stage_2)/NUMBER_FOLD)
    f_score_per_tag_stage_2.append(sum(f_score_per_tag_stage_2)/NUMBER_FOLD)

    fold_global_stage_2.append(('Avg ' + str(NUMBER_FOLD) + ' folds'))
    precision_global_stage_2.append(sum(precision_global_stage_2)/NUMBER_FOLD)
    recall_global_stage_2.append(sum(recall_global_stage_2)/NUMBER_FOLD)
    accuracy_global_stage_2.append(sum(accuracy_global_stage_2)/NUMBER_FOLD)
    f_score_global_stage_2.append(sum(f_score_global_stage_2)/NUMBER_FOLD)

    df_stage_2_per_tag_values = pd.DataFrame(per_tag_values_stage_2, columns=[
                                             'Fold', 'Precision', 'Recall', 'Accuracy', 'F-Score'])
    df_stage_2_global_values = pd.DataFrame(global_values_stage_2, columns=[
                                            'Fold', 'Precision', 'Recall', 'Accuracy', 'F-Score'])

    df_stage_2_per_tag_values.to_csv(K_FOLD_EVALUATION + '/per_tag_values_stage_2.csv',
                                     sep=',', index=False, encoding='utf-8', float_format='%.4f')
    df_stage_2_global_values.to_csv(K_FOLD_EVALUATION + '/global_values_stage_2.csv',
                                    sep=',', index=False, encoding='utf-8', float_format='%.4f')


if __name__ == "__main__":
    stage_1()
    stage_2()