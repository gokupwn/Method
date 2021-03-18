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

#-------Usage--------#
function usage (){
  echo -e $usage"$lightGray Nmap Automation Bashscript"$usage
}

#-------Yes Or No-----#
function YesOrNo(){
  echo -en "$error Please Enter yes or no$error "
}

#------Get Input-----#
function getInput (){
    good="0"
    echo -en  "$info Enter The Host To Scan$info "
    read host
    while [[ "1" == "1" ]]; do
      if [[ $host =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
        good="1"
        break
      fi
      echo -en  "$error Please Enter A Valid Ip$error "
      read host
    done

   echo -en "$info Enter Port(s) To Scan$info "
   read ports

   echo -en "$info Services Detection (yes/no)$info "
   read services
   while [[ "$services" != "yes" && "$services" != "no" ]] ; do
     YesOrNo
     read services
   done

   echo -en "$info OS detection (yes/no)$info "
   read OS
   while [[ "$OS" != "yes" && "$OS" != "no" ]] ; do
     YesOrNo
     read OS
   done

   echo -en "$info Display Only Open Port(yes/no)$info "
   read Open
   while [[ "$Open" != "yes" && "$Open" != "no" ]] ; do
     YesOrNo
     read Open
   done

   echo -en "$info Do You Want Save Result In A File(yes/no)$info "
   read output
   while [[ "$output" != "yes" && "$output" != "no" ]] ; do
     YesOrNo
     read output
   done
   if [ "$output" == "yes" ]; then
     echo -en "$info Enter File Name$info "
     read file
  fi

   echo -en "$workFine "
}

#------Launch Scan----#
function scan(){
  cmd="nmap"
  if [ "$services" = "yes" ]; then 
    cmd=$cmd" -sV"
  fi

  if [ "$OS" = "yes" ]; then
    cmd=$cmd" -O"
  fi

  if [ "$Open" = "yes" ]; then
    cmd=$cmd" --open"
  fi

  if [ "$output" = "yes" ]; then
    cmd=$cmd" -oN "$file
  fi

  cmd=$cmd" $host"" -p $ports"
  echo -e  $lightRed $cmd$rest
  cmd=$cmd" -oX $file.xml"
  ( $cmd )
}

#-----start-----#
usage
getInput
scan

echo -e $workFine$blue"Nmap Scan Result saved at $lightYellow$( pwd )$file $rest"$workFine
