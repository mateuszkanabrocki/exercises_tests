#!/bin/sh

NUMBERS="1 2 3 4 5 6 7 8 9 10"

for NUM in $NUMBERS
do
    R=`expr $NUM % 2`
    if [ $R -eq 0 ]
    then
        echo "Number "$NUM" is even."
        continue
    fi
    echo "Number "$NUM" is odd."
done
