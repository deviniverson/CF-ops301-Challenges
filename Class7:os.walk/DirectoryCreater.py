#!/usr/bin/env python3

# File Name: DirectoryCreater.py
# Author: Devin Iverson
# Date: 05/05/2022
# Purpose: 

# Import libraries

import os

# Declaration of variables

### Read user input here into a variable
input = input("Enter directory: ")
# Declaration of functions

### Declare a function here
def file_paths(input):
    for (root, dirs, files) in os.walk(input):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

# Main

### Pass the variable into the function here

# End