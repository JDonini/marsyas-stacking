#!/bin/bash

NUMBER_FOLD=$(python "$(pwd)"/utils/config_to_shell.py "NUMBER_FOLD")
MARSYAS_RUBY=$(python "$(pwd)"/utils/config_to_shell.py "MARSYAS_RUBY")
VALIDATION=$(python "$(pwd)"/utils/config_to_shell.py "K_FOLD_VALIDATION_TXT")
STACKING=$(python "$(pwd)"/utils/config_to_shell.py "K_FOLD_STACKING")

for i in $(seq "${NUMBER_FOLD}")
do
    ruby "${MARSYAS_RUBY}"/per-tag-and-global-precision-recall-fixed.rb "${VALIDATION}""${i}"/ground_truth.txt "${STACKING}""${i}"/stage1_predictions.txt > "${STACKING}""${i}"/stage1_evaluation.txt
done

for i in $(seq "${NUMBER_FOLD}")
do
    ruby "${MARSYAS_RUBY}"/per-tag-and-global-precision-recall-fixed.rb "${VALIDATION}""${i}"/ground_truth.txt "${STACKING}""${i}"/stage2_predictions.txt > "${STACKING}""${i}"/stage2_evaluation.txt
done

echo "Computing evaluation ... "

python src/compute_evaluation_k_fold.py
