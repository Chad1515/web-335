""" 
Title: Assignment 5.3 oneal-hobbies.js
Author: Chad ONeal
Date: 11/15/2022
Description: Python Conditionals/Lists/Loops assignment for WEB 335
"""

hobbies = ["hunting", "fishing", "camping", "hiking", "biking"]

for hobby in hobbies:
    print(hobby)

days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

for day in days:
    if day == "sunday" or day == "saturday":
        print("Today you are off. It is: " + day)
    else:
        print("Today is a work day. It is: " + day)

input("Enjoy!")