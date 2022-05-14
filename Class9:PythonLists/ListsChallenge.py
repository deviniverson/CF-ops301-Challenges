#!/usr/bin/env python3

# File Name: ListsChallenge.py
# Author: Devin Iverson
# Date: 05/13/22
# Purpose:

# list of friends

friends = ["Kevin", "Sue", "Brad", "Chad", "Scott", "Blake", "Karen", "John", "Ian", "George", "Sue"]
print("Original List of Friends: ")
print(friends)

# prints the 4th element of the list
print("Print the 4th element: ")
print(friends[5])

# prints elements 6th through 10th, ":" means to the end of list
print("Print elements 6th through 10th: ")
print(friends[5:])

# change the 7th element to be "onion"
print("Change 7th element to 'Onion': ")
friends[6] = "Onion"
print(friends)

# Stretch Goals:

# use append() method: adds an element at the end of the list
print("Add 'Drew' to end of list: ")
friends.append("Drew")
print(friends)

# use copy() method: returns a copy of the list
print("Return a copy of the list: ")
copy = friends.copy()
print(copy)

# use count() method: returns the number of elements with the specific value
print("Print number of times 'Kevin' is in the list: ")
x = friends.count("Kevin")
print(x)

# use extend() method: add the elements of a list to the end of the current list
print("Add a list of elements to the end of the Friends list: ")
cars = ["Ford", "BMW", "Volvo"]
friends.extend(cars)
print(friends)

# use index() method: returns the index of the first element with the specific value
print("Find the index of element 'John': ")
whereis = friends.index("John")
print(whereis)

# use insert() method: adds an element at the specified position
print("Add 'apple' at position 1: ")
friends.insert(1, "apple")
print(friends)

# use pop() method: removes the element at the specified position
print("Remove element at position 1: ")
friends.pop(1)
print(friends)

# use remove() method: removes the first item with the specified value
print("Remove first item that matches 'Sue': ")
friends.remove("Sue")
print(friends)

# use reverse() method: reverses the order of the list
print("Reverse order of list: ")
friends.reverse()
print(friends)

# use sort() method: sorts the list
print("Sort the list: ")
friends.sort()
print(friends)

# use clear() method: removes all the elements from the list
print("Remove all elements: ")
friends.clear()
print(friends)

# create tuple: Tuple items are indexed starting with [0],
# ordered in terms of location and can not be changed,
# unchangeable as can not change elements, add or remove elements, and
# allows duplicates as tuples are indexed, they can have items with the same value.
print("Print tuple: ")
mytuple = ("apple", "banana", "cherry")
print(mytuple)

# create set: a collection which is unordered, unchangeable(set items can not change, but you can remove items and add new items), and unindexed. No duplicate members
print("Print set: ")
myset = {"apple", "banana", "cherry"}
print(myset)

# create dictionary: used to store data values in key:value pairs.
# Dictionary is a collection which is ordered, changeable and do not allow duplicates
print("Print dictionary: ")
thisdict = {"brand": "Subaru", "model": "CrossTrek", "year": "2022"}
print(thisdict)