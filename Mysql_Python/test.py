'''
1. Import Mysql.connector Module
2. Connect to Mysql Server
3. Create Cursor Object
4. Excute SQL Queries

'''
# Setup and Basic Queries

import mysql.connector
from datetime import datetime

db = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase" # select the data base after you create it, line 11 then comment it out or removeit
)

mycursor = db.cursor()

# Creating Tables, Inserting and Selecting Data

'''
mycursor.execute("CREATE DATABASE IF NOT EXISTS testdatabase") # specify the db name in server connection afer , line 7
mycursor.execute("CREATE TABLE person (name VARCHAR(50), age smallint UNSIGNED, personID INT PRIMARY KEY AUTO_INCREMENT)") # reomve after create 

mycursor.execute("DESCRIBE person")
for x in mycursor:
   print(x)

mycursor.execute("INSERT INTO person (name, age) VALUES (%s,%s)", ("Hatim", 45))
db.commit()

mycursor.execute("SELECT * FROM person")
for x in mycursor:
  print(x)

mycursor.execute("CREATE TABLE School (name VARCHAR (50), joined DATETIME, location ENUM('SDN', 'KSA', 'USA'), ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT  ) ")

mycursor.execute("DESCRIBE School")
for x in mycursor:
  print(x)

mycursor.execute("INSERT INTO School (name, joined, location, ID) VALUES (%s,%s,%s,%s)", ("Calc", datetime.now(), "USA", 102))
db.commit()

mycursor.execute("SELECT * FROM School")
for x in mycursor:
   print(x)


mycursor.execute("SELECT name, location FROM School WHERE location='USA' ORDER BY id DESC")
for x in mycursor:
    print(x)

    '''

# Altering table

'''
mycursor.execute("ALTER TABLE School ADD COLUMN Result ENUM('Passed', 'Failed') NOT NULL")

mycursor.execute("ALTER TABLE School DROP Result")

mycursor.execute("DESCRIBE School")
print(mycursor.fetchone())

mycursor.execute("ALTER TABLE School CHANGE joined Graduated DATE")

'''
# Foreign Key and Relating Tables

'''code goes here'''

# How to Host Mysql Server
'''code goes here'''
