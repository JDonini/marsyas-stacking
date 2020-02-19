#!/bin/bash

MARSYAS_RUBY=$(python "$(pwd)"/utils/config_to_shell.py "MARSYAS_RUBY")
VALIDATION_TXT=$(python "$(pwd)"/utils/config_to_shell.py "HOLDOUT_VALIDATION_TXT")
STACKING=$(python "$(pwd)"/utils/config_to_shell.py "HOLDOUT_STACKING")

echo "Computing evaluation ... "

ruby "${MARSYAS_RUBY}"/per-tag-and-global-precision-recall-fixed.rb "${VALIDATION_TXT}" "${STACKING}"stage1_predictions.txt > "${STACKING}"stage1_evaluation.txt
ruby "${MARSYAS_RUBY}"/per-tag-and-global-precision-recall-fixed.rb "${VALIDATION_TXT}" "${STACKING}"stage2_predictions.txt > "${STACKING}"stage2_evaluation.txt

python src/compute_evaluation_holdout.py
