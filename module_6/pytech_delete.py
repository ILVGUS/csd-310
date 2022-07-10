# Jennifer Adams
# CYBR410-T301
# July 10, 2022
# Objective: Display student documents from students collection, add one student_id, delete that student_id,
# then display student documents again.

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

jane = {
    "student_id": "1010",
    "first_name": "Jane",
    "last_name": "Doe",
    "enrollment": [{
        "term": "Spring",
        "gpa": "2.5",
        "start_date": "March 20, 2022",
        "end_date": "June 20, 2022",
        "course": [{
            "course_id": "BSIT440",
            "description": "Microsoft Windows Server Mgmt",
            "instructor": "Prof. William Cox",
            "grade": "A"
        },
        {        
            "course_id": "CYBR410",
            "description": "Data/Database Security",
            "instructor": "Prof. Peter Haas",
            "grade": "A-"
        }]
    }]
}
# Introduce results from insert_one method
print("\n-- INSERT STATEMENTS --")

# Inserting student Jane Doe
jane_student_id = students.insert_one(jane).inserted_id

# Print result
print("Inserted student record into the students collection with document_id " + str(jane_student_id))

# Introduce results from find_one for student_id 1010
print("\n-- DISPLAYING STUDENT TEST DOC --")

# Use the find_one method to locate the test doc, student_id 1010
one_student = db.students.find_one({"student_id": "1010"})

# Print the student_id, first_name, and last_name for student_id 1010
print("Student ID: " + one_student["student_id"] + "\nFirst Name: " + one_student["first_name"] + "\nLast Name: " + one_student["last_name"] + "\n")

# Assign variable to student_id to be removed
remove_student_id = {"student_id": "1010"}

# Delete the record from the collection
students.delete_one(remove_student_id)

# Introduce the list of all student_ids currently in the students collection
print("\n\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

new_list_students = db.students.find({})
# Iterate through available documents in the collection "students"
for doc in new_list_students:
    
    # Display Student ID, First Name, and Last Name using the corresponding entries in the documents
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")

# Collect input from user after program has ended
input("\n\nEnd of program, press any key to continue. . .")


