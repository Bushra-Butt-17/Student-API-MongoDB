from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
import os
app.secret_key = os.urandom(24) 
# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")

# Database and Collection
db = client["school_database"]
students_collection = db["students"]


# Home Route
@app.route("/")
def home():
    return render_template("index.html")

# Route for the "Add Student" page
@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        # Get data from the form
        name = request.form.get("name")
        age = request.form.get("age")
        grade = request.form.get("grade")

        # Validation
        if not name or not age or not grade:
            return render_template("add_student.html", message="All fields are required!")

        # Insert the student data into MongoDB
        student_data = {
            "name": name,
            "age": int(age),
            "grade": grade
        }

        try:
            students_collection.insert_one(student_data)
            return redirect(url_for("home"))
        except Exception as e:
            return render_template("add_student.html", message=f"Error adding student: {str(e)}")

    return render_template("add_student.html")

@app.route("/students/age", methods=["GET", "POST"])
def view_students_by_age():
    if request.method == "POST":
        age = int(request.form.get("age"))
        # Fetch students older than the given age
        students = students_collection.find({"age": {"$gt": age}})
        students_list = list(students)
        return render_template("students_by_age.html", students=students_list, age=age)

    return render_template("filter_by_age.html")

# View all students Route
@app.route("/students", methods=["GET"])
def view_all_students():
    # Fetch all students from the database
    students = list(students_collection.find({}, {"_id": 0}))  # Exclude the _id field from the response
    return render_template("view_students.html", students=students)



@app.route('/students/update/<student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    student = db.students.find_one({'_id': ObjectId(student_id)})
    if request.method == 'POST':
        new_name = request.form['name']
        new_age = request.form['age']
        new_grade = request.form['grade']
        db.students.update_one(
            {'_id': ObjectId(student_id)},
            {'$set': {'name': new_name, 'age': new_age, 'grade': new_grade}}
        )
        flash('Student updated successfully!', 'success')
        return redirect('/students')
    return render_template('update_student_form.html', student=student)

@app.route('/students/delete/<student_id>', methods=['POST'])
def delete_student(student_id):
    db.students.delete_one({'_id': ObjectId(student_id)})
    flash('Student deleted successfully!', 'danger')
    return redirect('/students')


@app.route('/students/update_or_delete', methods=['GET', 'POST'])
def update_or_delete_student():
    students = db.students.find()  # Fetch all students
    return render_template('update_or_delete_student.html', students=students)


if __name__ == "__main__":
    app.run(debug=True)
