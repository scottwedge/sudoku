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

# Main code
greet_user() 
        
# Create list of sets of inner grids based on PART_SIDE
list_of_internal_grids = create_list_of_internal_grids(PART_SIDE)  # Create list of internal grid lists for any size grid

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
#DEBUG  print(possibles_list)

# Remove known single values from same column, same row and same internal grid 
# Remove known values in column
# Start from top left spot and work to bottom right spot in puzzle
for j in range(len(possibles_list)):
#DEBUG    print(".....................START COLUMN SOLVING.............................")
# Use modulo operator (%) to determine which column (0 through FULL_SIDE-1)
# spot is in and check all other spots in that column for known single values
# Use 'break' and 'continue' inside the loop

    col = j % FULL_SIDE  # determine which column spot is in
#DEBUG    print("Spot {} is column {}.".format(j, col))

# If value of spot is known then quit loop and move to next spot
#    print("..............DEBUG............")
#    print("Spot can be {}".format(possibles_list[j]))    #DEBUG
    if len(possibles_list[j]) == 1:
        continue

# Find all other spots in that column (col) with only a single value 
# and remove from current spot if it is in list of possible values
    else:
        for k in range(len(puzzle)):
            if j % FULL_SIDE != k % FULL_SIDE:
                continue    # skip this value since in different column
            # continue comparison since same column
            print("Matching spot {} wth spot {}".format(j,k), end="")    #DEBUG
            if j == k:
                print("  Skip since cannot match to self")
                continue    # skip since cannot compare self to self 
            
            if len(possibles_list[k]) == 1:
                print("  Single value {}".format(possibles_list[k], end=""))  #DEBUG
                if possibles_list[k] in possibles_list[j]:    #Must convert to integer else not "in" list
                    print("{} in {} so remove it".format(possibles_list[k], possibles_list[j]), end ="")
                    possibles_list[j].remove(possibles_list[k])  # remove value from list
                    print(" leaves {}".format(possibles_list[j]))
                    continue
                else:
                    print("Not in {} so do nothing".format(possibles_list[j]))
                    continue
            else:
                print("  Not single value {} so skip".format(possibles_list[k]))
                    

# Find all single value spots in each row and remove them from other possible spots in same row
# Determine row number using integer division (//)
        for k in range(len(puzzle)):
            if j // FULL_SIDE != k // FULL_SIDE:
                continue   # return to top of inner ('k') loop
            print("Row {} matches row {}".format(j//FULL_SIDE, k//FULL_SIDE))    #DEBUG
            if j == k:
                print("  Skip since cannot match to self")
                continue    # skip since cannot compare self to self 
            if len(possibles_list[k]) == 1:    # single value in spot
                print("Single value {} in spot {} ....".format(possibles_list[k], k), end = "") 
                if possibles_list[k] in possibles_list[j]:
                    print(" {} is in {} ".format(possibles_list[k], possibles_list[j]), end="")
                    possibles_list[j].remove(possibles_list[k])
                    print(" leaves {}".format(possibles_list[j]))

# Now check each inner grid for single values and remove them from the other possible spots


        for k in range(len(puzzle)):
        # first verify that both spots are located in the same inner grid 
        # then verify that this is not the exact same spot as the outer loop
        # then verify that spot only has a single value
        # then if single value inside outer list, remove it
            for list in list_of_internal_grids:
                if j in list and k in list:
                    print("Both {} and {} in same internal grid {}".format(j, k, list))  #DEBUG
                    if j == k:
                        continue  # Cannot delete self from self
                    if len(possibles_list[k]) == 1:
                        if possibles_list[k] in possibles_list[j]:
                            print("Remove {} from {}".format(possibles_list[k], possibles_list[j]), end = "")
                            possibles_list[j].remove(possibles_list[k])
                            print(" leaves {}".format(possibles_list[j]))
                        

print(possibles_list)
show_grid_lines(possibles_list, FULL_SIDE, ROW_SEP, COL_SEP)    # Add separator characters between rows and columns
