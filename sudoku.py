#!/usr/bin/env python3

# Script to solve simple Sudoku puzzle


# Imports
import time    # in case want to time how long brute force solution takes


# Constants
PART_SIDE = 3  # start with 9 by 9 grid (16 by 16 also possible in the future)
FULL_SIDE = PART_SIDE ** 2
ROW_SEP = "-"   # separator symbol between rows in grid
COL_SEP = "|"   # separator symbol between columns in grid
SPACE = " "     # have space on either side of value to make reading grid easier
MAX_LOOP = 100  # Maximum number of loop before program ends
HUGE_VALUE = 100000   # Initial count for number of values still possible

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


def get_hard_puzzle(): # return data file as list
                          # cannot have blank in list so use "0" for blanks
    hard_puzzle = [0,0,0,0,0,0,0,1,7,\
                   0,0,7,0,6,2,0,0,5,\
                   4,0,0,0,1,0,0,0,0,\
                   0,7,0,0,0,3,0,0,8,\
                   0,0,3,5,0,4,1,0,0,\
                   8,0,0,1,0,0,0,6,0,\
                   0,0,0,0,4,0,0,0,9,\
                   1,0,0,7,9,0,2,0,0,\
                   3,4,0,0,0,0,0,0,0]
    return hard_puzzle


def get_hardest_puzzle(): # return data file as list
                          # cannot have blank in list so use "0" for blanks
    hardest_puzzle = [0,0,0,2,0,1,5,0,3,\
                   2,0,0,0,0,6,0,7,0,\
                   0,0,9,0,0,0,0,0,0,\
                   9,0,0,0,8,0,7,0,2,\
                   0,1,0,0,0,0,0,3,0,\
                   8,0,6,0,1,0,0,0,9,\
                   0,0,0,0,0,0,9,0,0,\
                   0,9,0,8,0,0,0,0,6,\
                   3,0,8,7,0,2,0,0,0]
    return hardest_puzzle


def select_puzzle():
    print()   # blank line
    num = int(input("Which puzzle do you want to solve? \n1 (easiest) or \n2 (medium) or \n3 (hard) or \n4 (hardest). \nEnter value: ")) # Convert returned string to integer
    if num == 1: 
        puzzle = get_initial_puzzle()
    if num == 2: 
        puzzle = get_medium_puzzle()
    if num == 3: 
        puzzle = get_hard_puzzle()
    if num == 4: 
        puzzle = get_hardest_puzzle()
    return puzzle


def show_grid(puzzle):    # format known puzzle values into grid to be displayed to user
    print()  # blank line
    side = size_of_puzzle_side(puzzle)
    for row in range(side):
        for column in range(side):
            print(puzzle[row * side + column], " ",  sep="", end="")
        print() # line break at end of line


def create_row_separating_line_with_intersecting_plus_symbol(side , ROW_SEP, COL_SEP):  # "+-+-+-...-+" format
    side = size_of_puzzle_side(puzzle)
    for j in range(side):
        print("+", ROW_SEP, ROW_SEP, ROW_SEP, sep="", end="") 
    print("+")   # Need new line at end of string of symbols


def create_extended_row_separating_line_with_intersecting_plus_symbol(side, ROW_SEP, COL_SEP):  # "+-+-+-...-+" format
    for j in range(side):
        print("+", ROW_SEP, ROW_SEP, ROW_SEP, ROW_SEP, ROW_SEP, sep="", end="") 
    print("+")   # Need new line at end of string of symbols


def show_grid_lines(puzzle, ROW_SEP, COL_SEP):    # Add separator characters between rows and columns
    print()  # blank line
    side = size_of_puzzle_side(puzzle)
    for row in range(side):
        create_row_separating_line_with_intersecting_plus_symbol(side, ROW_SEP, COL_SEP)
        for column in range(side):
            print(COL_SEP, SPACE, puzzle[row * side + column], SPACE,  sep="", end="")
        print(COL_SEP) # Add final column separator and default line break at end of line
    create_row_separating_line_with_intersecting_plus_symbol(side, ROW_SEP, COL_SEP)  # Create bottom separator line


def show_extended_grid_lines(puzzle, ROW_SEP, COL_SEP):    # Add separator characters between rows and columns
    print()  # blank line
    side = size_of_puzzle_side(puzzle)
    for row in range(side):
        create_extended_row_separating_line_with_intersecting_plus_symbol(side, ROW_SEP, COL_SEP)  # "+---+---...+" format
        for column in range(side):
            print(COL_SEP, SPACE, puzzle[row * side + column], SPACE,  sep="", end="")
        print(COL_SEP) # Add final column separator and default line break at end of line
    create_extended_row_separating_line_with_intersecting_plus_symbol(side, ROW_SEP, COL_SEP)  # final line


def all_values(side):
    values = []
    for count in range(1, side + 1):
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
            break    # Exit loop at first failure
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


def size_of_puzzle_side(list):
    num = int((len(list) + 1) ** 0.5)  # Integer number of columns or rows is square root of number of spots
    return num


def column_width(possibles_list): # Determine largest possible list in each column so can print column that width
    number_of_columns = size_of_puzzle_side(possibles_list)  # Integer number of columns is square root of number of spots
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


def delete_pair_from_row(possibles_list, a, b):   # Then delete these two values from all other spots in row
# Delete both values from all the other spots in the row except the two matching spots
    progress = False # Track whether any values are removed  (default = False = nothing removed)
    side = size_of_puzzle_side(possibles_list)  # calculate length of row or column
    correct_row = a // side    # Determine which row to delete values from
    for j in range(len(possibles_list)):   # Iterate through all spots
        if j // side != correct_row:
            continue   # Wrong row so skip
        if j == a:
            continue    # skip since cannot delete from self
        if j == b:
            continue    # skip since cannot delete from self
        if possibles_list[a][0] in possibles_list[j]:
            progress = True
            print("Removing {} from {} in spot {}.".format(possibles_list[a][0], possibles_list[j], j))   #DEBUG
            possibles_list[j].remove(possibles_list[a][0])  # Remove first value 
            possibles_list[j] = convert_list(possibles_list[j])    # Convert list of single list to list of single integer
        if possibles_list[a][1] in possibles_list[j]:
            progress = True
            print("Removing {} from {} in spot {}.".format(possibles_list[a][1], possibles_list[j], j))   #DEBUG
            possibles_list[j].remove(possibles_list[a][1])  # Remove second value 
            possibles_list[j] = convert_list(possibles_list[j])    # Convert list of single list to list of single integer
    return progress


def delete_pair_from_column(possibles_list, a, b):   # Then delete these two values from all other spots in column
# Delete both values from all the other spots in the column except the two matching spots
    progress = False # Track whether any values are removed  (default = False = nothing removed)
    side = size_of_puzzle_side(possibles_list)   # calculate length of row or column
    correct_column = a % side    # Determine which column to delete values from
    for j in range(len(possibles_list)):   # Iterate through all spots
        if j % side != correct_column:
            continue   # Wrong column so skip
        if j == a:
            continue    # skip since cannot delete from self
        if j == b:
            continue    # skip since cannot delete from self
        if possibles_list[a][0] in possibles_list[j]:
            progress = True
            print("Removing {} from {} in spot {}.".format(possibles_list[a][0], possibles_list[j], j))   #DEBUG
            possibles_list[j].remove(possibles_list[a][0])  # Remove first value 
            possibles_list[j] = convert_list(possibles_list[j])    # Convert list of single list to list of single integer
        if possibles_list[a][1] in possibles_list[j]:
            progress = True
            print("Removing {} from {} in spot {}.".format(possibles_list[a][1], possibles_list[j], j))   #DEBUG
            possibles_list[j].remove(possibles_list[a][1])  # Remove second value 
            possibles_list[j] = convert_list(possibles_list[j])    # Convert list of single list to list of single integer
    return progress


def delete_pair_from_minigrid(possibles_list, a, b, list):
    # Delete value from all spots in own inner grid except self
    progress = False
    for j in list: # Cycle through all spots in minigrid
        if j == a or j == b:
            continue # Skip since cannot delete self
        if possibles_list[a][0] in possibles_list[j]:
            progress = True
            possibles_list[j].remove(possibles_list[a][0])
            possibles_list[j] = convert_list(possibles_list[j])    # Convert list of single list to list of single integer
        if possibles_list[a][1] in possibles_list[j]:
            progress = True
            possibles_list[j].remove(possibles_list[a][1])
            possibles_list[j] = convert_list(possibles_list[j])    # Convert list of single list to list of single integer
    return progress


def find_pairs(possibles_list):  
# If there are two pairs in a column, row or minigrid. 
# One can remove those two numbers from all other spots in that column, row or minigrid.
    side = size_of_puzzle_side(possibles_list)   # calculate length of row or column
    row_progress = False
    column_progress = False
    minigrid_progress = False
    for j in range(len(possibles_list)):
        if len(possibles_list[j]) == 2:
            print("Grid {} has two values of {}.".format(j, possibles_list[j])) 
            # Match rows
            for k in range(len(possibles_list)):
                row = j // side
                if j // side == k // side:  # In same row
                    if j != k:  # Cannot compare self to self
                        if possibles_list[j] == possibles_list[k]:  # If contents match
                            print("Spots {} and {} in row {} both have value of {}.".format(j, k, row,  possibles_list[j]))
                            row_progress = row_progress or delete_pair_from_row(possibles_list, j, k)    # Then delete these two values from all other spots in row
            # Match column
            for k in range(len(possibles_list)):
                column = j % side
                if j % side == k % side:  # In same column
                    if j != k:  # Cannot compare self to self
                        if possibles_list[j] == possibles_list[k]:  # If contents match
                            print("Spots {} and {} in column {} both have value of {}.".format(j, k, column,  possibles_list[j]))
                            column_progress = column_progress or delete_pair_from_column(possibles_list, j, k) # Delete these two values from all other spots in column
            # Match minigrid
            list_of_internal_grids = create_list_of_internal_grids(PART_SIDE)  # Create list of internal grid lists for any size grid
            for list in list_of_internal_grids:
                for k in range(len(possibles_list)):
                    if j in list and k in list:
                        if j != k:
                            if possibles_list[j] == possibles_list[k]: # If contents match
                                print("Spots {} and {} in same minigrid both have value of {}.".format(j, k, possibles_list[j]))
                                minigrid_progress = minigrid_progress or delete_pair_from_minigrid(possibles_list, j, k, list) # Delete these two values from all other spots in minigrid
    return (row_progress or column_progress or minigrid_progress)  # True if have deleted any values in rows or columns or minigrid


def how_to_continue_when_stalled():  # Prompt user if and how to continue when stalled
    while True:
        reply = input("How continue? \n1. Quit or \n2. Brute force from zero or \n3. Brute force from an input number or \n4. Try guessing pairs or \n5. Time estimate \nEnter value:  ")
        if reply == "1" or reply == "2" or reply == "3" or reply == "4" or reply == "5":
            reply = int(reply)   # Convert string to integer
            break # exit loop otherwise prompt again
        else:
            print("Try again.")   # prompt for another input
    return reply

def count_pairs(list):  # Find unique pairs in puzzle
    dict_of_pairs = {}   # Use dictionary to track and count unique pairs in puzzle
    dict_of_pair_locations = {}   # Dictionary to track pair locations as list
    for j in range(len(list)):
        if len(list[j]) == 2:    # Only count pairs
            if str(list[j]) in dict_of_pairs:   # Must convert dictionary index from list to string (list not allowed as index)
                dict_of_pairs[str(list[j])] = dict_of_pairs[str(list[j])] + 1  # Increment count
                dict_of_pair_locations[str(list[j])].append(j)  # Append next value to list
            else:
                dict_of_pairs[str(list[j])] = 1  # Initialize count
                dict_of_pair_locations[str(list[j])] = [j]  # First spot in grid
    print(dict_of_pairs)   #DEBUG
    print(dict_of_pair_locations)   #DEBUG
    return (dict_of_pairs, dict_of_pair_locations)


def try_guess_list(possibles_list):
    # Find two spots with two different possible values and cycle through all possible four configurations until one works
    guess_list = possibles_list.copy()
    return guess_list


def get_stalled_spots_list(list):   # Determine which spots are still unknown after resolving stalls
    unknown_spots = dict()   # Initialize dictionary
    for j in range(len(list)):
        if len(list[j]) > 1:  # Spot is not yet resolved
            unknown_spots[j] = list[j]   # Add this to dictionary
            print("Unknown Spot {} is {}.".format(j, list[j]))   #DEBUG
    return unknown_spots
        

def get_known_spots_list(list):   # Determine which spots are known after resolving stalls
    known_spots = dict()   # Initialize dictionary
    for j in range(len(list)):
        if len(list[j]) == 1:  # Store known single values in another list
            known_spots[j] = list[j]   
    return known_spots
        

def get_number_possible_solutions(unknowns_dict):
    num = 1
    for j in unknowns_dict.values():
        num = num * len(j)
#DEBUG        print(num)
    return num


def size_of_puzzle(puzzle):
    num = len(puzzle)
    return num


def select_set_of_unknown_values(puzzle, unknown_spots, known_spots, iteration):
#    print(puzzle)   #DEBUG
#    print(unknown_spots)   #DEBUG
    list_of_keys = list(unknown_spots.keys())    # convert dictionary keys to list
#    print(list_of_keys)   #DEBUG
    list_of_keys.sort()    # Sort list into ascending order since dictionary is unordered
    list_of_keys.reverse()   # Sort list of keys into descending order
#    print(list_of_keys)   #DEBUG
    for j in range(len(list_of_keys)):
#        print("{}  key value is {} and values are {}.".format(j, list_of_keys[j], unknown_spots[list_of_keys[j]]))
        grid_spot_index = iteration % len(unknown_spots[list_of_keys[j]])   # Calculate index into list of possible values
#        print("Replace possibles list of {} with value of {}.".format(unknown_spots[list_of_keys[j]], unknown_spots[list_of_keys[j]][grid_spot_index]))
        puzzle[list_of_keys[j]] = unknown_spots[list_of_keys[j]][grid_spot_index]    # Replace list of possible values with single trial value
        iteration = iteration // len(unknown_spots[list_of_keys[j]])
    return puzzle


def create_trial_grid(list, unknown_spots, known_spots, index):
    trial_solution = list.copy()    # start by copying the current list, 
                                    # then cycle through and overwrite the spots with multiple values
                                    # Using 'modulo' and 'remainder' of index value to determine which
                                    # of multiple values to set in each spot of grid
    for j in range(index):   # Cycle through all possible combinations 
        trial_solution = select_set_of_unknown_values(trial_solution, unknown_spots, known_spots, j)
    return trial_solution 




def init_trial_count(puzzle): # Initialize all row, column and internal grid counts to zero
    num = size_of_puzzle(puzzle)
    count = dict()
    for j in range(num):
        count[j] = 0  # set all grid spot counts to zero
#    print(count)    #DEBUG
    return count


def quick_check(puzzle): # Ensure count of each number is correct (not too high or too low)
    result = True
    num = size_of_puzzle_side(puzzle)    # Get length of side or column
    for j in range(1, num + 1):  # For every possible value
        if puzzle.count([j]) != num:
            print("Count of {} is {}.".format(j, puzzle.count([j])))
            result = False
            break
    return result

def count_rows(puzzle):   # count how many of each value are in each row
    # Use list built-in 'count' method to ensure exactly one of each value in every row
    num = size_of_puzzle_side(puzzle)
    result = True
    test_row = []
    for j in num:
        test_row = puzzle[j * num:(j + 1) * num]  # quickly create using slices
        for k in num: 
            if test_row.count(k) != 1:  # Ensure exactly one of each value in row
                result = False
                break
    return result


def count_columns(puzzle):  # Count how many of each value are in each column
    # Use list built-in 'append' method to create list and 
    # 'count' method to ensure exactly one of each value in every column
    num = size_of_puzzle_side(puzzle)
    result = True
    test_column = []
    for c in num:
        for j in num: 
            test_column.append(puzzle[c + (j * num)])  # Build list of column values to test
        for k in num:
            if test_column.count(k) != 1:  # Ensure exactly one of each value in column
                result = False
                break
    return result

    pass


def count_internal_grids(puzzle):  # Count how many of each value are in each internal grid
    pass


def test_trial_solution(puzzle):  # Build first possible grid solutions
    result = True
    while result:      # If any tests fail then result will be False
        result = result and quick_check(puzzle)
        result = result and count_rows(puzzle)   
        result = result and count_columns(puzzle)
        result = result and count_internal_grids(puzzle)
#    print("Result is {}".format(result))     #DEBUG
    return result

def get_starting_value():
    num = input("Enter starting number: ")
    num = int(num)    # Convert from string to integer
    return  num 


def bruteforce(list, num):   # Try all possible combinations and see which works
#    unknown_spots =  get_stalled_spots_list(list)   # Create list of grid spots that are still unknown
#    num_unknown_spots = len(unknown_spots)   # Count number of unknown spots in grid
#    print("Number of 'num_unknown_spots' is {}".format(num_unknown_spots))   
#    known_spots = get_known_spots_list(list)  # List of known spots
#    number_solutions = get_number_possible_solutions(unknown_spots)
#    print("Number of possible brute force solutions is: {} over {} unknown spots".format(number_solutions, num_unknown_spots))

    for j in range(num, number_solutions):  # Cycle through all possible values in grids until one works
        trial_solution = create_trial_grid(possibles_list, unknown_spots, known_spots, j)
        result = test_trial_solution(trial_solution)
        if result == True:
            print(trial_solution)     #DEBUG
            break   # This is a successful solution 
        else:
            print("Iteration {} did not work.".format(j))
    return trial_solution


# Main code

# Initialize variables
last_count = HUGE_VALUE

greet_user() 
        
puzzle = select_puzzle()   # Choose between the two puzzles
side = size_of_puzzle_side(puzzle)

values = all_values(FULL_SIDE)

print()
print("These are the initial puzzle values:", puzzle)  # Show initial puzzle data in long list format

show_grid(puzzle) # Show puzzle values in more readable grid format

show_grid_lines(puzzle, ROW_SEP, COL_SEP)

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
    
    progress = find_pairs(possibles_list)  
    if progress:  # reset loop and count values so looping continues
        loop = 0
        last_count = 100000

    (done, reason) = are_we_done(possibles_list, loop, last_count)

#all_grids_resolved(possibles_list) or loop >= MAX_LOOP or no_progress(last_count)
    last_count = current_count
else:
    print("Game over because {} so try guessing.".format(reason))
    progress = find_pairs(possibles_list)  

print()
print()
#DEBUG  print(possibles_list)
print("***************** Final puzzle result is: ********************")
#show_extended_grid_lines(possibles_list, FULL_SIDE, ROW_SEP, COL_SEP)    
show_adjustable_grid_lines(possibles_list, FULL_SIDE, ROW_SEP, COL_SEP, column_max)    #DEBUG 

count = count_total_possible_values(possibles_list)   # Count all the known and unknown values in the puzzle
print("Total values count in the puzzle is {}.".format(count_total_possible_values(possibles_list)))

if count > len(possibles_list):  # Decide how to proceed if there are still unresolved grids
    print()
    print("There are still unresolved grids.")
    unknown_spots =  get_stalled_spots_list(possibles_list)   # Create list of grid spots that are still unknown
    num_unknown_spots = len(unknown_spots)   # Count number of unknown spots in grid
    known_spots = get_known_spots_list(possibles_list)  # List of known spots
    number_solutions = get_number_possible_solutions(unknown_spots)
    print()
    print("Number of possible brute force solutions is: {} over {} unknown spots".format(number_solutions, num_unknown_spots))


    reply = how_to_continue_when_stalled()  # Prompt user if and how to continue when stalled

    if reply == 1:  # Quit game
        pass

    if reply == 2: # Brute force solution starting from zero
        successful_solution = bruteforce(possibles_list, 0)

    if reply == 3: # Brute force solution starting from entered value (allows continuation)
        begin_num  = get_starting_value()
        successful_solution = bruteforce(possibles_list, begin_num)

    if reply == 4:
        while True:
            guess_list = try_guess_list(possibles_list)    # Copy stalled list and start guessing
            (dict_of_pairs, dict_of_pair_locations) = count_pairs(guess_list)  # Find unique pairs in puzzle
    
    if reply == 5:   # Time trial
        start_num = 0
        ending_num = 1000
        start_time = get_time()
        end_time = get_time()
else:
    print("All grids resolved.")
