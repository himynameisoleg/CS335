#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" Final Project - Naive Bayes classification of movie reviews """
__author__="Oleg Perchyk"

import sys
import csv
import re
from word_probabilities_model import WordProbabilitiesModel


def main():
    if sys.argv[1] == 'help':
        show_help()
        exit()
    
    # input splitting phase
    print('Parsing keywords from argument.')
    words_metadata = get_words_from_argument()

    # data processing phase
    print(f'Processing movie data for keywords: {[item.word for item in words_metadata]}.')
    processed_data = process_movie_data(words_metadata)

    # data normalizing phase
    ALPHA = 1
    normalized_data = normalize_data(processed_data, ALPHA)

    # analysis phase 
    print('Analyzing probabilities.')
    result = analyze_probabilities(normalized_data)

    print(f'Results: {result}')


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

        result = {
            "total_positive": 0,
            "total_negative": 0,
            "words_metadata": words_metadata
        }

        for row in csv_reader:
            if row[1] == 'positive': result["total_positive"] += 1
            elif row[1] == 'negative': result["total_negative"] += 1

            for i in range(len(words_metadata)):
                if row[0].lower().find(words_metadata[i].word) != -1:
                    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(words_metadata[i].word), row[0].lower()))

                    result["words_metadata"][i].total += count

                    if row[1] == 'positive': result["words_metadata"][i].positive += count
                    elif row[1] == 'negative': result["words_metadata"][i].negative += count


            line_count += 1
            # TODO: remove perf limiter
            if line_count == 1000: 
                return result
    
    return result

def normalize_data(movie_data, ALPHA):
    has_zero_value = False

    for word in movie_data["words_metadata"]:
        if word.positive == 0 or word.negative == 0:
            has_zero_value = True

    if has_zero_value:
        for word in movie_data["words_metadata"]:
            word.positive += ALPHA
            word.negative += ALPHA
            word.total += (ALPHA * 2)

    return movie_data

def analyze_probabilities(movie_data):
    results = {
        "probability_positive": 0.00,
        "probability_negative": 0.00
    }

    return results


help_msg = """
final_project.py <command>

Naive Bayes Movie Review Classifier based on keywords used in movie reviews. 

Usage:

final_project.py word1 word2 ...    run text classifier on words provided
final_project.py help               show this help message and exit

"""

def show_help():
    print(help_msg)
  

if __name__ == "__main__":
    main()