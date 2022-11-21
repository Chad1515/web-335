""" 
Title: Assignment 6.3 oneal_usersp1
Author: Chad ONeal
Date: 11/21/2022
Description: Python with MongoDB part 1
"""

# import the MongoClient 
from pymongo import MongoClient

# connection to MongoDB 
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.ox0t9kr.mongodb.net/web335DB")

# variable to access web335DB
db = client['web335DB']

# print all documents in users collection
for user in db.users.find():
  print(user)

# print user document with employeeId equal to 1011
print(db.users.find_one( { "employeeId": "1011" } ))  

# print user document with lastName Mozart
print(db.users.find_one( { "lastName": "Mozart" } ))
