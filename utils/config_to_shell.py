import sys
import os

pwd = os.getcwdb().decode('utf8')
database_name = os.environ["database_name"]

if sys.argv[1] == 'NUMBER_FOLD':
    print(5)

elif sys.argv[1] == 'AUDIO':
    print('/mnt/Files/Database/' + database_name + '/audios/')

elif sys.argv[1] == 'HOLDOUT_TRAIN_TXT':
    print(pwd + '/database/' + database_name + '/holdout/annotations/train.txt')

elif sys.argv[1] == 'HOLDOUT_TEST_TXT':
    print(pwd + '/database/' + database_name + '/holdout/annotations/test.txt')

elif sys.argv[1] == 'HOLDOUT_VALIDATION_TXT':
    print(pwd + '/database/' + database_name + '/holdout/annotations/ground_truth.txt')

elif sys.argv[1] == 'HOLDOUT_TRAIN_ARFF':
    print(pwd + '/database/' + database_name + '/holdout/out/stacking/train.arff')

elif sys.argv[1] == 'HOLDOUT_TEST_ARFF':
    print(pwd + '/database/' + database_name + '/holdout/out/stacking/test.arff')

elif sys.argv[1] == 'HOLDOUT_EVALUATION':
    print(pwd + '/database/' + database_name + '/holdout/out/evaluation/')

elif sys.argv[1] == 'HOLDOUT_STACKING':
    print(pwd + '/database/' + database_name + '/holdout/out/stacking/')

elif sys.argv[1] == 'K_FOLD_TRAIN_TXT':
    print(pwd + '/database/' + database_name + '/k_fold/annotations/')

elif sys.argv[1] == 'K_FOLD_TEST_TXT':
    print(pwd + '/database/' + database_name + '/k_fold/annotations/')

elif sys.argv[1] == 'K_FOLD_VALIDATION_TXT':
    print(pwd + '/database/' + database_name + '/k_fold/annotations/')

elif sys.argv[1] == 'K_FOLD_TRAIN_ARFF':
    print(pwd + '/database/' + database_name + '/k_fold/out/stacking/')

elif sys.argv[1] == 'K_FOLD_TEST_ARFF':
    print(pwd + '/database/' + database_name + '/k_fold/out/stacking/')

elif sys.argv[1] == 'K_FOLD_VALIDATION_ARFF':
    print(pwd + '/database/' + database_name + '/k_fold/out/stacking/')    

elif sys.argv[1] == 'K_FOLD_EVALUATION':
    print(pwd + '/database/' + database_name + '/k_fold/out/evaluation/')

elif sys.argv[1] == 'K_FOLD_STACKING':
    print(pwd + '/database/' + database_name + '/k_fold/out/stacking/')

elif sys.argv[1] == 'MARSYAS_BEXTRACT':
    print('/home/juliano/Workspace/marsyas/build/bin/bextract')

elif sys.argv[1] == 'MARSYAS_RUBY':
    print('/home/juliano/Workspace/marsyas/scripts/Ruby')

elif sys.argv[1] == 'MARSYAS_KEA':
    print('/home/juliano/Workspace/marsyas/build/bin/kea')
sys.exit(0)
