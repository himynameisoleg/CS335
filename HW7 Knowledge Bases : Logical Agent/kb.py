#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" Homework on Logical Agents and Knowledge Bases """
__author__="Oleg Perchyk"

import sys

def main():
    kb = sys.argv[1]
    # kb = "prep.kb"

    lines = open(kb).readlines()

    for line in lines:
        line = line.strip()
        expression = line.split(',')[0]
        models = line.split(',')[1:]

        expression = assign_truth_values(models, expression)
        expression = process_expression(expression)

        print(eval(expression))

def assign_truth_values(models, expression):
    for model in models:
        equality = {
            'key': model.split('=')[0],
            'val': True if model.split('=')[1] == 'T' else False
        }

        expression = expression.replace(equality['key'], str(equality['val']))

    return expression

def process_expression(expression):
    new_exp = expression.replace('V', 'or').replace('^', 'and').replace('~', 'not ')
    return new_exp

if __name__ == "__main__":
    main()