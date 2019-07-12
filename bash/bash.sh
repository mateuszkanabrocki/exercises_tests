#!/bin/bash
echo pwd:
pwd
echo ls:
ls
NAME="Mateusz"
#readonly NAME
echo name: $NAME
#NAME="Mat" # error
unset NAME
echo name: $NAME # display nothing
NAME="Me"
readonly NAME
echo current script name: $0
echo first argument: $1
echo list of quoted arguments: $*
echo "list of quoted arguments: $*"
echo list of idividually quoted args: $@
echo "list of idividually quoted args: $@"
echo number of given arguments: $#
NAME="Mee"  # throw an error
echo exit status of the last executed command: $?
echo current shell process: $$
echo process number of the last background command: $! # no command
echo zero command line argument - script name: $0
