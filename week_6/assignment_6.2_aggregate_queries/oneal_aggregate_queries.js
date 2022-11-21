/**
==============================================
; Title: oneal_assignment_6.2_aggregate_queries
; Author: Chad ONeal
; Date: 11/21/2022
; Description: MongoDB Shell Scripts for the houses and students collections
============================================================================
*/

// Connection String
// mongosh "mongodb+srv://bellevueuniversity.ox0t9kr.mongodb.net/web335DB" --apiVersion 1 --username web335_user

// display all documents in houses
db.houses.find()

// display all documents in students
db.students.find()

// add a document to students collection
db.students.insertOne({firstName: "Hermione", lastName: "Granger", studentId: "s1013", houseId: "h1007"})

// verify student "Hermione Granger" has been added
db.students.findOne({lastName: "Granger"})

// delete student document added in last steps
db.students.deleteOne({studentId: "s1013"})

// verify student document deleted no longer exists in collection
db.students.findOne({lastName: "Granger"})

// list students by house
db.houses.aggregate([{$lookup:{from: "students", localField: "houseId", foreignField: "houseId", as:"house_students"}}])

// list students in Gryffindor 
db.houses.aggregate([{$match: { "houseId": "h1007"}}, {$lookup: {from: "students", localField: "houseId", foreignField: "houseId", as: "house_students"}}])

// list students in house with eagle mascot 
db.houses.aggregate([{ $match: {"mascot": "Eagle"}}, {$lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "mascot_students"}}])

 

