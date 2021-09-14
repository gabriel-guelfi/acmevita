from main import db
from ..models import Dependent

# Service class for dependents operations
# This service provide the following operations:
# List, Create
class DependentService:
    # Method that lists dependents by employee ID
    def listDependents(employeeId):
        """

        This method retrieves, based on the argument received on "employeeId",
        a list of dependents, alongside with its respective employee, from the ORM,
        turns it into a JSON serializable dataset, then returns it.

        """

        result = []
        for dependent, employee in Dependent.listDependent(employeeId):
            result.append({
                "dependentName": dependent.firstName+" "+dependent.lastName,
                "dependentID": dependent.id,
                "employeeName": employee.firstName+" "+employee.lastName,
            })

        return result

    # Method that create a new department register
    def createDependent(data):
        """

        This method creates a new instance of a dependent, passing first name,
        last name and its related employee's ID received on parameter "data", 
        save it on the database, then returns this newly created dependent.

        """

        dependent = Dependent(firstName=data['firstname'], lastName=data['lastname'], employeeId=data['employeeid'])
        db.session.add(dependent)
        db.session.commit()
        db.session.refresh(dependent)
        return dependent