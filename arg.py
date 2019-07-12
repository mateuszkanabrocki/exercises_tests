#!/usr/bin/env python3.7


def add(*arg, x=1):
    print(f"x: {x}, arg: {arg}")


add({'k': 2, 'g': 3, 'h': 6, 'i': 8}, 4, x=2)


def count(*numbers):
    count = 0
    for number in numbers:
        count += number
    return count


print(count(1, 2, 6, 10, 11))


def append_list(list):
    a = list
    return a.append('!!!')


list1 = [1, 2, 3]
print(append_list(list1))  # None
print(list1)  # list1 is changed