from pymongo import MongoClient

client = MongoClient("lisa.stuy.edu", 27017)
db = client["mango"]

students = db.students.find()
for student in students:
    grades = [course["mark"] for course in student["courses"]]
    average = sum(grades) * 1.0 / len(grades)
    name = student["name"]
    _id = student["id"]
    print "ID: %s\nName: %s\nAverage: %s\n" % (_id, name, average)
