#!/usr/bin/env python3

# File Name: conditionalpython.py
# Author: Devin Iverson
# Date: 05/13/2022
# Purpose: Practice using logical conditionals with Python3.

testlists = [[1, 1], [1, 5], [7, 5], ["a", "a"], ["c", "z"]]

def EqualConditionals(a, b):
    if a == b: # Equals: a == b
        Equal = "{0} equals {1}"
        print(Equal.format(a, b))


    elif a != b: # Not Equals: a != b
        NotEqual = "{0} does not equal {1}, "
        print(NotEqual.format(a, b))
        GreaterLesser(a, b)

    else:
        error = "{0} and {1} are not the same data type"
        print("error.format(a,b)")

def GreaterLesser(c,d):
    if c < d: # Less than: c < d
        Less = "{0} is less than {1}"
        print(Less.format(c, d))

    elif c > d: # Greater than: c > d
        Greater = "{0} is greater than {1}"
        print(Greater.format(c, d))

def GreatLessEqual(e, f):
    if e <= f: # Less than or equal to: e <= f
        LessEqual = "{0} is less than or equal to {1}"
        print(LessEqual.format(e, f))

    elif e >= f: # Greater than or equal to: e >= f
        GreaterEqual = "{0} is greater than or equal to {1}"
        print(GreaterEqual.format(e, f))

    else: # else used incase other options are not met
        error = "{0} and {1} are not the same data type"
        print(error.format(e, f))

for testlist in testlists:
    #x, y = [testlist[0], testlist[1]]
    EqualConditionals(testlist[0], testlist[1])

for testlist in testlists:
        GreatLessEqual(testlist[0], testlist[1])
