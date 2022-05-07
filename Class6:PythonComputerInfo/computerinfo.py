# Script Name: computerinfo.py
# Author: Devin Iverson
# Date of last revision: 05/2/22
# Purpose: Print information about the computer to the screen
# Variables: whoami, ip_a, lshw

import os
#from subprocess import *

paywall = 0

for i in range(5):
    print("Main Menu")
    user = input("Are you a Paying customer or not?")
    #lower_user = user.casefold()
    if user == "yes":
        print("\n")
        paywall += 1
        break
    else:
        print("It's never to late to become one!   ")
        print("\n")

if paywall == 1:
    #whoami = call("whoami", shell=True)
    who = os.system("whoami")
    print(who)
    ip = os.system(["ip a"])
    print(ip)
    lshw = os.system(["lshw -short"])
    print(lshw)
else:
    pass