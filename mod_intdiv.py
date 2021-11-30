#!/usr/bin/env python3

# Script to display modulo and integer division values for a 9x9 grid

# Constants
PART_SIDE = 3  # start with 9 by 9 grid (16 by 16 also possible in the future)
FULL_SIDE = PART_SIDE ** 2
ROW_SEP = "-"   # separator symbol between rows in grid
COL_SEP = "|"   # separator symbol between columns in grid
SPACE = " "     # have space on either side of value to make reading grid easier

# Variables

# Functions
def greet_user():    # Greet user
    print("Welcome to my modulo and integer division calculation application", end="")
    print("for {} by {} puzzle".format(FULL_SIDE, FULL_SIDE))

def create_grid(FULL_SIDE):   # Initialize list of values from 0 to 80
    grid_list = []        
    for count in range(FULL_SIDE ** 2):
        grid_list.append(count)
    return grid_list

def show_grid(grid, FULL_SIDE):    # display list values in grid format without lines 
    print()  # blank line
    for row in range(FULL_SIDE):
        for column in range(FULL_SIDE):
            print("{:2d}".format(grid[row * FULL_SIDE + column]),  sep="", end="")
        print() # line break at end of line

def create_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP):  # display with both horizontal and vertical lines "+-+-+-...-+" format
    for j in range(FULL_SIDE):
        print("+", ROW_SEP, ROW_SEP, ROW_SEP, ROW_SEP, sep="", end="") 
    print("+")   # Need new line at end of string of symbols

def show_grid_with_lines(grid, FULL_SIDE, ROW_SEP, COL_SEP):    # Add separator characters between rows and columns
    print()  # blank line
    for row in range(FULL_SIDE):
        create_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP)
        for column in range(FULL_SIDE):
            print("{} {:2d} ".format(COL_SEP, grid[row * FULL_SIDE + column]),  sep="", end="")
        print(COL_SEP) # Add final column separator and default line break at end of line



# Main code
greet_user() 

grid = create_grid(FULL_SIDE)
show_grid(grid, FULL_SIDE)    


show_grid_with_lines(grid, FULL_SIDE, ROW_SEP, COL_SEP)

print()
print("Start solving puzzle now.")


for j in range(len(grid)):
    pass

print(grid)
show_grid_with_lines(grid, FULL_SIDE, ROW_SEP, COL_SEP)    # Add separator characters between rows and columns
