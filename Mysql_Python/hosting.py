# Hosting Mysql Server Remotly on linux 

import mysql.connector
from datetime import date
import datetime

db = mysql.connector.connect(
    host="172.104.29.71",
    user="root",
    passwd="Ai.Solutions203*",
    database="test"
)

mycursor = db.cursor()
mycursor.execute("SHOW TABLES")
print(mycursor.fetchone())


# You are good to un queries now








'''Process and Linux Commands
Once you have logged into the linux server run the following:

sudo apt-get install mysql-server
sudo mysql_secure_installation utility
sudo ufw enable  # allows remote access
sudo ufw allow mysql
sudo systemctl start mysql
sudo systemctl enable mysql 
cd to /etc/mysql/mysql.conf.d/mysqld.cnf
change bind to 0.0.0.0
sudo systemctl restart mysql  # restart mysql

Now obtain your PUBLIC IPV4 Address from the machine you want to connect with.

mysql -u root -p
create database Test
Get ip address
-- Create the user with a password
CREATE USER 'root'@'65.50.168.172' IDENTIFIED BY 'Ai.solutions23*';
-- Grant all privileges on the database `test` to the user
GRANT ALL PRIVILEGES ON test.* TO 'root'@'65.50.168.172';
-- Reload the privileges
FLUSH PRIVILEGES;
'''