#!/usr/bin/env python3


def count_bits(number):
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count


x = 10
print(count_bits(x))
