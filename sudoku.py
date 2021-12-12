#!/usr/bin/env python3

# Script to solve simple Sudoku puzzle

# Constants
PART_SIDE = 3  # start with 9 by 9 grid (16 by 16 also possible in the future)
FULL_SIDE = PART_SIDE ** 2
ROW_SEP = "-"   # separator symbol between rows in grid
COL_SEP = "|"   # separator symbol between columns in grid
SPACE = " "     # have space on either side of value to make reading grid easier
MAX_LOOP = 100  # Maximum number of loop before program ends

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


def get_medium_puzzle(): # return data file as list
                          # cannot have blank in list so use "0" for blanks
    medium_puzzle = [8,0,0,7,0,6,0,0,0,\
                     0,0,6,0,0,0,0,5,0,\
                     0,9,2,4,0,0,0,7,6,\
                     9,0,7,6,2,1,5,0,3,\
                     0,2,0,0,0,0,0,1,0,\
                     5,0,1,9,4,7,6,0,8,\
                     2,5,0,0,0,4,1,8,0,\
                     0,6,0,0,0,0,2,0,0,\
                     0,0,0,2,0,5,0,0,4]
    return medium_puzzle


def select_puzzle():
    num = int(input("Which puzzle do you want to solve: 1 or 2?")) # Convert returned string to integer
    if num == 1: 
        puzzle = get_initial_puzzle()
    if num == 2: 
        puzzle = get_medium_puzzle()
    return puzzle


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


def create_extended_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP):  # "+-+-+-...-+" format
    for j in range(FULL_SIDE):
        print("+", ROW_SEP, ROW_SEP, ROW_SEP, ROW_SEP, ROW_SEP, sep="", end="") 
    print("+")   # Need new line at end of string of symbols


def show_grid_lines(puzzle, FULL_SIDE, ROW_SEP, COL_SEP):    # Add separator characters between rows and columns
    print()  # blank line
    for row in range(FULL_SIDE):
        create_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP)
        for column in range(FULL_SIDE):
            print(COL_SEP, SPACE, puzzle[row * FULL_SIDE + column], SPACE,  sep="", end="")
        print(COL_SEP) # Add final column separator and default line break at end of line
    create_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP)  # Create bottom separator line


def show_extended_grid_lines(puzzle, FULL_SIDE, ROW_SEP, COL_SEP):    # Add separator characters between rows and columns
    print()  # blank line
    for row in range(FULL_SIDE):
        create_extended_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP)  # "+---+---...+" format
        for column in range(FULL_SIDE):
            print(COL_SEP, SPACE, puzzle[row * FULL_SIDE + column], SPACE,  sep="", end="")
        print(COL_SEP) # Add final column separator and default line break at end of line
    create_extended_row_separating_line_with_intersecting_plus_symbol(FULL_SIDE, ROW_SEP, COL_SEP)  # final line


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


def convert_list(list_of_list):    # Convert list of single list to list of single integer
    if len(list_of_list) == 1:     # for example "[[1]]" becomes "[1]"
        for item in list_of_list:
            if isinstance(item, list):
                list_of_list = item   # replace list of list with single list
    return list_of_list


def resolve_column(possibles_list, j, FULL_SIDE):
    col = j % FULL_SIDE  # determine which column spot is in
    
    # Delete value from all spots in column except self
    for k in range(len(possibles_list)):
#DEBUG        print("J = {}, K = {}".format(j,k))    #DEBUG

        if j % FULL_SIDE != k % FULL_SIDE:
            continue    # skip this value since in different column
        if j == k:
            continue    # skip since cannot compare self to self 
        if possibles_list[j] in possibles_list[k]:
            possibles_list[k].remove(possibles_list[j])
            possibles_list[k] = convert_list(possibles_list[k])    # Convert list of single list to list of single integer
    return possibles_list
    

def resolve_row(possibles_list, j, FULL_SIDE):
    # Delete value from all spots in row except self
    # Find all non-single value spots in each row and remove them from other possible spots in same row
    # Determine row number using integer division (//)
    for k in range(len(possibles_list)):
        if j // FULL_SIDE != k // FULL_SIDE:
            continue   # skip since different row
#DEBUG        print("Row {} matches row {}".format(j//FULL_SIDE, k//FULL_SIDE))    #DEBUG
        if j == k:
#DEBUG            print("  Skip since cannot match to self")
            continue    # skip since cannot compare self to self 
        if possibles_list[j] in possibles_list[k]:
            possibles_list[k].remove(possibles_list[j])
            possibles_list[k] = convert_list(possibles_list[k])    # Convert list of single list to list of single integer
    return possibles_list
    

def resolve_inner_grid(possibles_list, j, PART_SIDE):
    # Delete value from all spots in own inner grid except self
    # Create list of sets of inner grids based on PART_SIDE
    list_of_internal_grids = create_list_of_internal_grids(PART_SIDE)  # Create list of internal grid lists for any size grid

    for list in list_of_internal_grids:
    # first verify that both spots are located in the same inner grid 
    # then verify that this is not the exact same spot as the outer loop
    # then verify that spot only has a single value
    # then if single value inside outer list, remove it
        for k in range(len(possibles_list)):
            if j in list and k in list:
#DEBUG                print("Both {} and {} in same internal grid {}".format(j, k, list))  #DEBUG
                if j == k:
                    continue  # Cannot delete self from self
                if possibles_list[j] in possibles_list[k]:
                    possibles_list[k].remove(possibles_list[j])
                    possibles_list[k] = convert_list(possibles_list[k])    # Convert list of single list to list of single integer
    return possibles_list


def all_grids_resolved(possibles_list):
    resolved = True
    for j in range(len(possibles_list)):
        if len(possibles_list[j]) > 1:
            resolved = False
            break
    return resolved


def count_total_possible_values(possibles_list):   # Count all the known and unknown values in the puzzle
    count = 0
    for j in range(len(possibles_list)):
        count = count + len(possibles_list[j])
    return count


def init_column_width(possibles_list, number_of_columns):   # Initialize all dictionary values to one
    column_max = {}   # Initialize empty dictionary
    for j in range(number_of_columns):
        column_max[j] = 1
    return column_max


def column_width(possibles_list): # Determine largest possible list in each column so can print column that width
    number_of_columns = int((len(possibles_list) + 1) ** 0.5)  # Integer number of columns is square root of number of spots
    column_max = init_column_width(possibles_list, number_of_columns)   # Init all values to one
    for j in range(len(possibles_list)):  # Iterate through entire list    
        column = j % number_of_columns
        if len(possibles_list[j]) > column_max[column]:
            column_max[column] = len(possibles_list[j])  # Increase width of column 
    return column_max

def create_adjustable_row_separating_line(FULL_SIDE, ROW_SEP, COL_SEP, column_max):  # "+------------+-+...-+" format
    for j in range(FULL_SIDE):
#DEBUG        print("+", sep="", end="")  # Print first character in line
        print("+", sep="", end="")  # Print first character in line

        # Column width between COL_SEP is 5 for one element, 12 for two elements, plus 5 for every additional element
        if column_max[j] == 1: width = 5
        if column_max[j] == 2: width = 12
        if column_max[j] > 2: width = 12 + (column_max[j] - 2) * 5
     
        print("{}".format(ROW_SEP * width), sep="", end="")   # column width of 5 for single element
    print("+")   # Complete end of line with intersecting symbol


def show_adjustable_grid_lines(possibles_list, FULL_SIDE, ROW_SEP, COL_SEP, column_max):    # Adjust column spacing based on max column width
    print()  # blank line
    for row in range(FULL_SIDE):
        create_adjustable_row_separating_line(FULL_SIDE, ROW_SEP, COL_SEP, column_max)  # "+---+---...+" format

        for column in range(FULL_SIDE):
            # Column width between COL_SEP is 5 for one element, 12 for two elements, plus 5 for every additional element
            if column_max[column] == 1: width = 3
            if column_max[column] == 2: width = 10
            if column_max[column] > 2: width = 10 + (column_max[column] - 2) * 5
  #DEBUG          print(COL_SEP, SPACE, possibles_list[row * FULL_SIDE + column], SPACE,  sep="", end="")
            print("{}{}{:^{w}}{}".format(COL_SEP, SPACE, str(possibles_list[row * FULL_SIDE + column]), SPACE, w=width),  sep="", end="")
        print("{}".format(COL_SEP))    # End of line
    create_adjustable_row_separating_line(FULL_SIDE, ROW_SEP, COL_SEP, column_max)  # bottom-most line for grid
    #        print("{}".format(column, end=""))


def list_count(possibles_list):
    current_count = 0
    for j in possibles_list:
        current_count = current_count + len(j)
    return current_count


# Determine if game over or continues 
def are_we_done(possibles_list, loop, last_count):
    done = False
    reason = "Continue"
    if last_count == list_count(possibles_list):
        done = True
        reason = "No progress after {} loops".format(loop)
    if loop > MAX_LOOP:
        done = True
        reason = "Looped maximum of {} times".format(MAX_LOOP)
    if all_grids_resolved(possibles_list):
        done = True
        reason = "All {} grids resolved".format(len(possibles_list))
    return (done, reason)


# Main code

# Initialize variables
last_count = 1000000

greet_user() 
        
puzzle = select_puzzle()   # Choose between the two puzzles

values = all_values(FULL_SIDE)

print()
print("These are the initial puzzle values:", puzzle)  # Show initial puzzle data in long list format

show_grid(puzzle, FULL_SIDE) # Show puzzle values in more readable grid format

show_grid_lines(puzzle, FULL_SIDE, ROW_SEP, COL_SEP)

print()
print("Start solving puzzle now.")

loop = 0
done = False

possibles_list = setup_possibles_list(puzzle, values)
outer_list = possibles_list.copy()

while not done:
    print()
    print ("Loop count= {}".format(loop))
    
    count = count_total_possible_values(possibles_list)   # Count all the known and unknown values in the puzzle
    print("Total values count in the puzzle is {}.".format(count_total_possible_values(possibles_list)))

    c = column_width(possibles_list) # Determine largest possible list in each column so can print column that width
    print("Column widths are: {}".format(c))    #DEBUG

    # Remove conflicting known single values from same column, same row and same internal grid of inner loop
    # Start from top left spot and work to bottom right spot in puzzle
    for j in range(len(outer_list)):
#DEBUG        print("J=", j)   #DEBUG
    # If value of spot is known single value then remove it from matching column, row and inner grid
        if len(outer_list[j]) != 1:
            continue      # skip spot since contains more than one possible value
    
        # Check all other spots in that column and remove conflicts
        possibles_list = resolve_column(possibles_list, j, FULL_SIDE)
    
        # Find all single value spots in each row and remove conflicts 
        possibles_list = resolve_row(possibles_list, j, FULL_SIDE)
   
        # Now check each inner grid for single value conflicts 
        possibles_list = resolve_inner_grid(possibles_list, j, PART_SIDE)

        outer_list = possibles_list.copy()    # update outer list for next while loop iteration
    
    loop = loop + 1  #Increment iteration loop counter                            
#DEBUG    show_grid_lines(possibles_list, FULL_SIDE, ROW_SEP, COL_SEP)    # Add separator characters between rows and columns

    column_max = column_width(possibles_list)    #DEBUG

#DEBUG    create_adjustable_row_separating_line(FULL_SIDE, ROW_SEP, COL_SEP, column_max)  # DEBUG
    show_adjustable_grid_lines(possibles_list, FULL_SIDE, ROW_SEP, COL_SEP, column_max)    #DEBUG 

    current_count = list_count(possibles_list)

    (done, reason) = are_we_done(possibles_list, loop, last_count)

#all_grids_resolved(possibles_list) or loop >= MAX_LOOP or no_progress(last_count)
    last_count = current_count
else:
    print("Game over because {}.".format(reason))

print()
print()
#DEBUG  print(possibles_list)
print("***************** Final puzzle result is: ********************")
#DEBUG  show_extended_grid_lines(possibles_list, FULL_SIDE, ROW_SEP, COL_SEP)    

count = count_total_possible_values(possibles_list)   # Count all the known and unknown values in the puzzle
print("Total values count in the puzzle is {}.".format(count_total_possible_values(possibles_list)))
