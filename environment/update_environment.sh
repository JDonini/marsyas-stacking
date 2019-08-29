#!/bin/bash

progress(){
  echo -n "$0: Please wait ."
  while true
  do
    sleep 5
    echo -n "."
  done
}

dobackup(){
    # put backup commands here
    conda update -n keras --all
    conda env export > utils/environment.yml    
}

progress &

MYSELF=$!

dobackup

kill $MYSELF >/dev/null 2>&1

echo -n "... done."
echo
