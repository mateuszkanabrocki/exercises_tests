#!/bin/sh

echo "This script is called: $0"
var1=$1
var2=$2

until [ "$var1" -lt 20]
do
    echo "$var1"
    while [ "$var2" -le 10 ]
    do
        echo "$var2"
        if [ $var1 -eq 13 -a $var2 -ge 6 ]
        then
            echo "I'm breaking out!"
            break 2
        elif [ $var1 -eq 12 -a $var2 -ge 6 ]
        then
            echo "Almost!"
        else
            echo "Not yet."
        fi
        var1=`expr $var1 + 1`
        var2=`expr $var2 + 1`
    done
done
