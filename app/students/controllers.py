from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from flask import jsonify
from app.students.models import Student
from app.enrolment.models import Enroll
mod_students = Blueprint('students', __name__)

@mod_students.route('/students', methods=['GET'])
def get_all_students():
    if request.method == 'GET':
        students=[]
        list = Student.query.all()
        second = Enroll.query.all()
        for num in list:
            courses=[]
            for num1 in second:
                if num1.roll == num.roll:
                    courses.append(num1.id)
            req = {
                "roll" : num.roll,
                "name" : num.name,
                "year" : num.year,
                "courses" : courses
            }
            students.append(req)
        return jsonify(students = students)

@mod_students.route('/addStudent', methods=['POST'])
def add_student():
    if request.method == 'POST':
        try:
            student = Student(request.form['roll'], request.form['name'], request.form['year'])
            db.session.add(student)
            db.session.commit()
            return 'success: Created a student'
        except:
            return 'error: Enter the field values correctly'
