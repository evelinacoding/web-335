/**
	Title: zepeda-aggregate-queries.js
    Author: Evelyn Zepeda
    Date: 2/13/24
    Description: MongoDB Shell Scripts for houses.js
 */

//To load houses.js
load('houses.js')

//Write a query to list the documents in the houses collection
db.houses.find()

//Write a query to show a list of documents in the students collection
db.students.find()

//Write a query to add a document in the students collection
db.students.insertOne({'firstName':'John', 'lastName':'Johnson', 'studentId':'s1019', 'houseID':'1009'})

//Write a query to delete the student
db.students.deleteOne({'studentId':'s1019'})

//Write a query to show a list of students by house
db.houses.aggregate([{$lookup: {from: "students", localField: "houseId", foreignField: "houseId", as: "house"}}])

//Write a query to show a list of students at house Gryffindor
db.students.aggregate([{$match: {houseId:'h1007'}}, {$lookup: {from: 'students', localField:'houseId', foreignField: 'houseId', as: 'students'}}])

//Write a query to show the students who chose the eagle mascot
db.houses.aggregate([{$match: {mascot: 'Eagle'}}, {$lookup: {from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'students'}}])