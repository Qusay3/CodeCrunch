import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"

)
users = [("Qusay", "Qmf94", "Pass123", "qusay@gmail.com"),
         ("Brad", "bradtech12","Abc@12345", "bradly@gmail.com"),
         ("Sara", "IamSara", "Pa$$word666", "Sara.she@gmail.com"),
         ("Joy", "Joy_rr", "Joe149#", "joe@icloud.com")]

user_scores = [(12, 450),
               (10, 800),
               (15, 250),
               (9, 620)]

cursor = db.cursor()

Q1 = "CREATE TABLE Users (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50, username VARCHAR(50), email VARCHAR(50)))"
Q2 = "CREATE TABLE Scores (userID INT PRIMARY KEY, FOREIGN KEY(userID) REFERENCES Users(id), game1 INT DEFAULT 0, game2 INT DEFAULT 0)"

'''
cursor.execute(Q1)
cursor.execute(Q2)

'''
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

# cursor.executemany("INSERT INTO Users (name, passwd) VALUES (%s, %s)", users) # using executemany()

Q3 = "INSERT INTO Users (name, passwd) VALUES (%s, %s, %s, %s)"
Q4 = "INSERT INTO Scores(userID, game1, game2) VALUES (%s, %s, %s)"


for x, user in enumerate(users):
    cursor.execute(Q3, user)
    last_id = cursor.lastrowid
    cursor.execute(Q4, (last_id,) + user_scores[x])

db.commit()
cursor.execute("SELECT * FROM users")

for x in cursor:
    print(x)

cursor.execute("SELECT * FROM Scores")

for x in cursor:
    print(x)

