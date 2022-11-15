/**
==============================================
; Title: Assignment 5.2 projections.js
; Author: Chad ONeal
; Date: 11/15/2022
; Description: projections.js 
==============================================
*/

// Connection String
// mongosh "mongodb+srv://bellevueuniversity.ox0t9kr.mongodb.net/web335DB" --apiVersion 1 --username web335_user

// Loads users.js file
load('users.js');

// insert new document to users collection
db.users.insertOne({firstName: "Brad", lastName: "Craig", employeeId: "1007", email: "bcraig@me.com"})

// update mozart user's email address to mozart@me.com
db.users.updateOne({lastName: "mozart"}, {$set:{email: "mozart@me.com"}})

// display mozart document to confirm updated email
db.users.findOne({lastName: "Mozart"})

// list all documents in the users collection using projection to only display firstName, lastName, and email fields
db.users.aggregate([{$project: {firstName: 1, lastName: 1, email:1 }}])