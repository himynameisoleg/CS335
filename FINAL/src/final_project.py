#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" Final Project -  """
__author__="Oleg Perchyk"

import sys

def main():
    if sys.argv[1] == "help":
        show_help()
        exit()

    


def show_help():
    print(
"""
usage: final_project.py [] []

This is a short description of the program. 

positional arguments:
help                Show this help message and exit

optional arguments:

""")
    
if __name__ == "__main__":
    main()