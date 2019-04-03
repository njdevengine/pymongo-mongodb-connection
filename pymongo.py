import pymongo

#mongo always runs on 27017
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
print(client)

# make a database called classDB
db = client.classDB

db.classroom.insert_one({"Name":"Seth",
                        "Row":3,
                        "Favorite Code":"bins"})
