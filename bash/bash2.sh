#!/bin/sh

val=`expr 2 + 2`
echo "Total value : $val"

a=10
b=4
c=`expr $a \* $b`
echo $c
e=1

if [ $a -ne $b -a $b -eq 4 ]
then
    echo "It's not equal!"
fi

# e=[ $a -eq $b ]