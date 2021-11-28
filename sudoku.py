#!/usr/bin/env python3

# Script to solve simple Sudoku puzzle

# Constants
PART_SIDE = 3  # start with 9 by 9 grid (16 by 16 also possible in the future)
FULL_SIDE = PART_SIDE ** 2
ROW_SEP = "-"   # separator symbol between rows in grid
COL_SEP = "|"   # separator symbol between columns in grid
SPACE = " "     # have space on either side of value to make reading grid easier

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

def create_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP):  # "+-+-+-...-+" format
    for j in range(FULL_SIDE):
        print("+", ROW_SEP, ROW_SEP, ROW_SEP, sep="", end="") 
    print("+")   # Need new line at end of string of symbols

def show_grid_lines(puzzle, FULL_SIDE, ROW_SEP, COL_SEP):    # Add separator characters between rows and columns
    print()  # blank line
    for row in range(FULL_SIDE):
#        create_row_separating_line(FULL_SIDE, ROW_SEP, COL_SEP)
        create_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP)
        for column in range(FULL_SIDE):
            print(COL_SEP, SPACE, puzzle[row * FULL_SIDE + column], SPACE,  sep="", end="")
        print(COL_SEP) # Add final column separator and default line break at end of line

def all_values(FULL_SIDE):
    values = []
    for j in range(1, FULL_SIDE + 1):
        values.append(j)
    return values

def setup_possibles_list(puzzle, values):
    values = all_values(FULL_SIDE)
    possibles_list = []   # initialize empty list

    for j in range(len(puzzle)):
#DEBUG        print("Index j is: {}".format(j))
        if puzzle[j] == 0:
#DEBUG            print("puzzle[{}] is 0.".format(j))
            possibles_list.append(values)          # all values possible for blank field
        else:
#DEBUG            print("puzzle[{}] is not 0 it is {}.".format(j, puzzle[j]))
            possibles_list.append(puzzle[j])       # value is already known so use it
    return possibles_list


# Main code
greet_user() 

puzzle = get_initial_puzzle()

print()
print("These are the initial puzzle values:", puzzle)  # Show initial puzzle data in long list format

show_grid(puzzle, FULL_SIDE) # Show puzzle values in more readable grid format

show_grid_lines(puzzle, FULL_SIDE, ROW_SEP, COL_SEP)

#DEBUG print()
#DEBUG print("All possible values for a spot are: {}".format(all_values(FULL_SIDE)))

print()
print("Start solving puzzle now.")

loop = 0
print()
print ("Loop count= {}".format(loop))

values = all_values(FULL_SIDE)

possibles_list = setup_possibles_list(puzzle, values)
print(possibles_list)

