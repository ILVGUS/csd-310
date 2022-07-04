# Jennifer Adams
# CYBR410-T301
# July 3, 2022
# Objective: Display student documents from students collection

from pymongo import MongoClient

# Connection string from MongoDB Atlas
url="mongodb+srv://admin:admin@cluster0.olwht.mongodb.net/pytech";

# Variable used to connect to MongoDB cluster
client = MongoClient(url)

# Variable specifying connection to pytech database
db = client.pytech

# Variable specifying students collection
students = db.students

# Variable for finding all students
list_students = db.students.find({})

# Introduce results from using the find method
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Iterate through available documents in the collection "students"
for doc in list_students:
    
    # Display Student ID, First Name, and Last Name using the corresponding entries in the documents
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")

# Introduce results from using the find_one method
print("\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

# Assign variable for one specific student matching student_id 1007
one_student = db.students.find_one({"student_id": "1007"})

# Display Student ID, First Name, and Last Name using the corresponding entry in the collection
print("Student ID: " + one_student["student_id"] + "\nFirst Name: " + one_student["first_name"] + "\nLast Name: " + one_student["last_name"] + "\n")

# Collect input from user after program has ended
input("\nEnd of program, press any key to continue. . .")


