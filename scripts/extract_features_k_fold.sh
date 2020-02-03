#!/bin/bash

START=$(date +%s)

NUMBER_FOLD=$(python "$(pwd)"/utils/config_to_shell.py "NUMBER_FOLD")
AUDIO=$(python "$(pwd)"/utils/config_to_shell.py "AUDIO")
MARSYAS_BEXTRACT=$(python "$(pwd)"/utils/config_to_shell.py "MARSYAS_BEXTRACT")
TRAIN_TXT=$(python "$(pwd)"/utils/config_to_shell.py "K_FOLD_TRAIN_TXT")
TEST_TXT=$(python "$(pwd)"/utils/config_to_shell.py "K_FOLD_TEST_TXT")
TRAIN_ARFF=$(python "$(pwd)"/utils/config_to_shell.py "K_FOLD_TRAIN_ARFF")
TEST_ARFF=$(python "$(pwd)"/utils/config_to_shell.py "K_FOLD_TEST_ARFF")

for i in $(seq "${NUMBER_FOLD}")
do
    ${MARSYAS_BEXTRACT} -ws 1024 -l -1 -sv -fe "${TRAIN_TXT}""${i}"/train.txt -w "${TRAIN_ARFF}""${i}"/train.arff -od "${AUDIO}"
done

for i in $(seq "${NUMBER_FOLD}")
do
    ${MARSYAS_BEXTRACT} -ws 1024 -l -1 -sv -fe "${TEST_TXT}""${i}"/test.txt -w "${TEST_ARFF}""${i}"/test.arff  -od "${AUDIO}"
done

END=$(date +%s)
DIFF=$(( $END - $START ))
echo "Tempo de execução : $DIFF seconds"

