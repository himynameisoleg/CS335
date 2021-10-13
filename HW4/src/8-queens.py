#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" Beyond Search Homework """
__author__="Oleg Perchyk"

import random
import sys

def generate_random_board():
    return[random.randrange(0, 8, 1) for i in range(8)]


def hill_climbing_random(board, MAX_COST):
    best_board = list(board)
    current_board = list(board)
    cost = 0
    solved = False
    
    while (solved == False and  cost < MAX_COST):
        neighbor = list(get_neighbor(current_board))
        cost += 1

        score_current = number_attacking(best_board)
        score_neighbor = number_attacking(neighbor)

        if number_attacking(neighbor) < number_attacking(best_board):
            best_board = neighbor
            current_board = neighbor

        if  score_current == 0 or score_neighbor == 0:
            solved = True
            
    # print(f'board returned: {best_board}')

    return { 
        "cost": cost,
        "solved": solved 
        }


def hill_climbing(board):
    current = board

    while True:    
        neighbor = list(get_neighbor(board))
        if number_attacking(neighbor) >= number_attacking(current):
            return current
        
        current = neighbor


def get_neighbor(board):
    neighbor = list.copy(board)
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
    num_puzzles = 350 #int(sys.argv[1])

    MAX_COST = 100

    hc_cost = 0
    hc_solved = 0

    for i in range(num_puzzles):
        board = generate_random_board()
        # board = [1, 3, 0, 2]
        hc = hill_climbing_random(board, MAX_COST)
        hc_cost += hc["cost"]
        print(f'run# {i}: cost: {hc["cost"]} | solved: {hc["solved"]}')
        if hc["solved"]: hc_solved += 1

    print(f"Hill-climbing: {hc_solved / num_puzzles}% solved, average cost: {hc_cost / num_puzzles}")


if __name__ == "__main__":
    main()