"""
Author: Edgar Argueta
FileName: main.py

Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.
"""
import sys


def main():
    string1 = sys.argv[1]  # The first string to compare
    string2 = sys.argv[2]  # The second string that we have to map to
    print(string1)
    print(string2)


if __name__ == '__main__':
    main()