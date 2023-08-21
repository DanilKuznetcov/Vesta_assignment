# Application for administration employees data and monitoring birthday

## Usage
### 1. Registration
![image](https://github.com/DanilKuznetcov/Vesta_assignment/assets/49263683/08184e2a-d40e-4b72-91ee-02a9004ed917)

For registation use medium button "Регистрация" and fill data in opened window
![image](https://github.com/DanilKuznetcov/Vesta_assignment/assets/49263683/014d93a0-ed02-4248-9c31-df814bf07669)
### 2. Authorisation
Use created creentials for authorisation. Hint - use "Запомнить меня", for quick authorization.
![image](https://github.com/DanilKuznetcov/Vesta_assignment/assets/49263683/2befb9a6-a4a9-4e62-8e5b-1d5a4f84ade7)

You can log out and change user - using top right link.

![image](https://github.com/DanilKuznetcov/Vesta_assignment/assets/49263683/fe8c284a-1c19-4f40-a0c6-5da5ff709733)

### 3. Administration
When opening, there is a reminder with the nearest birthday people.
![image](https://github.com/DanilKuznetcov/Vesta_assignment/assets/49263683/2f51b1d7-9b15-4cd5-b597-3d0165d70f9c)

For administration and navigation use buttons from the right
![image](https://github.com/DanilKuznetcov/Vesta_assignment/assets/49263683/53705d44-1714-488d-a072-311d8566725f)

## Installation
### 1. DB. 
In application uses 10.6.12-MariaDB. Create user (with correct rights) and fill values in Configurations.py.
![image](https://github.com/DanilKuznetcov/Vesta_assignment/assets/49263683/a702be16-723c-4b03-9664-8fa0687ce764)

In DB create two tables, for this use sql scripts from migration folder:
    
    001_create_user_table.sql
    002_create_employees_table.sql

### 2. Environment.  
Use environment from venv folder by conda package manager 
