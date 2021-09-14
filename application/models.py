from main import db

# Department entity's model
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)

    def listDepartments():
        "This method retrieves a general list of departments from the database,"

        return db.session.query(Department).all()

# Employee entity's model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)
    departmentId = db.Column(db.Integer, db.ForeignKey('department.id'))

    def listEmployees(departmentId):
        return db.session.query(Employee, Department)\
            .join(Department)\
            .filter(Department.id == departmentId).all()

# Dependent entity's model
class Dependent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)
    employeeId = db.Column(db.Integer, db.ForeignKey('employee.id'))

    def listDependent(employeeId):
        return db.session.query(Dependent, Employee)\
            .join(Employee)\
            .filter(Employee.id == employeeId).all()
