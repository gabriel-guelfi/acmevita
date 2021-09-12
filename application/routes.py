from core.app import app
from flask import jsonify

# Route for listing departments:
@app.route("/department")
def listDepartments():
    """

    This function retrieves a list of departments from 
    Department Service, then returns this list jsonified

    """

    from .services.departmentservice import DepartmentService
    service = DepartmentService

    return jsonify(service.listDepartments())

# Route for listing employees within departments:
@app.route("/department-employees/<int:departmentId>")
def departmentEmployees(departmentId):
    """

    This function retrieves a list of employees, based
    on passed Department's ID from Employee Service, 
    then returns this list jsonified

    """

    from .services.employeeservice import EmployeeService
    service = EmployeeService()

    return jsonify(service.listEmployees(departmentId=departmentId))

# Route for listing employee's dependents:
@app.route("/employee-dependents/<int:employeeId>")
def employeeDependents(employeeId):
    """

    This function retrieves a list of dependents, based
    on passed Employee's ID from Dependent Service, 
    then returns this list jsonified

    """

    from .services.dependentservice import DependentService
    service = DependentService

    return jsonify(service.listDependents(employeeId=employeeId))

# Route for populating database
@app.route("/populate", methods=['POST'])
def populateDB():
    """

    This function uses the service DummyDataGenerator
    to populate database with randomized dummy data

    """
    from .services.dummydataservice import DummyDataGenerator
    dmg = DummyDataGenerator()

    return dmg.exec()
