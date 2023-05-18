Sueldos Chubut API
==================

This project provides a Python API for accessing the Sueldos Chubut website, offering convenient access to salary information for public employees in the Chubut province of Argentina.

Features
--------

The API offers the following features:

-   Retrieve the complete list of employees
-   Obtain salary information for a specific employee
-   Access the list of available positions
-   Retrieve salary information for a specific position

Installation
------------

To install the project, execute the following command:

`pip install sueldos-chubut-api`

Usage
-----

To use the project, import the `SueldosChubutApi` class and create an instance of it:

`from sueldos_chubut_api import SueldosChubutApi`

`api = SueldosChubutApi()`

You can then utilize the API to retrieve information about the salaries of public employees in the Chubut province of Argentina. For instance, to obtain the list of all employees, use the following code:

`employees = api.get_employees()`

The `employees` variable will be a list of dictionaries, with each dictionary containing information about a specific employee. For example, the following code will print the name of the first employee in the list:

`print(employees[0]["name"])`

To run the project as a standalone application, execute the following command:
----- 

`python manage.py runserver 0.0.0.0:8000`

Endpoints
---------

-   <http://127.0.0.1:8000/api/>
-   <http://127.0.0.1:8000/api/organisms/>
-   <http://127.0.0.1:8000/api/salary/?name=&dni=&organism=6218&page=1>