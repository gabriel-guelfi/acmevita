import json
from core.app import app
from core.dbconfig import Dbconfig
import application.routes

# Reads and sets configurations:
cfgFile = open('config.json')
configs = json.load(cfgFile)
cfgFile.close()

# Start Database ORM
dbcfg = Dbconfig(configs=configs['dbconfigs'])
db = dbcfg.startDB()

# Set Entities on Database
from application.models import *
db.create_all()
        
# Run App
if __name__ == "__main__":
    app.run(debug=True)