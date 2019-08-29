#!/bin/bash

AUDIO=$(python "$(pwd)"/utils/config_to_shell.py "AUDIO")
MARSYAS_BEXTRACT=$(python "$(pwd)"/utils/config_to_shell.py "MARSYAS_BEXTRACT")
TRAIN_TXT=$(python "$(pwd)"/utils/config_to_shell.py "HOLDOUT_TRAIN_TXT")
TEST_TXT=$(python "$(pwd)"/utils/config_to_shell.py "HOLDOUT_TEST_TXT")
TRAIN_ARFF=$(python "$(pwd)"/utils/config_to_shell.py "HOLDOUT_TRAIN_ARFF")
TEST_ARFF=$(python "$(pwd)"/utils/config_to_shell.py "HOLDOUT_TEST_ARFF")

${MARSYAS_BEXTRACT} -ws 1024 -l -1 -sv -fe "${TRAIN_TXT}" -w "${TRAIN_ARFF}" -od "${AUDIO}"
${MARSYAS_BEXTRACT} -ws 1024 -l -1 -sv -fe "${TEST_TXT}" -w "${TEST_ARFF}" -od "${AUDIO}"
