import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="study_tracker"
  )
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE study_sessions(id int,name VARCHAR(255),subject VARCHAR(255),Duration int,session_date DATE,Focus INT)")
print("Table created")
