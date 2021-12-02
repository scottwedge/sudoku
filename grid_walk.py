#!/usr/bin/env python3

# Script to create list of internal grid spots

# Constants
PART_SIDE = 3  # start with 9 by 9 grid (16 by 16 also possible in the future)
FULL_SIDE = PART_SIDE ** 2
ROW_SEP = "-"   # separator symbol between rows in grid
COL_SEP = "|"   # separator symbol between columns in grid
SPACE = " "     # have space on either side of value to make reading grid easier

# Variables

# Functions

def create_puzzle():
    puzzle = []
    for j in range(81):
        puzzle.append(j)
    return puzzle


def show_grid(puzzle, FULL_SIDE):    # format known puzzle values into grid to be displayed to user
    print()  # blank line
    for row in range(FULL_SIDE):
        for column in range(FULL_SIDE):
            print(puzzle[row * FULL_SIDE + column], " ",  sep="", end="")
        print() # line break at end of line

def create_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP):  # "+-+-+-...-+" format
    for j in range(FULL_SIDE):
        print("+", ROW_SEP, ROW_SEP, ROW_SEP, ROW_SEP, sep="", end="") 
    print("+")   # Need new line at end of string of symbols

def show_grid_lines(puzzle, FULL_SIDE, ROW_SEP, COL_SEP):    # Add separator characters between rows and columns
    print()  # blank line
    for row in range(FULL_SIDE):
        create_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP)
        for column in range(FULL_SIDE):
            print("{}{}{:2d}{}".format(COL_SEP, SPACE, puzzle[row * FULL_SIDE + column], SPACE),  sep="", end="")
        print(COL_SEP) # Add final column separator and default line break at end of line

def all_values(FULL_SIDE):
    values = []
    for count in range(1, FULL_SIDE + 1):
        values.append([count])    # Add value as single list so can easily check if [k] in [j]
    return values

def setup_possibles_list(puzzle, values):
    possibles_list = []   # initialize empty list

    for j in range(len(puzzle)):
        if puzzle[j] == 0:
            possibles_list.append(all_values(FULL_SIDE))          # all values possible for blank field
        else:
            possibles_list.append([puzzle[j]])       # value is already known so use it as a list of one value
    return possibles_list


def create_list_of_internal_grids(PART_SIDE):  # Create list of internal grid lists for any N x N grid
    list_of_internal_grids = []
    for s in range(PART_SIDE):
        for n in range(PART_SIDE):   # move to next grid
            internal_grid = []    # Initialize new list
            for v in range(PART_SIDE):  # Move vertically within grid 
                for h in range(PART_SIDE): # Move horizontally within grid
                    spot = v * PART_SIDE ** 2 + h
                    spot = spot + n * PART_SIDE
                    spot = spot + s * PART_SIDE ** 3
                    internal_grid.append(spot)
            list_of_internal_grids.append(internal_grid)        
    return list_of_internal_grids

# Main code
# Create list of sets of inner grids based on PART_SIDE
list_of_internal_grids = create_list_of_internal_grids(PART_SIDE)

print("This the list of internal grid spots created by this program: ")
for grid in list_of_internal_grids:
    print(grid)

puzzle = create_puzzle()

print()

show_grid_lines(puzzle, FULL_SIDE, ROW_SEP, COL_SEP)
