#! /usr/bin/env python

# a program to count the number of vowels in a sentence.
# Painfully (and badly) written in python2.

import sys


def count_vowels():
    result = raw_input('Enter your phrase: ')
    if not isinstance(result, str):
        traceback = sys.exc_info()[2]
        raise ValueError, "Somehow you didn't enter a string. Please try again.", traceback

    try:
        result = int(result)
        print "That's not a string, that's a number. >_<"
        sys.exit()
    except ValueError, e:
        # we want this to trigger
        pass

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_dict = dict()

    for char in result:
        if char in vowels:
            vdc = int(vowel_dict.get(char, 0))
            vowel_dict[char] = vdc + 1

    print "The total is: "

    for v, c in vowel_dict.iteritems():
        print "{}: {} instances".format(v, c)


if __name__ == "__main__":
    count_vowels()
