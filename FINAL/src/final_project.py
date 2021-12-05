#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" Final Project - Naive Bayes classification of movie reviews """
__author__="Oleg Perchyk"

import sys
import csv
from probabilities_model import ProbabilitiesModel

def main():
    if sys.argv[1] == "help":
        show_help()
        exit()
    
    words = get_words_from_argument()

    review_probabilities = process_probabilities(words)
    

def get_words_from_argument():
    words = sys.argv[1:]
    # TODO: attach each word to a probability model  
    return [word.lower() for word in words]

def process_probabilities(words):

    with open("movie") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print(row)
    

help_msg = """
final_project.py <command>

Naive Bayes Movie review classifier based on words used in movie reviews. 

Usage:

final_project.py word1 word2 ...    run text classifier on words provided
final_project.py help               show this help message and exit

"""

def show_help():
    print(help_msg)
    
if __name__ == "__main__":
    main()