#!/usr/bin/env python3

# Script to solve simple Sudoku puzzle

# Constants
PART_SIDE = 3  # start with 9 by 9 grid (16 by 16 also possible in the future)
FULL_SIDE = PART_SIDE ** 2

# Variables

# Functions
def greet_user():    # Greet user
    print("Welcome to my Sudoku solving application")
    print("for {} by {} puzzle".format(FULL_SIDE, FULL_SIDE))

def get_initial_puzzle(): # return data file as list
                          # cannot have blank in list so use "0" for blanks
    initial_puzzle = [7,4,5,0,9,0,0,0,0,\
                      0,3,2,1,5,0,0,4,6,\
                      0,0,0,2,8,0,5,0,3,\
                      2,0,0,0,0,0,0,6,0,\
                      9,8,0,6,0,0,3,5,1,\
                      0,0,0,5,4,0,2,0,7,\
                      3,0,8,0,0,0,0,0,2,\
                      0,2,0,7,6,0,0,1,0,\
                      0,6,0,9,0,8,0,3,4]
    return initial_puzzle

def show_grid(puzzle, FULL_SIDE):    # format known puzzle values into grid to be displayed to user
    print()  # blank line
    for row in range(FULL_SIDE):
        for column in range(FULL_SIDE):
            print(puzzle[row * FULL_SIDE + column], " ",  sep="", end="")
        print() # line break at end of line

# Main code
greet_user() 
puzzle = get_initial_puzzle()
print(puzzle)
show_grid(puzzle, FULL_SIDE)
