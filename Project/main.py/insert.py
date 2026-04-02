import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="study_tracker"
  )
mycursor = mydb.cursor()
sql ="INSERT INTO study_sessions(name,subject,duration,session_date,focus)VALUES(%s,%s,%s,%s,%s)"
data = [
("Arun","Math",60,"2026-03-01",85),
("Priya","Science",45,"2026-03-01",78),
("Karthik","English",30,"2026-03-02",70),
("Divya","Computer",90,"2026-03-02",92),
("Rahul","Math",120,"2026-03-03",88),
("Sneha","Science",60,"2026-03-03",80),
("Vijay","English",40,"2026-03-04",75),
("Anjali","Computer",100,"2026-03-04",95),
("Surya","Math",80,"2026-03-05",82),
("Meena","Science",50,"2026-03-05",77),
("Ajay","English",35,"2026-03-06",72),
("Kavya","Computer",110,"2026-03-06",93),
("Ramesh","Math",95,"2026-03-07",86),
("Lakshmi","Science",70,"2026-03-07",84),
("Dinesh","English",55,"2026-03-08",79),
("Harini","Computer",85,"2026-03-08",91),
("Manoj","Math",75,"2026-03-09",83),
("Pooja","Science",65,"2026-03-09",81),
("Sathish","English",45,"2026-03-10",74),
("Nisha","Computer",120,"2026-03-10",96),
("Prakash","Math",90,"2026-03-11",87),
("Deepa","Science",55,"2026-03-11",79),
("Gokul","English",50,"2026-03-12",73),
("Swathi","Computer",105,"2026-03-12",94),
("Murali","Math",85,"2026-03-13",84),
("Revathi","Science",60,"2026-03-13",82),
("Kiran","English",40,"2026-03-14",71),
("Aishwarya","Computer",115,"2026-03-14",95),
("Senthil","Math",100,"2026-03-15",89),
("Keerthi","Science",70,"2026-03-15",83),
("Arvind","English",35,"2026-03-16",72),
("Gayathri","Computer",90,"2026-03-16",92),
("Balaji","Math",110,"2026-03-17",90),
("Janani","Science",65,"2026-03-17",80),
("Vignesh","English",55,"2026-03-18",76),
("Raji","Computer",120,"2026-03-18",97),
("Suresh","Math",95,"2026-03-19",88),
("Uma","Science",75,"2026-03-19",85),
("Praveen","English",45,"2026-03-20",74),
("Latha","Computer",100,"2026-03-20",93),
("Naveen","Math",85,"2026-03-21",86),
("Shalini","Science",60,"2026-03-21",82),
("Arul","English",50,"2026-03-22",75),
("Divakar","Computer",110,"2026-03-22",94),
("Rohit","Math",120,"2026-03-23",91),
("Bhavya","Science",70,"2026-03-23",84),
("Tarun","English",40,"2026-03-24",73),
("Monika","Computer",95,"2026-03-24",92),
("Yogesh","Math",105,"2026-03-25",89),
("Chitra","Science",65,"2026-03-25",83)
]
mycursor.executemany(sql,data)
mydb.commit()
print(mycursor.rowcount,"Data inserted")





















     
