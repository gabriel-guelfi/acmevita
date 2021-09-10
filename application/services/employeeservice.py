from main import db
from ..models import Department, Employee, Dependent

# Service class for dependents operations
# This service provide the following operations:
# List, Has Dependent Check and Create
class EmployeeService:
    # Method that lists employees by department ID
    def listEmployees(self, departmentId):
        """

        This method retrieves, based on the argument received on "departmentId",
        a list of employees, alongside with its respective department name, from the ORM,
        turns it into a JSON serializable dataset, then returns it.

        """

        result = []

        dbData = db.session.query(Employee, Department)\
        .join(Department)\
        .filter(Department.id == departmentId).all()

        for employee, department in dbData:
            result.append({
                "employeeID": employee.id,
                "employeeName": employee.firstName+" "+employee.lastName,
                "department": department.name,
                "hasDependent": self.hasDependent(employee.id)
            })

        return result

    # This method checks if an employee has dependents
    def hasDependent(self, employeeId):
        """

        This method retrieves, based on the argument received on "employeeId",
        a list of dependents from the ORM, counts how many rows are in the dataset
        and if it's greater than zero, returns "True", else returns "False"

        """

        dbData = db.session.query(Dependent).filter(Dependent.employeeId == employeeId)

        if dbData.count() > 0:
            return True
        else: return False

    # Method that create a new employee register
    def createEmployee(self, data):
        """

        This method creates a new instance of an employee, passing first name,
        last name and its related department's ID received on parameter "data", 
        save it on the database, then returns this newly created employee.

        """

        employee = Employee(firstName=data['firstname'],lastName=data['lastname'], departmentId=data['departmentid'])
        db.session.add(employee)
        db.session.commit()
        db.session.refresh(employee)

        return employee