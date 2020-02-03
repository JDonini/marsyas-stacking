#!/bin/sh
show_menu() {
  NORMAL=$(echo "\033[m")
  MENU=$(echo "\033[36m")   #Blue
  NUMBER=$(echo "\033[33m") #yellow
  FGRED=$(echo "\033[41m")
  RED_TEXT=$(echo "\033[31m")
  ENTER_LINE=$(echo "\033[33m")
  echo -e "${MENU}*********************************************${NORMAL}"
  echo -e "${MENU}**${NUMBER} 1)${MENU} CAL500 ${NORMAL}"
  echo -e "${MENU}**${NUMBER} 2)${MENU} FMA ${NORMAL}"
  echo -e "${MENU}**${NUMBER} 3)${MENU} MagnaTagATune ${NORMAL}"
  echo -e "${MENU}**${NUMBER} 4)${MENU} MillionSong ${NORMAL}"
  echo -e "${MENU}*********************************************${NORMAL}"
  echo -e "${ENTER_LINE}Please enter a menu option and enter or ${RED_TEXT} enter to exit. ${NORMAL}"
  read opt

  while [ opt != '' ]; do
    if [[ $opt == "" ]]; then
      exit
    else
      case $opt in
      1)
        clear
        export database_name="CAL500"
        option_picked $database_name
        sub_menu
        ;;

      2)
        clear
        export database_name="FMA"
        option_picked $database_name
        sub_menu
        ;;

      3)
        clear
        export database_name="MagnaTagATune"
        option_picked $database_name
        sub_menu
        ;;

      4)
        clear
        export database_name="MillionSong"
        option_picked $database_name
        sub_menu
        ;;

      5)
        clear
        export database_name="Music2All"
        option_picked $database_name
        sub_menu
        ;;

      x)
        exit
        ;;

      \n)
        exit
        ;;

      *)
        clear
        option_picked "Pick an option from the menu"
        show_menu
        ;;
      esac
    fi
  done
}

function option_picked() {
  COLOR='\033[01;31m' # bold red
  RESET='\033[00;00m' # normal white
  MESSAGE=${@:-"${RESET}Error: No message passed"}
  echo -e "${COLOR}${MESSAGE}${RESET}"
}

pyclean() {
  find . -name "*.pyc" -exec rm -f {} \;
  find . -name "__pycache__" -exec rm -rf {} \;
}

sub_menu() {
  NORMAL=$(echo "\033[m")
  MENU=$(echo "\033[36m")   #Blue
  NUMBER=$(echo "\033[33m") #yellow
  FGRED=$(echo "\033[41m")
  RED_TEXT=$(echo "\033[31m")
  ENTER_LINE=$(echo "\033[33m")
  echo -e "${MENU}*********************************************${NORMAL}"
  echo -e "${MENU}**${RED_TEXT} 0)${MENU} Return to Menu ${NORMAL}"
  echo -e "${MENU}**${NUMBER} 1)${MENU} Generate Structure ${NORMAL}"
  echo -e "${MENU}**${NUMBER} 2)${MENU} Preprocessing Dataset ${NORMAL}"
  echo -e "${MENU}**${NUMBER} 3)${MENU} Generate Annotations ${NORMAL}"
  echo -e "${MENU}*********************************************${NORMAL}"
  echo -e "${MENU}**${NUMBER} 10)${MENU} Generate Holdout${NORMAL}"
  echo -e "${MENU}**${NUMBER} 11)${MENU} Extract Features - Holdout${NORMAL}"
  echo -e "${MENU}**${NUMBER} 12)${MENU} Stacking First Stage - Holdout${NORMAL}"
  echo -e "${MENU}**${NUMBER} 13)${MENU} Stacking Second Stage - Holdout${NORMAL}"
  echo -e "${MENU}**${NUMBER} 14)${MENU} Evaluate Stacking - Holdout${NORMAL}"
  echo -e "${MENU}*********************************************${NORMAL}"
  echo -e "${MENU}**${NUMBER} 20)${MENU} Generate K-Fold${NORMAL}"
  echo -e "${MENU}**${NUMBER} 21)${MENU} Extract Features - K-Fold${NORMAL}"
  echo -e "${MENU}**${NUMBER} 22)${MENU} Stacking First Stage - K-Fold${NORMAL}"
  echo -e "${MENU}**${NUMBER} 23)${MENU} Stacking Second Stage - K-Fold${NORMAL}"
  echo -e "${MENU}**${NUMBER} 24)${MENU} Evaluate Stacking - K-Fold${NORMAL}"
  echo -e "${MENU}*********************************************${NORMAL}"
  echo -e "${ENTER_LINE}Please enter a menu option and enter or ${RED_TEXT}enter to exit. ${NORMAL}"
  read sub1
  while [ sub1 != '' ]; do
    if [[ $sub1 == "" ]]; then
      exit
    else
      case $sub1 in
      0)
        clear
        pyclean
        option_picked "Return to Menu"
        show_menu
        ;;

      1)
        clear
        pyclean
        option_picked "Create Structure"
        python3 $(pwd)/src/generate_structure.py
        sub_menu
        ;;

      2)
        clear
        pyclean
        option_picked "Preprocessing Dataset"
        python3 $(pwd)/src/data_preprocessing.py
        sub_menu
        ;;

       3) clear;
       pyclean;
       option_picked "Generate Annotations";
       python3 $(pwd)/src/generate_annotations.py
       sub_menu;
       ;;

       10) clear;
       pyclean;
       option_picked "Generate Holdout";
       python3 $(pwd)/src/holdout_validation.py
       sub_menu;
       ;;

       11) clear;
       pyclean;
       option_picked "Extract Features - Holdout";
       bash $(pwd)/scripts/extract_features_holdout.sh
       sub_menu;
       ;;

       12) clear;
       pyclean;
       option_picked "Stacking First Stage - Holdout";
       bash $(pwd)/scripts/first_stage_holdout.sh
       sub_menu;
       ;;

       13) clear;
       pyclean;
       option_picked "Stacking Second Stage - Holdout";
       bash $(pwd)/scripts/second_stage_holdout.sh
       sub_menu;
       ;;

       14) clear;
       pyclean;
       option_picked "Evaluate Stacking - Holdout";
       bash $(pwd)/scripts/evaluation_holdout.sh
       sub_menu;
       ;;

       20) clear;
       pyclean;
       option_picked "Generate K-Fold";
       python3 $(pwd)/src/k_fold_cross_validation.py
       sub_menu;
       ;;

       21) clear;
       pyclean;
       option_picked "Extract Features - K-Fold";
       bash $(pwd)/scripts/extract_features_k_fold.sh
       sub_menu;
       ;;

       22) clear;
       pyclean;
       option_picked "Stacking First Stage - K-Fold";
       bash $(pwd)/scripts/first_stage_k_fold.sh
       sub_menu;
       ;;

       23) clear;
       pyclean;
       option_picked "Stacking Second Stage - K-Fold";
       bash $(pwd)/scripts/second_stage_k_fold.sh
       sub_menu;
       ;;

       24) clear;
       pyclean;
       option_picked "Evaluate Stacking - K-Fold";
       bash $(pwd)/scripts/evaluation_k_fold.sh
       sub_menu;
       ;;

      x)exit;
      ;;

      \n)exit;
      ;;

      *)clear
      option_picked "Pick an option from the menu"
       sub_menu
       ;;
      esac
    fi
  done
}

clear
show_menu
