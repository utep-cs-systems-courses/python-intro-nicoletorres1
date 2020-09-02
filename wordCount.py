#! /usr/bin/env python3
import re
import os
import sys
#import Counter

#import libraries
#re is regular expressions
#os functions for interacting w operating systems
#system to access functions and lists

# contains the command-line arguments passed
inputFname = sys.argv[1]
outputFname = sys.argv[2]

# how to read a file
# takes as input the name of an input file and output file
# excluding white space and punctuation and ignores upper/lower case
file = open(inputFname, "r")
x = file.readlines()
# make a new list of words
biggerlist = []
for word in x:
    word = word.lower()
    word = word.replace("?", "")
    word = word.replace(".", "")
    word = word.replace(":", "")
    word = word.replace(",", "")
    word = word.replace(";", "")
    word = word.replace("&", "")
    word = word.replace("-", " ")
    word = word.replace("'", " ")
    biggerlist.append(word.split())
#print(biggerlist)

# initialize dictionary value & key
dictionary = {}

# count. keeps track of the total the number of times each word occurs in the text file
# if the word appears more than once increment by 1
for smallerlist in biggerlist:
    for word in smallerlist:
        # add the word to dictionary with count 1
        # or increment the word already in dictionary by 1
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1


# print out to the output file (overwriting if it exists) the list of words
# sorted in descending order with their respective totals separated by a space, one word per line
print(dictionary)

with open(outputFname, 'w') as outputFile:
    for i in sorted(dictionary):
        outputFile.write(i + " " + str(dictionary[i]) + "\n")




#def __main__():
    #pass