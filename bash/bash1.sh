#!/bin/bash

for TOKEN in $*  # can also use $@ instead - same result
do
    echo $TOKEN
done


NAME=("Mat" "Tad" "Bad")

echo first element: ${NAME[1]}

NAME[0]="Zara"
NAME[1]="Qadir"
echo "First Index: ${NAME[0]}"
echo "Second Index: ${NAME[1]}"
echo all elements: ${NAME[*]}
echo all elements: ${NAME[@]}
