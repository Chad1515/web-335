""" 
Title: Assignment 5.3 oneal-hobbies.js
Author: Chad ONeal
Date: 11/15/2022
Description: Python Conditionals/Lists/Loops assignment for WEB 335
"""
# list of hobbies
hobbies = ["hunting", "fishing", "camping", "hiking", "biking"]

# print each hobby to console
for hobby in hobbies:
    print(hobby)

# list of days of the week 
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# print message for the corresponding day of the week
for day in days:
    if day == "Sunday" or day == "Saturday":
        print("Today you are off.  Go enjoy your hobbies! It is: " + day)
    else:
        print("Today is a work day. Better work Hard! It is: " + day)

# enjoy message
input("Enjoy!")