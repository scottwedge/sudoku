#!/usr/bin/env python3
# Recursive program

# Constants
MAX = 10

# Functions
def print_first_in_list(list):
    try:
        print(list[0])
    except IndexError:
        pass
    else:
        l.pop(0)
        print_first_in_list(list)  # Recursive call to self 


# Main code
l = list()

for j in range(MAX):
    l.append(j)  # Create list

print_first_in_list(l)
