#!/usr/bin/env python3
import webbrowser
from time import sleep

for i in range(10):
    webbrowser.open('http://google.pl')
    print('!')
    sleep(20)
