## Introduction

This is an application for the test proposed by [Telavita](https://www.telavita.com.br/) for a job opportunity as a Senior Back-end developer.

It is written in Python using framework Flask, the ORM SQL Alchemy and a MySQL database server.

For more information about the test itself, follow this [link](https://gitlab.com/telavita/projeto-backend/-/tree/master)

If you're looking for the API's **documentation and reference guide**, follow this [Postman Link](https://documenter.getpostman.com/view/17465061/U16kq4zE)

---

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [MySQL](https://www.mysql.com/)  Server 8

---

## Dependencies

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- Flask [SQL Alchemy](https://www.sqlalchemy.org/)
- [PyMySQL](https://pypi.org/project/PyMySQL/)

---

## Installation Steps

1. Download the project on your computer and unzip it under some folder. (Ex.: */foo/bar/acmevita*)
2. Open up your terminal and navigate to its folder:
```shell
cd /foo/bar/acmevita
```
3. Create a Python virtual environment:
```shell
python3 -m venv venv
```
4. Activate Python virtual environment:
```shell
source venv/bin/activate
```
5. Install the dependencies:

*Install Flask Framework:*
```shell
pip install flask
```
*Install PyMySQL:*
```shell
pip install pymysql
```
*Install Flask-SQLAlchemy:*
```shell
pip install flask_sqlalchemy
```

---

## Configuration
Under the root folder of the project(Ex.: */foo/bar/acmevita*) you will find a file named ***config.json***.
This file contains all configs that you must do in order to run this **Acmevita Application**, such as
Database settings and so on.

Here's an example:
```json
{
    "dbconfigs": {
        "dbhost": "localhost",
        "dbname": "acmevita",
        "dbuser": "acmevita",
        "dbpass": "Senha123#",
        "dbport": 3306
    }
}
```
Just change "dbconfigs" to fulfill your database setup.

---

## Running the Application
1. From a terminal, navigate to the application's root folder:
```shell
cd /foo/bar/acmevita
```

2. Activate the Python Virtual Environment:
```shell
source venv/bin/activate
```

3. Run the application itself:
```shell
python main.py
```

Done and done! Now you can access its API's endpoints to see data at "localhost:5000". The **documentation and reference guide** about the API is 
documented on this [Postman Link](https://documenter.getpostman.com/view/17465061/U16kq4zE)

***OBS: You can populate database automatically with dummy data accessing endpoint "/populate". See **documentation and reference guide** for further info***

---