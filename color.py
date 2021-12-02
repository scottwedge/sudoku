#!/usr/bin/env python3

# Experiment with colour and flashing text using colored module

# First install colored using pip with "pip install termcolor"

# Then import with "from termcolor import colored"


# Imports
from termcolor import colored
text1 = colored("Hello", "red", "on_yellow", attrs=["blink", "bold"])
text2 = "world"
print (text1, text2)
