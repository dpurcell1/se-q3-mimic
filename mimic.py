#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = """Darrell Purcell with help from
https://stackoverflow.com/
questions/24928585/python-for-loop-without-index-and-item"""


import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """

    mimic_dict = {}
    start = True
    with open(filename, 'r') as f:
        for line in f:
            i = 0
            word_list = line.split()
            for word in word_list:
                if start:
                    mimic_dict[''] = [word_list[i]]
                    mimic_dict[word] = [word_list[i + 1]]
                    i += 1
                    start = False
                elif word not in mimic_dict.keys() and i < len(word_list) - 1:
                    mimic_dict[word] = [word_list[i + 1]]
                    i += 1
                elif i < len(word_list) - 1:
                    mimic_dict[word] += [word_list[i + 1]]
                    i += 1
    return mimic_dict


def print_mimic_random(mimic_dict, num_words):
    """Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
        - Use a start_word of '' (empty string)
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    """
    start_word = ''
    start_dict_word = mimic_dict[start_word][0]
    print(start_dict_word, end=' ')
    next_list = mimic_dict[start_dict_word]
    rand = random.randrange(0, len(next_list))
    next_list_word = next_list[rand]
    print(next_list_word, end=' ')
    for __ in range(0, num_words - 2):
        next_list = mimic_dict.get(next_list_word, start_dict_word)
        rand = random.randrange(0, len(next_list))
        next_list_word = next_list[rand]
        print(next_list_word, end=' ')


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
