/**
==============================================
; Title: oneal_exercise_4.3_mongodb_shell
; Author: Professor Richard Krasso
; Modified by: Chad ONeal
; Date: 11/10/2022
; Description: MongoDB Shell Scripts for the users collection
==============================================
*/

// Connection String
// mongosh "mongodb+srv://bellevueuniversity.ox0t9kr.mongodb.net/web335DB" --apiVersion 1 --username web335_user

//Loads the users file
load('users.js');

// Query to find users
db.users.find();

// Query to find users by email
db.users.find({ email: 'jbach@me.com'});

// Query to find users by last name
db.users.find({ lastName: 'Mozart' });

// Query to find users by first Name
db.users.find({ firstName: 'Richard' });

// Query to find users by employeeId
db.users.find({ employeeId: '1010' });