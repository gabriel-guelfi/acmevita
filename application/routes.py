from engine.app import app

@app.route("/department")
def listDepartments():
    return {
        "route": "/department",
        "data": ("dummy", "test", "data")
    }

@app.route("/department-employees/<int:departmentId>")
def departmentEmployees(departmentId):
    return {
        "route": "/department-employees",
        "params": {"departmentId": departmentId},
        "data": ("dummy", "test", "data")
    }

@app.route("/employee-dependents/<int:employeeId>")
def employeeDependents(employeeId):
    return {
        "route": "/employee-dependents",
        "params": {"employeeId": employeeId},
        "data": ("dummy", "test", "data")
    }

