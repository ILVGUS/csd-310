# Jennifer Adams
# CYBR410-T301
# July 3, 2022
# Objective: Insert three new student documents into students

from pymongo import MongoClient

# Connection string from MongoDB Atlas
url="mongodb+srv://admin:admin@cluster0.olwht.mongodb.net/pytech";

# Variable used to connect to MongoDB cluster
client = MongoClient(url)

# Variable specifying connection to pytech database
db = client.pytech

# First student, plus enrollments and courses using the same fields as Module 2.3
bob = {
    "student_id": "1007",
    "first_name": "Bob",
    "last_name": "Barker",
    "enrollment": [{
        "term": "Winter",
        "gpa": "2.5",
        "start_date": "November 13, 2021",
        "end_date": "March 13, 2022",
        "course": [{
            "course_id": "CYBR410",
            "description": "Data/Database Security",
            "instructor": "Prof. Peter Haas",
            "grade": "A-"
        },
        {
            "course_id": "BSIT380",
            "description": "System Hardening and Network Risk Mgmt",
            "instructor": "Prof. George Moats",
            "grade": "A+"
        }]
    }]
}

# Second student, plus enrollments and courses using the same fields as Module 2.3
alice = {
    "student_id": "1008",
    "first_name": "Alice",
    "last_name": "Wonderland",
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
            "course_id": "BSIT420",
            "description": "Microsoft Operating System Mgmt",
            "instructor": "Prof. William Cox",
            "grade": "A"
        }]
    }]
}

# Third student, plus enrollments and courses using the same fields as Module 2.3
eve = {
    "student_id": "1009",
    "first_name": "Eve",
    "last_name": "Dropper",
    "enrollment": [{
        "term": "Winter",
        "gpa": "2.5",
        "start_date": "November 13, 2022",
        "end_date": "March 13, 2022",
        "course": [{
            "course_id": "BSIT380",
            "description": "System Hardening and Network Risk Mgmt",
            "instructor": "Prof. George Moats",
            "grade": "B+"
        },
        {
            "course_id": "BSIT420",
            "description": "Microsoft Operating System Mgmt",
            "instructor": "Prof. William Cox",
            "grade": "A"
        }]
    }]
}

# Assign a variable to the student collection
students = db.students

# Insert student documents for Bob, Alice, and Eve into the student collection
bob_student_id = students.insert_one(bob).inserted_id
alice_student_id = students.insert_one(alice).inserted_id
eve_student_id = students.insert_one(eve).inserted_id

# Print header in specified format
print("\n-- INSERT STATEMENTS --")

# Print student record addition notification with student id appended as a string
print("Inserted student record Bob Barker into students collection with document id "+ str(bob_student_id))
print("Inserted student record Alice Wonderland into students collection with document id "+ str(alice_student_id))
print("Inserted student record Eve Dropper into students collection with document id "+ str(eve_student_id))

# Notify user that the program has ended, prompt to press a key to continue
input("\n\nEnd of program, press and key to continue. . .")