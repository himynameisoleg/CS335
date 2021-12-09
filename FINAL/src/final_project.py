#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" Final Project - Naive Bayes classification of movie reviews """
__author__="Oleg Perchyk"

import sys
import csv
import re

class WordProbabilitiesModel:
    word = ""
    positive = 0
    negative = 0
    total = 0

    def __init__(self, word):
        self.word = word

def main():
    if sys.argv[1] == 'help':
        show_help()
        exit()
    
    # input splitting phase
    print('Parsing keywords from argument.')
    words_metadata = get_words_from_argument()

    # data processing phase
    print(f'Processing movie data for keywords: {[item.word for item in words_metadata]}...\n\n')
    processed_data = process_movie_data(words_metadata)

    # data normalizing phase
    ALPHA = 1
    normalized_data = normalize_data(processed_data, ALPHA)

    # analysis phase 
    results = analyze_probabilities(normalized_data)
    print_results(results)

def get_words_from_argument():
    args = sys.argv[1:]
    words = []
    for arg in args:
        words.append(WordProbabilitiesModel(arg.lower()))
    
    return words

def process_movie_data(words_metadata):

    with open("movie_data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        result = {
            "total_positive": 0,
            "total_negative": 0,
            "total_words": 0,
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

        result["total_words"] = result["total_positive"] + result["total_negative"]

    return result

def normalize_data(movie_data, ALPHA):
    has_zero_value = False

    for word in movie_data["words_metadata"]:
        if word.positive == 0 or word.negative == 0:
            has_zero_value = True

    if has_zero_value:
        for word in movie_data["words_metadata"]:
            word.positive += ALPHA
            movie_data["total_positive"] += ALPHA

            word.negative += ALPHA
            movie_data["total_negative"] += ALPHA

            word.total += (ALPHA * 2)

    movie_data["total_words"] = movie_data["total_positive"] + movie_data["total_negative"]

    return movie_data

def analyze_probabilities(movie_data):
    classification_positive = movie_data["total_positive"] / movie_data["total_words"]
    classification_negative = movie_data["total_negative"] / movie_data["total_words"]

    for word in movie_data["words_metadata"]:
        prob_word_positive = word.positive / word.total
        prob_word_negative = word.negative / word.total

        classification_positive = classification_positive * prob_word_positive
        classification_negative = classification_negative * prob_word_negative

    return {
        "movie_data": movie_data, 
        "classification_positive": classification_positive,
        "classification_negative": classification_negative
    }

def print_results(results):
    classification = 'POSITIVE' if results["classification_positive"] > results["classification_negative"] else 'NEGATIVE'

    print(f'''Naive Bayes calculation results for words {[item.word for item in results["movie_data"]["words_metadata"]]}:
Positive = {results["classification_positive"]}
Negative = {results["classification_negative"]}
This combination of words is more likely to yeild a {classification} movie review. 
''')

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