#!/bin/bash

MARSYAS_KEA=$(python "$(pwd)"/utils/config_to_shell.py "MARSYAS_KEA")
MARSYAS_RUBY=$(python "$(pwd)"/utils/config_to_shell.py "MARSYAS_RUBY")
STACKING=$(python "$(pwd)"/utils/config_to_shell.py "HOLDOUT_STACKING")
TRAIN_TXT=$(python "$(pwd)"/utils/config_to_shell.py "HOLDOUT_TRAIN_TXT")

${MARSYAS_KEA} -m tags -id "${STACKING}" -od "${STACKING}" -w train.arff.affinities.arff -tw test.arff.affinities.arff -pr stage2_affinities.txt
"${MARSYAS_RUBY}"/threshold_binarization.rb "${TRAIN_TXT}" "${STACKING}"stage2_affinities.txt > "${STACKING}"stage2_predictions.txt
