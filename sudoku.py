#!/usr/bin/env python3

# Script to solve simple Sudoku puzzle

# Constants
PART_SIDE = 3  # start with 9 by 9 grid (16 by 16 also possible in the future)
FULL_SIDE = PART_SIDE ** 2
ROW_SEP = "-"   # separator symbol between rows in grid
COL_SEP = "|"   # separator symbol between columns in grid
SPACE = " "     # have space on either side of value to make reading grid easier
MAX_LOOP = 5   # Maximum number of loop before program ends

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
        create_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP)
        for column in range(FULL_SIDE):
            print(COL_SEP, SPACE, puzzle[row * FULL_SIDE + column], SPACE,  sep="", end="")
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
    for s in range(PART_SIDE): # Move down vertically between top left spot in column of left-most internal grids
                               # So in a 9x9 grid (spots 0-80) move between spots 0, 27 and 54
        for n in range(PART_SIDE):   # move to next grid to the right 
            internal_grid = []    # Initialize new list
            for v in range(PART_SIDE):  # Move vertically within internal grid 
                for h in range(PART_SIDE): # Move horizontally within internal grid
                    spot = v * PART_SIDE ** 2 + h
                    spot = spot + n * PART_SIDE
                    spot = spot + s * PART_SIDE ** 3
                    internal_grid.append(spot)
            list_of_internal_grids.append(internal_grid)        
    return list_of_internal_grids

def resolve_column(possibles_list, j, FULL_SIDE):
    col = j % FULL_SIDE  # determine which column spot is in
    
    # Find all other spots in that column (col) with only a single value 
    # and remove from current spot if it is in list of possible values
    for k in range(len(possibles_list)):
        if j % FULL_SIDE != k % FULL_SIDE:
            continue    # skip this value since in different column
        # continue comparison since same column
        if j == k:
            continue    # skip since cannot compare self to self 
                
        if len(possibles_list[k]) == 1:
            if possibles_list[k] in possibles_list[j]:    #Must convert to integer else not "in" list
                print("Single {} in same column {} so remove it".format(possibles_list[k], possibles_list[j]), end ="")
                possibles_list[j].remove(possibles_list[k])  # remove value from list
                print(" leaves {}".format(possibles_list[j]))
                continue
    return possibles_list
    
def resolve_row(possibles_list, j, FULL_SIDE):
    # Find all single value spots in each row and remove them from other possible spots in same row
    # Determine row number using integer division (//)
    for k in range(len(possibles_list)):
        if j // FULL_SIDE != k // FULL_SIDE:
            continue   # return to top of inner ('k') loop
#DEBUG        print("Row {} matches row {}".format(j//FULL_SIDE, k//FULL_SIDE))    #DEBUG
        if j == k:
#DEBUG            print("  Skip since cannot match to self")
            continue    # skip since cannot compare self to self 
        if len(possibles_list[k]) == 1:    # single value in spot
#DEBUG            print("Single value {} in spot {} ....".format(possibles_list[k], k), end = "") 
            if possibles_list[k] in possibles_list[j]:
                print("Single {} is in same row as {} ".format(possibles_list[k], possibles_list[j]), end="")
                possibles_list[j].remove(possibles_list[k])
                print(" leaves {}".format(possibles_list[j]))
    return possibles_list
    
def resolve_inner_grid(possibles_list, j, PART_SIDE):
    # Create list of sets of inner grids based on PART_SIDE
    list_of_internal_grids = create_list_of_internal_grids(PART_SIDE)  # Create list of internal grid lists for any size grid

    for k in range(len(possibles_list)):
    # first verify that both spots are located in the same inner grid 
    # then verify that this is not the exact same spot as the outer loop
    # then verify that spot only has a single value
    # then if single value inside outer list, remove it
        for list in list_of_internal_grids:
            if j in list and k in list:
#DEBUG                print("Both {} and {} in same internal grid {}".format(j, k, list))  #DEBUG
                if j == k:
                    continue  # Cannot delete self from self
                if len(possibles_list[k]) == 1:
                    if possibles_list[k] in possibles_list[j]:
                        print("Remove {} from {} in internal grid".format(possibles_list[k], possibles_list[j]), end = "")
                        possibles_list[j].remove(possibles_list[k])
                        print(" leaves {}".format(possibles_list[j]))
    return possibles_list

# Main code
greet_user() 
        
puzzle = get_initial_puzzle()

print()
print("These are the initial puzzle values:", puzzle)  # Show initial puzzle data in long list format

show_grid(puzzle, FULL_SIDE) # Show puzzle values in more readable grid format

show_grid_lines(puzzle, FULL_SIDE, ROW_SEP, COL_SEP)

print()
print("Start solving puzzle now.")

loop = 1

while loop <= MAX_LOOP:
    print()
    print ("Loop count= {}".format(loop))
    
    values = all_values(FULL_SIDE)
    
    possibles_list = setup_possibles_list(puzzle, values)
    
    # Remove conflicting known single values from same column, same row and same internal grid 
    # Start from top left spot and work to bottom right spot in puzzle
    for j in range(len(possibles_list)):

    # If value of spot is known single value then quit loop and move to next spot
        if len(possibles_list[j]) == 1:
            continue
    
        # Check all other spots in that column and remove conflicts
        possibles_list = resolve_column(possibles_list, j, FULL_SIDE)
    
        # Find all single value spots in each row and remove conflicts 
        possibles_list = resolve_row(possibles_list, j, FULL_SIDE)
   
        # Now check each inner grid for single value conflicts 
        possibles_list = resolve_inner_grid(possibles_list, j, PART_SIDE)
    
    loop = loop + 1  #Increment iteration loop counter                            

print(possibles_list)
show_grid_lines(possibles_list, FULL_SIDE, ROW_SEP, COL_SEP)    # Add separator characters between rows and columns
