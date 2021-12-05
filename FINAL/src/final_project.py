#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" Final Project - Naive Bayes classification of movie reviews """
__author__="Oleg Perchyk"

import sys
import csv
import re
from word_probabilities_model import WordProbabilitiesModel

def main():
    if sys.argv[1] == "help":
        show_help()
        exit()
    
    words_metadata = get_words_from_argument()

    processed_words_metadata = process_movie_data(words_metadata)
    

def get_words_from_argument():
    args = sys.argv[1:]
    words = []
    for arg in args:
        words.append(WordProbabilitiesModel(arg.lower()))
    
    return words
        

def process_movie_data(words_metadata):

    with open("movie_data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            for i in range(len(words_metadata)):
                if row[0].lower().find(words_metadata[i].word) != -1:
                    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(words_metadata[i].word), row[0].lower()))
                    
                    words_metadata[i].total += count

                    if row[1] == 'positive': words_metadata[i].positive += count
                    elif row[1] == 'negative': words_metadata[i].negative += count


            line_count += 1
            # TODO: remove perf limiter
            if line_count == 1000: 
                return words_metadata
    
    return words_metadata
    

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