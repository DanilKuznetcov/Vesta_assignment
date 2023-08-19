import mysql.connector as database

username = "vista_admin"
password = "vista"
db = "VISTA_DB"
host = "localhost"

connection = database.connect(
    user=username,
    password=password,
    host=host,
    database=db)

cursor = connection.cursor()

cursor.execute("INSERT INTO User (User_Fname,User_Lname,User_Username,User_Password,User_Email) VALUES ('AutoTom', 'Skagen', 'Stavanger', '4006', 'Norway')")
connection.commit()

x = cursor.execute("select * from User;")
print(cursor.fetchall())
# INSERT INTO User (User_Fname,User_Lname,User_Username,User_Password,User_Email) VALUES ('Tom', 'Skagen', 'Stavanger', '4006', 'Norway');