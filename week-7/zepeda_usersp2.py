#	Title: zepeda-usersp2.py
#   Author: Evelyn Zepeda
#   Date: 2/25/24
#   Description: A python exercise.

#To import MongoClient from pymongo
from pymongo import MongoClient
from datetime import datetime
 #A string ot connect to the database
conn = "mongodb+srv://web335_user:s3cret@bellevueuniversity.8vzftv7.mongodb.net/web335DBretryWrites=true&w=majority"

#To create a client
client = MongoClient(conn,tls=True,tlsAllowInvalidCertificates=True)

#Creating a variable to access the collection
db = client['web335DB']

#Creating the new user document
chopin = {
    "firstName" : "Frederic",
    "lastName" : "Chopin",
    "employeeId": "1014",
    "email": "fchopin@me.com",
    "dateCreated": datetime.now()
}


#Adding the document to the database
new_User = db.users.insert_one(chopin)

print(new_User.inserted_id)

#To display the new document
find_Chopin = db.users.find_one({"_id": new_User.inserted_id})
print(find_Chopin)

#To update the email address
db.users.update_one({"_id": new_User.inserted_id}, {"$set": {"email": "chopin@me.com"}})

#To print the updated document
updated_newUser = db.users.find_one({"_id": new_User.inserted_id})
print(updated_newUser)

#To delete the document
db.users.delete_one({"_id": new_User.inserted_id})

#To prove the document was deleted
deleted_user = db.users.find_one({"_id": new_User.inserted_id})
print(deleted_user)