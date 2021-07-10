from flask_sqlalchemy import SQLAlchemy
from app import db
from flask import jsonify
class Student(db.Model):
    __tablename__ = 'student'
    # Define the fields here
    roll = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.String(3))

    def __init__(self, roll, name, year):
        self.roll = roll
        self.name = name
        self.year = year
        # fill this up
    def __repr__(self):
        return '<Roll : %r , Name : %r , Year : %r>' %(self.roll,self.name,self.year)
