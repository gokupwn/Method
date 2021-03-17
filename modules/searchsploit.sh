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
usage=$lightYellow"[!]"$rest
workFine=$blue"[+]"$rest

echo -e $usage"Searchsploit Automation Bashscript"$usage
echo -en $info"Enter The Path Of Xml File"$info
read file

while [[ '1' == '1' ]] ; do
  if [[ $file =~ \.(xml) ]] ; then
    break
  fi
  echo -en $error'Please Enter A .xml File'$error
  read file
done

xmlFile=$( pwd )" /"$file

searchsploit -v --nmap $file --www 
