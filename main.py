"""
Author: Edgar Argueta
FileName: main.py

Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.
"""
import sys


def main():
    if len(sys.argv) < 2:
        raise Exception("Two strings are needed to run this program")
    else:
        string1 = sys.argv[1]  # The first string to compare
        string2 = sys.argv[2]  # The second string that we have to map to
        dictionary = dict()  # The map to store which character from string1 is mapped to in string2
        condition = False  # Boolean to keep track if the string1 can be 1-to-1 mapped.
        for i in range(len (string1)):
            if string1[i] in dictionary:  # Check if character in dictionary
                condition = True
                break
            dictionary[string1[i]] = string2[i]  # If not, map the characters
        if condition:
            print("false")
        else:
            print("true")


if __name__ == '__main__':
    main()
