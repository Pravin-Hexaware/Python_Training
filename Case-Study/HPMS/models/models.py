from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Users(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),unique=True)
    password=db.Column(db.String(255))
    role=db.Column(db.String(255))
    created_on=db.Column(db.DateTime)

class Departments(db.Model):
    __tablename__="departments"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),nullable=True)
    head_doctor=db.Column(db.String(255),nullable=True)
    created_on=db.Column(db.DateTime)

class Patients(db.Model):
    __tablename__="patients"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),nullable=True)
    age=db.Column(db.Integer,nullable=True)
    disease=db.Column(db.String(255),nullable=True)
    admitted_on=db.Column(db.DateTime)
    department_id=db.Column(db.Integer,db.ForeignKey("departments.id"))

    department=db.relationship("Departments",backref="patients")