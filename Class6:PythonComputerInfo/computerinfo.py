# Script Name: computerinfo.py
# Author: Devin Iverson
# Date of last revision: 05/2/22
# Purpose: Print information about the computer to the screen
# Variables: whoami, ip_a, lshw, spacer

import subprocess as sp

# variables
whoami = sp.getoutput('whoami --version')
ip_a = sp.getoutput('ip a')
lshw = sp.getoutput('lshw -short')
spacer = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

print(whoami)
print(spacer)
print(ip_a)
print(spacer)
print(lshw)