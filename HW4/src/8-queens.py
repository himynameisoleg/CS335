#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" Beyond Search Homework """
__author__="Oleg Perchyk"

import random
import sys

def generate_random_board():
    return[random.randrange(0, 8, 1) for i in range(8)]


def hill_climbing_random(board, MAX_COST):
    random_neighbor = generate_random_board()
    best_board = hill_climbing(board)
    cost = 0
    solved = False
    
    while cost < MAX_COST or solved:
        random = hill_climbing(random_neighbor)
        if number_attacking(random_neighbor) < number_attacking(best_board):
            best_board = random
        random_neighbor = generate_random_board()
        cost += 1
        if number_attacking(best_board) == 0:
            solved += 1

    return { 
        "cost": cost,
        "solved": solved 
        }


def hill_climbing(board):
    current = board

    while True:    
        neighbor = get_neighbor(board)
        if number_attacking(neighbor) >= number_attacking(current):
            return current
        
        current = neighbor


def get_neighbor(board):
    neighbor = board
    neighbor[random.randint(0, 7)] = random.randint(0, 7)
    return neighbor


def number_attacking(board):
    attacking = 0

    # horizontally
    for col in range(len(board)):
        queen_pos = board[col]
        for row in range(col + 1, len(board)):
            if board[row] == queen_pos:
                attacking += 1
    
    # vertically: based on hw specs we should not see any vertical attacks since we use 1D list representation

    # diagonally down
    for col in range(len(board)):
        queen_pos = board[col]
        
        for row in range(col + 1, len(board)):
            check_pos = board[row]
            if queen_pos + (row - col) == check_pos:
                attacking += 1
            if queen_pos - (row - col) == check_pos:
                attacking += 1


    return attacking


def main():
    num_puzzles = 1 #int(sys.argv[1])

    MAX_COST = 9999

    hc_cost = 0
    hc_solved = 0

    for i in range(num_puzzles):
        # board = generate_random_board()
        board = [3, 4, 1, 6, 7, 2, 5, 4]
        hc = hill_climbing_random(board, MAX_COST)
        hc_cost = hc["cost"]
        if hc["solved"]: hc_solved += 1

    print(f"Hill-climbing: {hc_solved / num_puzzles}% solved, average cost: {hc_cost / num_puzzles}")


if __name__ == "__main__":
    main()