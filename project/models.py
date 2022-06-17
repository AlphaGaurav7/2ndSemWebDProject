from . import db
from flask_login import UserMixin


class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    rollno = db.Column(db.String(30))
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    branch = db.Column(db.String(4))
    year = db.Column(db.Integer)
    password = db.Column(db.String(30))
    role = db.Column(db.String(30), default='student')


class Teacher(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    subject = db.Column(db.String(30), db.ForeignKey("subject.subject"))
    password = db.Column(db.String(30))
    role = db.Column(db.String(30), default='teacher')


class Assignments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    branch = db.Column(db.String(4))
    subject = db.Column(db.String(30))
    assignment = db.Column(db.String(30))
    max_marks = db.Column(db.Integer)
    
class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))
    assignment = db.Column(db.String(30))
    marks = db.Column(db.Integer)
    rollno = db.Column(db.String(30), db.ForeignKey('student.rollno'))
    
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String(4))
    year = db.Column(db.Integer)
    subject = db.Column(db.String(30))
