#!/usr/bin/env python3

# Script to solve simple Sudoku puzzle


# Imports
import time    # in case want to time how long brute force solution takes
import random  # for random quick time instead of very long delays
import copy    # Need to perform deep copy so can restore previous version of puzzle


# Constants
ROW_SEP = "-"   # separator symbol between rows in grid
COL_SEP = "|"   # separator symbol between columns in grid
SPACE = " "     # have space on either side of value to make reading grid easier
MAX_LOOP = 100  # Maximum number of loop before program ends
HUGE_VALUE = 100000   # Initial count for number of values still possible


# Functions
def greet_user():    # Greet user
    print("Welcome to my Sudoku solving application ", end="")
    print("for either 9x9 or 16x16 puzzle.")


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
    while True:
        print()   # blank line
        val = input("Which puzzle do you want to solve? \n1 (easiest) or \n2 (medium) or \n3 (hard) or \n4 (hardest). \nEnter value: ")  
        try:
            num = int(val)  # Convert returned string to integer
        except ValueError:
            print("'{}' is not valid. Enter a value between 1 and 4.".format(val))
        else:
            if num == 1:
                puzzle = get_initial_puzzle()
                break
            if num == 2:
                puzzle = get_medium_puzzle()
                break
            if num == 3:
                puzzle = get_hard_puzzle()
                break
            if num == 4:
                puzzle = get_hardest_puzzle()
                break
    print()  # Blank line
    print("Puzzle #{} selected.".format(num))  # Confirm selected choice
    return puzzle


def show_grid(puzzle):    # format known puzzle values into grid to be displayed to user
    print()  # blank line
    full_side = size_of_puzzle_side(puzzle)
    for row in range(full_side):
        for column in range(full_side):
            print(puzzle[row * full_side + column], " ",  sep="", end="")
        print()  # line break at end of line


def create_row_separating_line_with_intersecting_plus_symbol(full_side , ROW_SEP, COL_SEP):  # "+-+-+-...-+" format
    for j in range(full_side):
        print("+", ROW_SEP, ROW_SEP, ROW_SEP, sep="", end="") 
    print("+")   # Need new line at end of string of symbols


def create_extended_row_separating_line_with_intersecting_plus_symbol(side, ROW_SEP, COL_SEP):  # "+-+-+-...-+" format
    for j in range(side):
        print("+", ROW_SEP, ROW_SEP, ROW_SEP, ROW_SEP, ROW_SEP, sep="", end="") 
    print("+")   # Need new line at end of string of symbols


def show_grid_lines(puzzle, ROW_SEP, COL_SEP):    # Add separator characters between rows and columns
    print()  # blank line
    full_side = size_of_puzzle_side(puzzle)
    for row in range(full_side):
        create_row_separating_line_with_intersecting_plus_symbol(full_side, ROW_SEP, COL_SEP)
        for column in range(full_side):
            print(COL_SEP, SPACE, puzzle[row * full_side + column], SPACE,  sep="", end="")
        print(COL_SEP)  # Add final column separator and default line break at end of line
    create_row_separating_line_with_intersecting_plus_symbol(full_side, ROW_SEP, COL_SEP)  # Create bottom separator line


def show_extended_grid_lines(puzzle, ROW_SEP, COL_SEP):    # Add separator characters between rows and columns
    print()  # blank line
    full_side = size_of_puzzle_side(puzzle)
    for row in range(full_side):
        create_extended_row_separating_line_with_intersecting_plus_symbol(full_side, ROW_SEP, COL_SEP)  # "+---+---...+" format
        for column in range(full_side):
            print(COL_SEP, SPACE, puzzle[row * full_side + column], SPACE,  sep="", end="")
        print(COL_SEP)  # Add final column separator and default line break at end of line
    create_extended_row_separating_line_with_intersecting_plus_symbol(side, ROW_SEP, COL_SEP)  # final line


def all_values(side):
    values = []
    for count in range(1, side + 1):
        values.append([count])    # Add value as single list so can easily check if [k] in [j]
    return values


def setup_possibles_list(puzzle, values):
    new_puzzle = []   # initialize empty list
    full_side = size_of_puzzle_side(puzzle)

    for j in range(len(puzzle)):
        if puzzle[j] == 0:
            new_puzzle.append(all_values(full_side))  # all values possible for blank field
        else:
            new_puzzle.append([puzzle[j]])  # value is already known so use it as a list of one value
    return new_puzzle


def create_list_of_internal_grids(part_side):  # Create list of internal grid lists for any N x N grid
    list_of_internal_grids = []
    for s in range(part_side):  # Move down vertically between top left spot in column of left-most internal grids
                               # So in a 9x9 grid (spots 0-80) move between spots 0, 27 and 54
        for n in range(part_side):   # move to next grid to the right 
            internal_grid = []    # Initialize new list
            for v in range(part_side):  # Move vertically within internal grid 
                for h in range(part_side):  # Move horizontally within internal grid
                    spot = v * part_side ** 2 + h
                    spot = spot + n * part_side
                    spot = spot + s * part_side ** 3
                    internal_grid.append(spot)
            list_of_internal_grids.append(internal_grid)        
    return list_of_internal_grids


def convert_list(list_of_list):    # Convert list of single list to list of single integer
    if len(list_of_list) == 1:     # for example "[[1]]" becomes "[1]"
        for item in list_of_list:
            if isinstance(item, list):
                list_of_list = item   # replace list of list with single list
    return list_of_list


def convert_list_to_integer(list):  # From list of single list to single integer; from '[[1]]' to '1'
    if len(list) == 1:              # for example "[[1]]" becomes "1"
        for index in list:
            pass
    else:
        index = 0   # Return an invalid value for case where list length > 1
    return index


def resolve_column(puzzle, j, full_side):  # Delete value from all spots in column except self
    col = j % full_side  # determine which column spot is in
    
    for k in range(len(puzzle)):
        if j % full_side != k % full_side:
            continue    # skip this value since in different column
        if j == k:
            continue    # skip since cannot compare self to self 
        if puzzle[j] in puzzle[k]:
            puzzle[k].remove(puzzle[j])
            puzzle[k] = convert_list(puzzle[k])    # Convert list of single list to list of single integer
    return puzzle
    

def resolve_row(puzzle, j, full_side):  # Delete value from all spots in row except self
    # Find all non-single value spots in each row and remove them from other possible spots in same row
    # Determine row number using integer division (//)
    for k in range(len(puzzle)):
        if j // full_side != k // full_side:
            continue   # skip since different row
        if j == k:
            continue    # skip since cannot compare self to self 
        if puzzle[j] in puzzle[k]:
            puzzle[k].remove(puzzle[j])
            puzzle[k] = convert_list(puzzle[k])    # Convert list of single list to list of single integer
    return puzzle
    

def resolve_inner_grid(puzzle, j, part_side):  # Delete value from all spots in own inner grid except self
    list_of_internal_grids = create_list_of_internal_grids(part_side)  # Create list of internal grid lists for any size grid

    for list in list_of_internal_grids:
    # first verify that both spots are located in the same inner grid 
    # then verify that this is not the exact same spot as the outer loop
    # then verify that spot only has a single value
    # then if single value inside outer list, remove it
        for k in range(len(puzzle)):
            if j in list and k in list:
                if j == k:
                    continue  # Cannot delete self from self
                if puzzle[j] in puzzle[k]:
                    puzzle[k].remove(puzzle[j])
                    puzzle[k] = convert_list(puzzle[k])    # Convert list of single list to list of single integer
    return puzzle


def all_grids_resolved(puzzle):
    resolved = True
    for j in range(len(puzzle)):
        if len(puzzle[j]) > 1:
            resolved = False
            break    # Exit loop at first failure
    return resolved


def count_total_possible_values(puzzle):   # Count all the known and unknown values in the puzzle
    count = 0
    for j in range(len(puzzle)):
        count = count + len(puzzle[j])
    return count


def init_column_width(puzzle, number_of_columns):   # Initialize all dictionary values to one
    column_max = {}   # Initialize empty dictionary
    for j in range(number_of_columns):
        column_max[j] = 1
    return column_max


def size_of_puzzle_side(puzzle):
    full_side = int((len(puzzle) + 1) ** 0.5)  # Integer number of columns or rows is square root of number of spots
    return full_side


def size_of_grid_side(list):
    part_side = int((len(list) + 1) ** 0.25)  # Integer number of columns or rows is fourth root of number of spots
    return part_side


def column_width(puzzle):  # Determine largest possible list in each column so can print column that width
    number_of_columns = size_of_puzzle_side(puzzle)  # Integer number of columns is square root of number of spots
    column_max = init_column_width(puzzle, number_of_columns)   # Init all values to one
    for j in range(len(puzzle)):  # Iterate through entire list    
        column = j % number_of_columns
        if len(puzzle[j]) > column_max[column]:
            column_max[column] = len(puzzle[j])  # Increase width of column 
    return column_max


def create_adjustable_row_separating_line(full_side, ROW_SEP, COL_SEP, column_max):  # "+------------+-+...-+" format
    for j in range(full_side):
        print("+", sep="", end="")  # Print first character in line

        # Column width between COL_SEP is 5 for one element, 12 for two elements, plus 5 for every additional element
        if column_max[j] == 1: width = 5
        if column_max[j] == 2: width = 12
        if column_max[j] > 2: width = 12 + (column_max[j] - 2) * 5
     
        print("{}".format(ROW_SEP * width), sep="", end="")   # column width of 5 for single element
    print("+")   # Complete end of line with intersecting symbol


def show_adjustable_grid_lines(puzzle, full_side, ROW_SEP, COL_SEP, column_max):    # Adjust column spacing based on max column width
    print()  # blank line
    for row in range(full_side):
        create_adjustable_row_separating_line(full_side, ROW_SEP, COL_SEP, column_max)  # "+---+---...+" format

        for column in range(full_side):
            # Column width between COL_SEP is 5 for one element, 12 for two elements, plus 5 for every additional element
            if column_max[column] == 1: width = 3
            if column_max[column] == 2: width = 10
            if column_max[column] > 2: width = 10 + (column_max[column] - 2) * 5
            print("{}{}{:^{w}}{}".format(COL_SEP, SPACE, str(puzzle[row * full_side + column]), SPACE, w=width),  sep="", end="")
        print("{}".format(COL_SEP))    # End of line
    create_adjustable_row_separating_line(full_side, ROW_SEP, COL_SEP, column_max)  # bottom-most line for grid


def list_count(puzzle):
    current_count = 0
    for j in puzzle:
        current_count = current_count + len(j)
    return current_count


def are_we_done(puzzle, loop, last_count):  # Determine if game over or continues 
    done = False
    reason = "Continue"
    if last_count == list_count(puzzle):
        done = True
        reason = "No progress after {} loops".format(loop)
    if loop > MAX_LOOP:
        done = True
        reason = "Looped maximum of {} times".format(MAX_LOOP)
    if all_grids_resolved(puzzle):
        done = True
        (sane, reason) = check_puzzle_sanity(puzzle)  # Check if solved puzzle is valid
        if sane:
            reason = "Puzzle sane. All {} grids resolved".format(len(puzzle))
        else:
            reason = "Puzzle INSANE. All {} grids resolved".format(len(puzzle))
    return (done, reason)


def reset_count(num): 
    count = dict()  # Init dictionary to track count values in row, column and internal grid
    for j in range(1, num + 1):  # Create dict with index 1 through N for N=9 or 16
        count[j] = 0  # Reset all counts to zero
    return count


def all_columns_sane(puzzle):
    sanity = True
    reason = "All columns are sane."
    
    full_side = size_of_puzzle_side(puzzle)  # calculate number and length of column
    for j in range(full_side):  # for each column
        count = reset_count(full_side)  # reset all counters to zero
        for k in range(full_side):  # for every spot in column
            index = convert_list_to_integer(puzzle[j + k * full_side])  # Convert list to single integer index for dictionary 'count'
            try:
                count[index] = count[index] + 1
                if count[index] > 1:
                    sanity = False
                    reason = "Column " + str(j+1) + " is INSANE."
                    break  # exit 
            except:
                pass  # Ignore index = 0 (case where >1 value possible for spot)
        else:
            continue
        break  # if break out of internal loop then also break out of outer loop
    return (sanity, reason)   #DEBUG


def all_rows_sane(puzzle):  # Check every row for duplicate single value; If found, the puzzle is invalid
    # Determine row number using integer division (//)
    sanity = True
    reason = "All rows are sane."
    
    full_side = size_of_puzzle_side(puzzle)  # calculate number and length of rows
    for j in range(full_side):  # for each row
        count = reset_count(full_side)  # reset all counters to zero
        for k in range(full_side):  # for every spot in row
            index = convert_list_to_integer(puzzle[j * full_side + k])  # Convert list to single integer index for dictionary 'count'
            try:
                count[index] = count[index] + 1
                if count[index] > 1:
                    sanity = False
                    reason = "Row " + str(j+1) + " is INSANE."
                    break  # exit 
            except:
                pass  # Ignore index = 0 (case where >1 value possible for spot)
        else:
            continue
        break  # if break out of internal loop then also break out of outer loop
    return (sanity, reason)   #DEBUG


def all_grids_sane(puzzle):
    sanity = True
    reason = "All grids are sane."
    full_side = size_of_puzzle_side(puzzle)  # calculate number and length of rows
    part_side = int(full_side ** 0.5)  # Convert to integer for list index

    list_of_internal_grids = create_list_of_internal_grids(part_side)  # Create list of internal grid lists for any size grid

    for list in list_of_internal_grids:
    # first verify that spot is located in the same inner grid 
    # then verify that spot only has a single value
    # then increment the count for that spot value 

        count = reset_count(full_side)  # reset all counters to zero
        for j in range(len(puzzle)):  # for each spot
            if j not in list:
                continue
            else:  # spot is in list
                index = convert_list_to_integer(puzzle[j])  # Convert list to single integer index for dictionary 'count'
                try:
                    count[index] = count[index] + 1
                    if count[index] > 1:
                        sanity = False
                        reason = "Grid with spot " + str(j+1) + " is INSANE."
                        break  # exit 
                except:
                    pass  # Ignore index = 0 (case where >1 value possible for spot)
        else:
            continue
        break  # if break out of internal loop then also break out of outer loop
    return (sanity, reason)   #DEBUG


def check_puzzle_sanity(puzzle):  # Check if solved puzzle is valid/sane
    (row_sanity, row_reason) = all_rows_sane(puzzle) 
    (column_sanity, column_reason) = all_columns_sane(puzzle) 
    (grid_sanity, grid_reason) = all_grids_sane(puzzle) 
    sanity = row_sanity and column_sanity and grid_sanity
    reason = row_reason + " " + column_reason + " " + grid_reason
    return (sanity, reason)


def all_grids_resolved(puzzle):
    resolved = True
    for j in range(len(puzzle)):
        if len(puzzle[j]) > 1:
            resolved = False
    return resolved


def delete_pair_from_row(puzzle, a, b):   # Then delete these two values from all other spots in row
# Delete both values from all the other spots in the row except the two matching spots
    progress = False  # Track whether any values are removed  (default = False = nothing removed)
    side = size_of_puzzle_side(puzzle)  # calculate length of row or column
    correct_row = a // side    # Determine which row to delete values from
    for j in range(len(puzzle)):   # Iterate through all spots
        if j // side != correct_row:
            continue   # Wrong row so skip
        if j == a:
            continue    # skip since cannot delete from self
        if j == b:
            continue    # skip since cannot delete from self
        if puzzle[a][0] in puzzle[j]:
            progress = True
            print("Removing {} from {} in spot {}.".format(puzzle[a][0], puzzle[j], j))   #DEBUG
            puzzle[j].remove(puzzle[a][0])  # Remove first value 
            puzzle[j] = convert_list(puzzle[j])    # Convert list of single list to list of single integer
        if puzzle[a][1] in puzzle[j]:
            progress = True
            print("Removing {} from {} in spot {}.".format(puzzle[a][1], puzzle[j], j))   #DEBUG
            puzzle[j].remove(puzzle[a][1])  # Remove second value 
            puzzle[j] = convert_list(puzzle[j])    # Convert list of single list to list of single integer
    return progress


def delete_pair_from_column(puzzle, a, b):   # Then delete these two values from all other spots in column
# Delete both values from all the other spots in the column except the two matching spots
    progress = False  # Track whether any values are removed  (default = False = nothing removed)
    side = size_of_puzzle_side(puzzle)   # calculate length of row or column
    correct_column = a % side    # Determine which column to delete values from
    for j in range(len(puzzle)):   # Iterate through all spots
        if j % side != correct_column:
            continue   # Wrong column so skip
        if j == a:
            continue    # skip since cannot delete from self
        if j == b:
            continue    # skip since cannot delete from self
        if puzzle[a][0] in puzzle[j]:
            progress = True
            print("Removing {} from {} in spot {}.".format(puzzle[a][0], puzzle[j], j))   #DEBUG
            puzzle[j].remove(puzzle[a][0])  # Remove first value 
            puzzle[j] = convert_list(puzzle[j])    # Convert list of single list to list of single integer
        if puzzle[a][1] in puzzle[j]:
            progress = True
            print("Removing {} from {} in spot {}.".format(puzzle[a][1], puzzle[j], j))   #DEBUG
            puzzle[j].remove(puzzle[a][1])  # Remove second value 
            puzzle[j] = convert_list(puzzle[j])    # Convert list of single list to list of single integer
    return progress


def delete_pair_from_minigrid(puzzle, a, b, list):
    # Delete value from all spots in own inner grid except self
    progress = False
    for j in list:  # Cycle through all spots in minigrid
        if j == a or j == b:
            continue  # Skip since cannot delete self
        if puzzle[a][0] in puzzle[j]:
            progress = True
            puzzle[j].remove(puzzle[a][0])
            puzzle[j] = convert_list(puzzle[j])    # Convert list of single list to list of single integer
        if puzzle[a][1] in puzzle[j]:
            progress = True
            puzzle[j].remove(puzzle[a][1])
            puzzle[j] = convert_list(puzzle[j])    # Convert list of single list to list of single integer
    return progress


def find_pairs(puzzle):  
# If there are two pairs in a column, row or minigrid. 
# One can remove those two numbers from all other spots in that column, row or minigrid.
    full_side = size_of_puzzle_side(puzzle)   # calculate length of row or column
    part_side = size_of_grid_side(puzzle)   # calculate length of grid side
    row_progress = False
    column_progress = False
    minigrid_progress = False
    for j in range(len(puzzle)):
        if len(puzzle[j]) == 2:
            # Match rows
            for k in range(len(puzzle)):
                row = j // full_side
                if j // full_side == k // full_side:  # In same row
                    if j != k:  # Cannot compare self to self
                        if puzzle[j] == puzzle[k]:  # If contents match
#                            print("Spots {} and {} in row {} both have value of {}.".format(j, k, row,  puzzle[j]))
                            row_progress = row_progress or delete_pair_from_row(puzzle, j, k)    # Then delete these two values from all other spots in row # Match column
            for k in range(len(puzzle)):
                column = j % full_side
                if j % full_side == k % full_side:  # In same column
                    if j != k:  # Cannot compare self to self
                        if puzzle[j] == puzzle[k]:  # If contents match
#                            print("Spots {} and {} in column {} both have value of {}.".format(j, k, column,  puzzle[j]))
                            column_progress = column_progress or delete_pair_from_column(puzzle, j, k)  # Delete these two values from all other spots in column
            # Match minigrid
            list_of_internal_grids = create_list_of_internal_grids(part_side)  # Create list of internal grid lists for any size grid
            for list in list_of_internal_grids:
                for k in range(len(puzzle)):
                    if j in list and k in list:
                        if j != k:
                            if puzzle[j] == puzzle[k]:  # If contents match
#                                print("Spots {} and {} in same minigrid both have value of {}.".format(j, k, puzzle[j]))
                                minigrid_progress = minigrid_progress or delete_pair_from_minigrid(puzzle, j, k, list)  # Delete these two values from all other spots in minigrid
    return (row_progress or column_progress or minigrid_progress)  # True if have deleted any values in rows or columns or minigrid


def how_to_continue_when_stalled():  # Prompt user if and how to continue when stalled
    while True:
        print()  # Blank space line
        reply = input("How continue? \n1. Choose puzzle or \n2. Solve puzzle or \n3. Brute force from zero or \n4. Brute force from an input number or \n5. Try guessing a value for a spot and resolve and maybe revert or \n6. Time estimate from zero or \n7. Time estimate spread over 10% increments or\n8. Show puzzle or\n9. Show unknown spots or \n10. Show known spots or \n11. Quit game\nEnter value:  ")
        if reply == "1" or reply == "2" or reply == "3" or reply == "4" or reply == "5" or reply == "6" or reply == "7" or reply == "8" or reply == "9" or reply == "10" or reply == "11":
            reply = int(reply)   # Convert string to integer
            break  # exit loop otherwise prompt again
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

    return (dict_of_pairs, dict_of_pair_locations)


def create_puzzle_with_guess(puzzle, spot_choice, value_choice):
    # Update stalled puzzle with user-selected value 
    original_puzzle = copy.deepcopy(puzzle)
    guess_as_list = []  # Initialize empty list
    guess_as_list.append(value_choice)  # Convert to list
    print("Update puzzle spot {} from {} to {} as {}".format(spot_choice, puzzle[spot_choice], value_choice, guess_as_list))   #DEBUG
    puzzle[spot_choice] = guess_as_list  # Update stalled puzzle with user-selected value 
    return (puzzle, original_puzzle)


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
    return num


def size_of_puzzle(puzzle):
    num = len(puzzle)
    return num


def select_set_of_unknown_values(puzzle, unknown_spots, known_spots, iteration):
    list_of_keys = list(unknown_spots.keys())    # convert dictionary keys to list
    list_of_keys.sort()    # Sort list into ascending order since dictionary is unordered
    list_of_keys.reverse()   # Sort list of keys into descending order
    for j in range(len(list_of_keys)):
        grid_spot_index = iteration % len(unknown_spots[list_of_keys[j]])   # Calculate index into list of possible values
        puzzle[list_of_keys[j]] = unknown_spots[list_of_keys[j]][grid_spot_index]    # Replace list of possible values with single trial value
        iteration = iteration // len(unknown_spots[list_of_keys[j]])
    return puzzle


def create_trial_grid(list, unknown_spots, known_spots, index):
    trial_solution = copy.deepcopy(list)    # start by copying the current list, 
                                    # then cycle through and overwrite the spots with multiple values
                                    # Using 'modulo' and 'remainder' of index value to determine which
                                    # of multiple values to set in each spot of grid
    for j in range(index):   # Cycle through all possible combinations 
        trial_solution = select_set_of_unknown_values(trial_solution, unknown_spots, known_spots, j)
    return trial_solution 


def init_trial_count(puzzle):  # Initialize all row, column and internal grid counts to zero
    num = size_of_puzzle(puzzle)
    count = dict()
    for j in range(num):
        count[j] = 0  # set all grid spot counts to zero
    return count


def quick_check(puzzle):  # Ensure count of each number is correct (not too high or too low)
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
        test_row = puzzle[j * num:(j + 1) * num]   # quickly create using slices
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


def count_internal_grids(puzzle):  # Count how many of each value are in each internal grid
    pass


def test_trial_solution(puzzle):  # Build first possible grid solutions
    result = True
    while result:      # If any tests fail then result will be False
        result = result and quick_check(puzzle)
        result = result and count_rows(puzzle)   
        result = result and count_columns(puzzle)
        result = result and count_internal_grids(puzzle)
    return result


def get_starting_value(number_solutions):
    while True:  # repeat until valid entry
        num = input("Enter starting number: ")
        try:
            num = int(num)    # Convert from string to integer
            if num < 0:
                print("Entered value must be between 0 and {}.".format(number_solutions))
                continue
            if num > number_solutions:
                print("Entered value must be between 0 and {}.".format(number_solutions))
                continue
        except ValueError:
            print("{} is not a valid starting number.".format(num))
        except UnboundLocalError:
            print("Entered value must be between 0 and {}.".format(number_solutions))
        else:
            break
    return  num 


def bruteforce(puzzle, start_num, end_num):   # Try all possible combinations and see which works
    for j in range(start_num, end_num):  # Cycle through all possible values in grids until one works
        trial_solution = create_trial_grid(puzzle, unknown_spots, known_spots, j)
        result = test_trial_solution(trial_solution)
        if result == True:
            print(trial_solution)     #DEBUG
            break   # This is a successful solution 
        else:
            print("Iteration {} did not work.".format(j))
    return trial_solution


def get_time():
    t = time.time()
    return t


def run_time_trial():
    t = 1    # DEBUG   temp value
    return t


def basic_time_trial(puzzle, start_num, end_num):
        start_time = get_time()
        bruteforce(puzzle, start_num, end_num)
        end_time = get_time()
        trial_duration = end_time - start_time
        print()
        print("Trial of {} solutions took {:.2f} seconds.".format(end_num - start_num, trial_duration))
        full_duration_seconds = number_solutions / (end_num - start_num) * trial_duration
        full_duration_hours = full_duration_seconds / 3600
        print("This means that at this rate all {} solutions would need {:.2f} seconds or {:.2f} hours.".format(number_solutions, full_duration_seconds, full_duration_hours))


def advanced_time_trial(puzzle, number_solutions):
        number_of_intervals = 10
        test_values = []   # Initialize 
        interval = number_solutions / number_of_intervals
        interval = int(interval)   # convert to integer from float
        time_sum = 0
        for j in range(1, number_of_intervals + 1):  # Want to test at top of 10% range, not at bottom
            start_time = get_time()
            t = random.randint(0,10)   # DEBUG to generate random time to test calculation of average time
            time.sleep(t)
            end_time = get_time()
            trial_duration = end_time - start_time
            time_sum = time_sum + trial_duration
            print()
            print("Iteration {} of {} solutions took {:.2f} seconds.".format(j, number_of_intervals, trial_duration))
            average_time_in_seconds = time_sum / j   # Calculate average time in seconds
            print("Average of {} iterations is {:.2f} seconds.".format(j, time_sum / j))
            total_time_in_seconds = average_time_in_seconds * interval * number_of_intervals
            total_time_in_hours = total_time_in_seconds / 3600
            total_time_in_days = total_time_in_hours / 24
            print("This means that if all {} solutions are needed it will take {:.2f} seconds or {:.2f} hours or {:.2f} days to solve.".format(number_solutions, total_time_in_seconds, total_time_in_hours, total_time_in_days))


def list_pair_choices(dict_of_pairs):
    # print(dict_of_pairs)
    pass


def list_to_integer(d):  # Convert dictionary value of list of single list to list of integers: ie [[1],[2],[3]] to [1,2,3] 
    new_dict = copy.deepcopy(d)   # Copy dictionary

    for j in new_dict:
        int_list = []    # Initialize empty list
        for k in new_dict[j]:  #Cycle through list of single value list for this dictionary index
            for m in k:
                int_list.append(m)
        new_dict[j] = int_list   # Replace values ie [[1],[2],[3]] with [1,2,3]
    return new_dict


def remove_single_conflicts(puzzle):
# Remove conflicting known single values from same column, same row and same internal grid 
# Start from top left spot and work to bottom right spot in puzzle
    full_side = size_of_puzzle_side(puzzle)  # Determine if puzzle is 9x9 or 16x16
    part_side = size_of_grid_side(puzzle)  # Determine if puzzle grid is 3x3 or 4x4

    for j in range(len(puzzle)):
    # If value of spot is known single value then remove it from matching column, row and inner grid
        if len(puzzle[j]) != 1:
            continue      # skip spot since contains more than one possible value
    
        # Check all other spots in that column and remove conflicts
        puzzle = resolve_column(puzzle, j, full_side)
    
        # Find all single value spots in each row and remove conflicts 
        puzzle = resolve_row(puzzle, j, full_side)
    
        # Now check each inner grid for single value conflicts 
        puzzle = resolve_inner_grid(puzzle, j, part_side)
    
    updated_puzzle = copy.deepcopy(puzzle)    # update puzzle for next while loop iteration
    return updated_puzzle


def get_user_guess(puzzle):  # Check validity of spot and value for user entered guess
    unknown_spots =  get_stalled_spots_list(puzzle)   # Create dict of grid spots that are unknown
    valid_value = False  # setup conditions for while loop
    valid_spot = False
    while not valid_value and not valid_spot:
        (dict_of_spots, dict_of_spot_locations) = count_pairs(puzzle)  # Find unique pairs in stalled puzzle
        list_pair_choices(dict_of_spots)
        integer_list = list_to_integer(unknown_spots)   #DEBUG

        while not valid_spot:
            for j in integer_list:
                print("Spot: {:2d}    List of values: {}.".format(j,integer_list[j]))
            print()  # blank spacer line
            spot_choice = input("Which spot do you want to select?: ")
            try:
                spot_choice = int(spot_choice)  # Only valid values convert to integer
            except:
                pass  # Will prompt for another value
            if spot_choice in integer_list:
                valid_spot = True    # Exit while loop

        while not valid_value:
            print()  # blank line
            print("Spot {} possible values are: ".format(spot_choice), end="")
            l = len(integer_list[spot_choice])
            for j in range(l):
                if j == l - 1:
                    print("{}.".format(integer_list[spot_choice][j]))  # print last value then newline
                else:
                    print("{}, ".format(integer_list[spot_choice][j]), end="")  # print all but last value without newline
            value_choice = input("Enter which value to try: ") 
            try:
                value_choice = int(value_choice)  # Only valid inputs convert to integer
            except:
                pass   # Will prompt for another input
            if value_choice in integer_list[spot_choice]:
                valid_value = True    # Exit while loop
    return (spot_choice, value_choice)


def solve_puzzle(puzzle):
    loop = 0
    done = False
    full_side = size_of_puzzle_side(puzzle)  # Determine if puzzle is 9x9 or 16x16
    part_side = size_of_grid_side(puzzle)  # Determine if puzzle grid is 3x3 or 4x4
    last_count = 1000
    
    while not done:
        print()
        print ("Loop count= {}".format(loop))
        
        count = count_total_possible_values(puzzle)   # Count all the known and unknown values in the puzzle
        print("Total values count in the puzzle is {}.".format(count_total_possible_values(puzzle)))
    
        cw = column_width(puzzle)  # Determine largest possible list in each column so can print column that width
        print("Column widths are: {}".format(cw))    #DEBUG
    
        puzzle = remove_single_conflicts(puzzle)  # Remove conflicting known single values from same column, 
                                                 # row and internal grid 
        
        loop = loop + 1  # Increment iteration loop counter                            
    
        column_max = column_width(puzzle)    #DEBUG
    
        show_adjustable_grid_lines(puzzle, full_side, ROW_SEP, COL_SEP, column_max)    #DEBUG 
    
        current_count = list_count(puzzle)
       
        progress = find_pairs(puzzle)  

        if progress:  # reset loop and count values so looping continues
            loop = 0
            last_count = 100000
    
        (done, reason) = are_we_done(puzzle, loop, last_count)
    
        last_count = current_count
    else:
        unknown_spots =  get_stalled_spots_list(puzzle)   # Create list of grid spots that are still unknown
        num_unknown_spots = len(unknown_spots)   # Count number of unknown spots in grid
        number_solutions = get_number_possible_solutions(unknown_spots)
        print()  # Blank line
        print("Game status: {}".format(reason))
        print("Number of possible brute force solutions is: {} over {} unknown spots".format(number_solutions, num_unknown_spots))
        print()  # Blank line
        progress = find_pairs(puzzle)  
    return (reason, puzzle)


def select_spot_and_values(puzzle):  # Check validity of spot and value to update puzzle 
    unknown_spots =  get_stalled_spots_list(puzzle)   # Create list of grid spots that are unknown
    valid_value = False  # setup conditions for while loop
    valid_spot = False
    while not valid_value and not valid_spot:
        (dict_of_spots, dict_of_spot_locations) = count_pairs(puzzle)  # Find unique pairs in stalled puzzle
        list_pair_choices(dict_of_spots)
        integer_list = list_to_integer(unknown_spots)   #DEBUG

        while not valid_spot:
            for j in integer_list:
                print("Spot: {:2d}    List of values: {}.".format(j,integer_list[j]))
            print()  # blank spacer line
            spot_choice = input("Which spot do you want to edit?: ")
            try:
                spot_choice = int(spot_choice)  # Only valid values convert to integer
            except:
                pass  # Will prompt for another value
            if spot_choice in integer_list:
                valid_spot = True    # Exit while loop

        while not valid_value:
            print()  # blank line
            print("Spot {} possible values are: ".format(spot_choice), end="")
            l = len(integer_list[spot_choice])
            for j in range(l):
                if j == l - 1:
                    print("{}.".format(integer_list[spot_choice][j]))  # print last value then newline
                else:
                    print("{}, ".format(integer_list[spot_choice][j]), end="")  # print all but last value without newline
            values_choice = input("Enter which value to try: ") 
            try:
                values_choice = int(values_choice)  # Only valid inputs convert to integer
                print("Values choice entered is: {}".format(values_choice))   #DEBUG
            except:
                pass   # Will prompt for another input
            if values_choice in integer_list[spot_choice]:
                valid_value = True    # Exit while loop
                print("Value {} in {}".format(values_choice, integer_list[spot_choice]))  #DEBUG
            else:  #DEBUG
                print("Value {} not in {}".format(values_choice, integer_list[spot_choice]))  #DEBUG

    return (spot_choice, values_choice)


def flat_print_unknown_spots(puzzle):   # List spots is a few lines instead of one per line
    unknown_spots =  get_stalled_spots_list(puzzle)   # Create dict of grid spots that are still unknown
    unknown_spots_keys = list(unknown_spots.keys())  # Convert dict to list for both keys and values
    unknown_spots_values = list(unknown_spots.values())  # Convert dict to list for both keys and values
    print()  # Blank line as spacer
    print("Unknown Spots are ", end = "")  
    for j in range(len(unknown_spots) - 1):  
        print("{}:{},  ".format(unknown_spots_keys[j], unknown_spots_values[j]), end = "")
    print("{}:{}.".format(unknown_spots_keys[j+1], unknown_spots_values[j+1]))  # Print last value followed by "."
        

def show_known_spots(puzzle):  # Only show known spots; leave unknown spots blank
    column_max = 3  # Since only show known values, this value should be set to 3
    # Need to keep only the known/single values and ignore the others
    print(puzzle)
#    show_adjustable_grid_lines(puzzle, full_side, ROW_SEP, COL_SEP, column_max)   


def main():
    # Initialize variables
    last_count = HUGE_VALUE
    
    greet_user() 
            
    while True:  # Loop until break
        reply = how_to_continue_when_stalled()  # Prompt user if and how to continue when stalled
            
        if reply == 1:  # Choose puzzle
            puzzle = select_puzzle()
            full_side = size_of_puzzle_side(puzzle)  # Determine if puzzle is 9x9 or 16x16
            part_side = size_of_grid_side(puzzle)  # Determine if puzzle grid is 3x3 or 4x4
            
            values = all_values(full_side)  # Determine all possible values for each spot (1..9 or 1..16)

            puzzle = setup_possibles_list(puzzle, values)
            print()
            
        if reply == 2:  # Solve puzzle
            try:
                (reason, puzzle) = solve_puzzle(puzzle)
            except UnboundLocalError:
                print()  # Blank space line
                print("You must select a puzzle before trying to solve it!") 
            else:
                print()
                print()
                print("***************** Final puzzle result is: ********************")
                column_max = column_width(puzzle)    #DEBUG
                show_adjustable_grid_lines(puzzle, full_side, ROW_SEP, COL_SEP, column_max)    #DEBUG 
                    
                count = count_total_possible_values(puzzle)   # Count all the known and unknown values in the puzzle
                print("Total values count in the puzzle is {}.".format(count_total_possible_values(puzzle)))
                if count > len(puzzle):  # Decide how to proceed if there are still unresolved grids
                    print()
                    print("There are still unresolved grids.")
                    unknown_spots =  get_stalled_spots_list(puzzle)   # Create list of grid spots that are still unknown
                    num_unknown_spots = len(unknown_spots)   # Count number of unknown spots in grid
                    known_spots = get_known_spots_list(puzzle)  # List of known spots
                    number_solutions = get_number_possible_solutions(unknown_spots)
                    print()
                    print("Number of possible brute force solutions is: {} over {} unknown spots".format(number_solutions, num_unknown_spots))
                else:
                    print("All grids resolved.")
                    (sane, reason) = check_puzzle_sanity(puzzle)  # Check if solved puzzle is valid/sane
                    print("Puzzle sanity is {} because: {}".format(sane, reason))
                    if not sane:
                        print("So selecting value {} for spot {} was not correct.".format(spot_choice, value_choice))

        if reply == 3:  # Brute force solution starting from zero
            successful_solution = bruteforce(puzzle, 0, number_solutions)
    
        if reply == 4:  # Brute force solution starting from entered value (allows continuation)
            begin_num  = get_starting_value(number_solutions)
            successful_solution = bruteforce(puzzle, begin_num, number_solutions)
    
        if reply == 5:  # Try guessing a spot and solving and revert if insane
            (spot_choice, value_choice) = get_user_guess(puzzle) 
            (puzzle, original_puzzle) = create_puzzle_with_guess(puzzle, spot_choice, value_choice)    # Update puzzle with guess   ##DEBUG
            (reason, puzzle) = solve_puzzle(puzzle)
            (sane, reason) = check_puzzle_sanity(puzzle)  # Check if solved puzzle is valid/sane
            print("Puzzle sanity is {} because: {}".format(sane, reason))
            if not sane:
                print("So selecting value {} for spot {} was not correct.".format(spot_choice, value_choice))
                while True:
                    revert = input("Do you want to revert to puzzle before guess? Enter Y/N.")
                    if revert == "Y":
                        puzzle = original_puzzle  # Replace insane puzzle with original (pre-guess) puzzle
                        break
                    if revert == "N":
                        break  # Keep insane puzzle with guess
                    else:
                        continue  # Prompt again to revert puzzle or not
        
        if reply == 6:   # Time trial for 1000 attempts, then calculate worst case if all possibilities needed
            start_num = 0
            end_num = 1000
            basic_time_trial(puzzle, start_num, end_num)
    
        if reply == 7:   # Time trial spread over ten 10% ranges assuming a huge number
                         # since single evaluation at 10,000,000 takes multiple minutes
                         # whereas starting from zero does several evaluations per second
                         # and gives an unrealistic "quick" solution
            number_of_intervals = 10
            advanced_time_trial(puzzle, number_solutions)
    
        if reply == 8:  # Show puzzle
            column_max = column_width(puzzle)    #DEBUG
            show_adjustable_grid_lines(puzzle, full_side, ROW_SEP, COL_SEP, column_max)    #DEBUG 

        if reply == 9:  # Show unknown spots
            flat_print_unknown_spots(puzzle)  # List spots is a few lines instead of one per line

        if reply == 10:  # Show known spots
            column_max = column_width(puzzle)    #DEBUG
            show_adjustable_grid_lines(puzzle, full_side, ROW_SEP, COL_SEP, column_max)    #DEBUG 
            show_known_spots(puzzle)  # List spots is a few lines instead of one per line

        if reply == 11:  # Quit game
            break

# Main code
if __name__ == "__main__":
    main()
