/**
	Title: zepeda-projections.js
    Author: Professor Krasso
    Date: 2/10/24
    Description: MongoDB Projections
 */


//Finds all the users
db.users.find()

//To insert a new user(a new user should be defined first using user={""})
db.users.insertOne(user)

//To update the email address
db.users.updateOne({"email":"wmozart@me.com"}, {$set: {"email":"mozart@me.com"}})

//To use projections in order to find specific fields
db.users.aggregate({$project: {"firstName":1, "lastName":1, "email":1}})