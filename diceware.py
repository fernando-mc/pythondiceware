#!/usr/bin/env python

import argparse

valid_numbers = set("123456")

def test_set(input):
    return set(input) <= valid_numbers

parser = argparse.ArgumentParser()

parser.add_argument("-wc", "--wordcount", 
                    help = "The number of words for your diceware password")

parser.add_argument("-dr", "--dicerolls",
                    help = "The dicerolls for your diceware password")

args = parser.parse_args()

print "Use -wc to set number of diceware words"
print "Use -dr to input your dicerolls (5 rolls per word)"

number_of_words = args.wordcount

dicerolls = args.dicerolls

#Check for valid inputs
if(test_set(dicerolls)):
    print "Looks like your inputs are numbers 1-6!"
else:
    print "Please make sure your inputs are numbers 1-6!"

#Check for length multiple 5
if(len(dicerolls) % 5 == 0):
    print "Awesome, your input is valid length (a multiple of five)"
else:
    print "Please check your input is a multiple of 5 - generating passwords"
