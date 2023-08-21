import mysql.connector as database

db_username = "vista_admin"
db_password = "vista"
db = "VISTA_DB"
host = "localhost"

connection = database.connect(
    user=db_username,
    password=db_password,
    host=host,
    database=db)

cursor = connection.cursor()

username = ""
password = ""