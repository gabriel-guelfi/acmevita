from random import randrange
from application.services.departmentservice import DepartmentService
from application.services.employeeservice import EmployeeService
from application.services.dependentservice import DependentService

class DummyDataGenerator:
    def __init__(self):
        self.__depNames = (
            "Tech & Solutions",
            "Accountability",
            "Sales",
            "Administration",
            "Logistics",
            "Marketing",
            "General Management",
            "Operations",
            "Human Resources",
            "Purchase"
        )

        self.__firstNames = (
            "James",
            "Mary",
            "Robert",
            "Patricia",
            "John",
            "Jennifer",
            "Michael",
            "Linda",
            "William",
            "Elizabeth",
            "David",
            "Barbara",
            "Richard",
            "Susan",
            "Joseph",
            "Jessica",
            "Thomas",
            "Sarah",
            "Charles",
            "Karen"
        )

        self.__lastNames = (
            "Smith",
            "Johnson",
            "Williams",
            "Brown",
            "Jones",
            "Garcia",
            "Miller",
            "Davis",
            "Rodriguez",
            "Martinez",
            "Hernandez",
            "Lopez",
            "Gonzalez",
            "Wilson",
            "Anderson",
            "Thomas",
            "Moore",
            "Jackson",
            "Martin",
            "Lee"
        )

    def exec(self):
        depService = DepartmentService
        empService = EmployeeService()
        depenService = DependentService

        if len(depService.listDepartments()) == 0:
            for depName in self.__depNames:
                department = depService.createDepartment(depName)

                for x in range(randrange(5)):
                    employee = empService.createEmployee(data={
                        "firstname": self.__firstNames[randrange(20)],
                        "lastname": self.__lastNames[randrange(20)],
                        "departmentid": department.id
                    })

                    for y in range(randrange(4)):
                        depenService.createDependent(data={
                            "firstname": self.__firstNames[randrange(20)],
                            "lastname": self.__lastNames[randrange(20)],
                            "employeeid": employee.id
                        })
            return "The database was successfully populated"
        else: 
            return "The database was already populated. No register was created."