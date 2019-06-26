#!/usr/bin/env python3.6
import sys

# cat text.txt | ./std.py >> output.txt  2> errors.txt


def main():
    stdinput = sys.stdin.readlines()
    sys.stderr.write("No errors. It's wooorking ;D")
    sys.stdout.write(f"I got this from the stdin: {stdinput}")


if __name__ == '__main__':
    main()
