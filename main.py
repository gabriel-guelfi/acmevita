import json
from core.app import app
from core.dbconfig import Dbconfig
import application.routes

# Start Database ORM
dbcfg = Dbconfig()
db = dbcfg.startDB()

# Set Entities on Database
from application.models import *
db.create_all()
        
# Run App
if __name__ == "__main__":
    app.run(debug=True)