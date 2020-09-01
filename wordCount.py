#! /usr/bin/env python3

#import libraries
#re is regular expressions
#os functions for interacting w operating systems
#system to access functions and lists

import re
import os
import sys

#contains the command-line arguments passed
inputFname = sys.argv[1]
outputFname = sys.argv[2]

    # how to read a file
    # takes as input the name of an input file and output file
    file = open(inputFname, "r")
    x = file.readline()
    print(x)

# initialize dictionary
    dictionary = {}

# count. keeps track of the total the number of times each word occurs in the text file
    for word in x:
        if word not in dictionary:
            dictionary[word] = 0
        dictionary[word] += 1

# excluding white space and punctuation and ignores upper/lower case




#print out to the output file (overwriting if it exists) the list of words

#sorted in descending order with their respective totals separated by a space, one word per line

def main():
