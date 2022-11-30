""" 
Title: Assignment 7.3 oneal_usersp2
Author: Chad ONeal
Date: 11/28/2022
Description: Python with MongoDB part 2
"""

# import the MongoClient 
from pymongo import MongoClient
from datetime import datetime

# connection to MongoDB 
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.ox0t9kr.mongodb.net/web335DB")

# variable to access web335DB
db = client['web335DB']

# create new user document
newUserDoc = {
    "firstName": "Jay",
    "lastName": "Phillips",
    "employeeId": "2002",
    "email": "jphillips@me.com",
    "dateCreated": datetime.utcnow()
}

# insert new user into database
db.users.insert_one(newUserDoc)

# print newly added document
print(db.users.find_one( { "employeeId": "2002" } ))

# update newly added document's email field
db.users.update_one(
    { "employeeId": "2002" },
    {    "$set": {
            "email": "phillipsjay@me.com"
        }
    }
)

# print updated document 
print(db.users.find_one( { "employeeId": "2022" } ))

# delete the new document from the database
db.users.delete_one( { "employeeId": "2022" } )

# try finding deleted document to check that it was deleted
print(db.users.find_one( { "employeeId": "2022" } ))