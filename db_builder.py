import csv
from pymongo import MongoClient

client = MongoClient("lisa.stuy.edu", 27017)
db = client["mango"]

csv_courses = csv.DictReader(open("courses.csv"))
csv_students = csv.DictReader(open("peeps.csv"))

students = {}
for row in csv_students:
    students[row["id"]] = {
        "name": row["name"],
        "age": int(row["age"]),
        "id": int(row["id"]),
        "courses": []
    }

for row in csv_courses:
    _id = row["id"]
    if _id in students:
        students[_id]["courses"].append({
            "code": row["code"],
            "mark": int(row["mark"]),
        })

db.students.insert_many(students.values())
