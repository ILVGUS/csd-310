# Jennifer Adams
# CYBR410-T301
# July 2, 2022
# Objective: Follow steps in Python: MongoDB Connection Example
# to show the "students" collection in Python.

# Import information
from pymongo import MongoClient

# Connection string from MongoDB Atlas
url="mongodb+srv://admin:admin@cluster0.olwht.mongodb.net/pytech";

# Variable used to connect to MongoDB cluster
client = MongoClient(url)

# Variable specifying connection to pytech database
db=client.pytech

# Print command to label Pytech Collection List
print("\n -- Pytech Collection List --")

# Print command to show collections inside pytech
print(db.list_collection_names())

# Input to accept any key to continue
input ("\n\nEnd of program, press any key to exit. . .")


