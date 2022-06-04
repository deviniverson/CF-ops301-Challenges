#!/usr/bin/env python3

# File Name: HttpRequest.py
# Author: Devin Iverson
# Date: 06/02/2022
# Purpose: 

from pip._vendor import requests

# response = requests.get('https://api.github.com')
menu_list = ["Null", "GET", "POST", "PUT", "Delete", "HEAD", "PATCH", "OPTIONS"]


# user input of url
url = input("Enter Destination URL: ")

# http methods menu
def menu():
    print("* MAIN MENU *\n")
    print("-------------\n")
    print("1. GET\n")
    print("2. POST\n")
    print("3. PUT\n")
    print("4. DELETE\n")
    print("5. HEAD\n")
    print("6. PATCH\n")
    print("7. OPTIONS\n")
    print("8. QUIT\n")
    print("-------------\n")
    menu_input = input("Enter Menu Selection: ")
    
    if menu_input == "1":
        txt = "You are requesting to use http method {0} for URL {1}. "
        print(txt.format(menu_list[1], url))
        answer = input("Do you want to continue with this request? (yes or no):  ")
        if answer == "yes":
            response = requests.get(url)
            code = response.status_code
            translate_code(code)
        else:
            exit
    elif menu_input == "2":
        txt = "You are requesting to use http method {0} for URL {1}. "
        print(txt.format(menu_list[2], url))
        answer = input("Do you want to continue with this request? (yes or no):  ")
        if answer == "yes":
            response = requests.post(url)
            code = response.status_code
            translate_code(code)
        else:
            exit    
    elif menu_input == "3":
        txt = "You are requesting to use http method {0} for URL {1}. "
        print(txt.format(menu_list[3], url))        
        answer = input("Do you want to continue with this request? (yes or no):  ")
        if answer == "yes":
            response = requests.put(url)
            code = response.status_code
            translate_code(code)
        else:
            exit    
    elif menu_input == "4":
        txt = "You are requesting to use http method {0} for URL {1}. "
        print(txt.format(menu_list[4], url))        
        answer = input("Do you want to continue with this request? (yes or no):  ")
        if answer == "yes":
            response = requests.delete(url)
            code = response.status_code
            translate_code(code)
        else:
            exit    
    elif menu_input == "5":
        txt = "You are requesting to use http method {0} for URL {1}. "
        print(txt.format(menu_list[5], url))        
        answer = input("Do you want to continue with this request? (yes or no):  ")
        if answer == "yes":
            response = requests.head(url)
            code = response.status_code
            translate_code(code)
        else:
            exit    
    elif menu_input == "6":
        txt = "You are requesting to use http method {0} for URL {1}. "
        print(txt.format(menu_list[6], url))        
        answer = input("Do you want to continue with this request? (yes or no):  ")
        if answer == "yes":
            response = requests.patch(url)
            code = response.status_code
            translate_code(code)
        else:
            exit    
    elif menu_input == "7":
        txt = "You are requesting to use http method {0} for URL {1}. "
        print(txt.format(menu_list[7], url))        
        answer = input("Do you want to continue with this request? (yes or no):  ")
        if answer == "yes":
            response = requests.options(url)
            code = response.status_code
            translate_code(code)
        else:
            exit
    elif menu_input == "8":
        print("Exiting script.")
        exit
    
# print response for url to screen
def translate_code(x):
    if x == 404:
        print("Site Not Found")
    elif x == 200:
        print("Successful")

# main function
menu()