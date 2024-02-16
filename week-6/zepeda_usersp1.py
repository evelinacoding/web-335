#	Title: zepeda-usersp1.py
#   Author: Evelyn Zepeda
#   Date: 2/14/24
#   Description: A python exercise.

#To import MongoClient from pymongo
from pymongo import MongoClient

#A string to connect to the database
conn = "mongodb+srv://web335_user:s3cret@bellevueuniversity.8vzftv7.mongodb.net/web335DBretryWrites=true&w=majority"

#To create a client
client = MongoClient(conn,tls=True,tlsAllowInvalidCertificates=True)

#Creating a variable to access the collection
db = client['web335DB']

#Display all documents in the users collection
for user in db.users.find({}):
  print(user)

#Display a document for a specific employeeId
print(db.users.find_one({"employeeId":"1011"}))

#Display a document for a specific last name
print(db.users.find_one({"lastName":"Mozart"}))