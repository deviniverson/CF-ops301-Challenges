#!/bin/bash

# Script:                       Ops 301 Ops Chall 03
# Author:                       Devin Iverson
# Date of latest revision:      04/25/2022
# Purpose: Bash Script to change permissions of a directory provided from user

# User prompts
read -p 'Name of Target Directory: ' target

# define path by searching for target directory
path=$(find $HOME -type d -name $target 2>/dev/null)

# show directory before changes are made
echo " "
echo "Permissions of Directory $target before changes:"
ls -al $path

echo " "
echo "Three Digit Permission Code Explanation: "

echo " " 
# Digit Permission code representation tables
echo "Digit   Permission  Representation 
0 No_Permission ---
1 Execute --x
2 Write -w-
3 Write+Execute -wx
4 Read r--
5 Read+Execute r-x
6 Read+Write rw-
7 Read+Write+Execute rwx
" | column -t

echo " "
echo "# # #
User Group Everyone_Else
" | column -t 

echo " "
read -p 'Enter Three Digit Permission Code: ' perm

# change permission of directory
chmod -R $perm $path

# show directory after changes are made
echo "Permissions of Directory $target after changes:"
ls -al $path
