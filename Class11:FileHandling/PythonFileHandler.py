#!/usr/bin/env python3

# File Name: PythonFileHandler.py
# Author: Devin Iverson
# Date: 05/23/2022
# Purpose: Python script that creates .txt file, appends lines of text, displays contents of file to screen then deletes the file.
import os

def create_file():
    # Create .txt file
    file = open("newfile.txt", "w")
    file.close() # close file to change file access mode

def append_lines():
    # Appends three lines to file
    file = open("newfile.txt", "a")
    file.write("This is line one \n")
    file.write("This is line two \n")
    file.write("This is line three \n")
    file.close() # close file to change file access mode

def print_first():
    # prints to the screen the first line
    file = open("newfile.txt", "r+")
    print(file.readline())
    file.close() # close file to change file access mode

def delete_file():
    # deletes the .txt file
    os.remove("newfile.txt")

def print_file():
    # prints to screen the whole file to show changes
    file = open("newfile.txt", "r+")
    print(file.read())

# main
create_file()

print_file()

append_lines()

print_file()

print_first()

delete_file()

