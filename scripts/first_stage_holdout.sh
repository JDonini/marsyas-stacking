#!/bin/bash

START=$(date +%s)

MARSYAS_KEA=$(python "$(pwd)"/utils/config_to_shell.py "MARSYAS_KEA")
MARSYAS_RUBY=$(python "$(pwd)"/utils/config_to_shell.py "MARSYAS_RUBY")
TRAIN_TXT=$(python "$(pwd)"/utils/config_to_shell.py "HOLDOUT_TRAIN_TXT")
STACKING=$(python "$(pwd)"/utils/config_to_shell.py "HOLDOUT_STACKING")

${MARSYAS_KEA} -m tags -id "${STACKING}" -od "${STACKING}" -w train.arff -tw test.arff -pr stage1_affinities.txt
"${MARSYAS_RUBY}"/threshold_binarization.rb "${TRAIN_TXT}" "${STACKING}"stage1_affinities.txt > "${STACKING}"stage1_predictions.txt

END=$(date +%s)
DIFF=$(( $END - $START ))
echo "Tempo de execução : $DIFF seconds"
