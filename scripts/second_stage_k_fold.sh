#!/bin/bash

START=$(date +%s)

NUMBER_FOLD=$(python "$(pwd)"/utils/config_to_shell.py "NUMBER_FOLD")
MARSYAS_KEA=$(python "$(pwd)"/utils/config_to_shell.py "MARSYAS_KEA")
MARSYAS_RUBY=$(python "$(pwd)"/utils/config_to_shell.py "MARSYAS_RUBY")
TRAIN_TXT=$(python "$(pwd)"/utils/config_to_shell.py "K_FOLD_TRAIN_TXT")
STACKING=$(python "$(pwd)"/utils/config_to_shell.py "K_FOLD_STACKING")

for i in $(seq "${NUMBER_FOLD}")
do
    ${MARSYAS_KEA} -m tags -id "${STACKING}""${i}"/ -od "${STACKING}""${i}/" -w train.arff.affinities.arff -tw test.arff.affinities.arff -pr stage2_affinities.txt
done

for i in $(seq "${NUMBER_FOLD}")
do
    "${MARSYAS_RUBY}"/threshold_binarization.rb "${TRAIN_TXT}""${i}"/train.txt "${STACKING}""${i}"/stage2_affinities.txt > "${STACKING}"/"${i}"/stage2_predictions.txt
done

END=$(date +%s)
DIFF=$(( $END - $START ))
echo "Tempo de execução : $DIFF seconds"
