#!/usr/bin/env python3.7
from enum import Enum, IntEnum


enum = Enum('Menu', 'Pizza Lasagna Spaghetti')
enum3 = IntEnum('Menu', 'Pizza Lasagna Spaghetti')
choice = input("""
        Co zjesz?:
        1. Pizza
        2. Lasagna
        3. Spaghetti
        """)

if int(choice) == enum.Pizza.value:
    print("Pizza time!")

if int(choice) == enum3.Pizza:
    print("Pizza time!")