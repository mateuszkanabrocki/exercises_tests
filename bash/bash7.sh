#!/bin/sh

Bonjour () {
    echo "Bonjour $1 $2!"
    echo "Comment ca va?"
    return 11
}

Hello () {
    echo "Hello $1 $2"
    echo "How you doin?!"
    Bonjour Mateusz Kanabrocki
    ret=$?
    echo $ret
    return 10
}

Hello Mateusz Kanabrocki
ret=$?
echo "Function returned $ret."

