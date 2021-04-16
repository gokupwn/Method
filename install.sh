#!/bin/bash


#-----Colors--------#
lightRed='\033[91m'
lightYellow='\033[93m'
blue='\033[34m'
lightGray='\033[37m'
blink='\033[90m'
lightBlue='\033[94m'
lightGreen='\033[92m'
rest='\033[0m'

#-------Symbols------#
error=$lightRed"[-]"$rest
info=$lightGreen"[?]"$rest
workFine=$blue"[~]"$rest


if [[ $EUID -ne 0 ]]; then
  echo -e "$error You don't say the magic word sudo $error"
  echo -e "$info Please run as root $info"
  exit 1
fi

clear
echo -e "$workFine Installing ..."
python3 -m venv venv3
source venv3/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install http.client
python3 -m pip install re
python3 -m pip install argparse
python3 -m pip install readline
echo -e "$workFine Done $workFine"
