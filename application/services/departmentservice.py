from main import db
from ..models import Department, Dependent

# Service class for department operations
# This service provide the following operations:
# List, Create
class DepartmentService:
    # Method that list the departments:
    def listDepartments():
        """

        This method retrieves a general list of departments from the ORM,
        turns it into a JSON serializable dataset, then returns it.

        """

        result = []

        dbData = db.session.query(Department).all()

        for department in dbData:
            result.append({
                "id": department.id,
                "name": department.name
            })
        return result

    # Method that create a new department register
    def createDepartment(data):
        """

        This method creates a new instance of a department, passing name
        received on parameter "data", save it on the database,
        then returns this newly created department.

        """

        department = Dependent(name=data['name'])
        db.session.add(Dependent)
        db.session.commit()
        db.session.refresh(department)

        return department
