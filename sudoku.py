#!/usr/bin/env python3

# Script to solve simple Sudoku puzzle

# Variables

# Functions
def greet_user():    # Greet user
    print("Welcome to my Sudoku solving application")

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

# Main code
greet_user() 
puzzle = get_initial_puzzle()
print(puzzle)
