from main import db

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)
    departmentId = db.Column(db.Integer, db.ForeignKey('department.id'))
    
class Dependent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)
    employeeId = db.Column(db.Integer, db.ForeignKey('employee.id'))
