#!/usr/bin/env python3.6
from sys import argv


def count_bits(number):
    # changing int into bin string (e.g 0b111)
    binary = bin(number)
    count = 0
    rev_binary = ''
    # reversing a string
    for i in binary:
        rev_binary = i + rev_binary
    for bit in rev_binary:
        if bit != 'b' and bit == '1':
            count += 1
    return count


def main():
    print(count_bits(int(argv[1])))


if __name__ == '__main__':
    main()


# The better way:

# def count_bits(x)
#     num_bits = 0
#     while x:
#         num_bits += x & 1
#         x >>= 1
#     return num_bits
