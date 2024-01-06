import mysql.connector as mq

i = input("Enter your Mysql password: ")

con = mq.connect(host = 'Localhost',user = 'root', password = i)
cur = con.cursor()

cur.execute("create Database BankDet")
cur.execute("use BankDet")
cur.execute("create table UserInfo(Username varchar(100) Primary Key, Password varchar(100), Pin int, Balance bigint, CardNumber bigint)")

print("Database Configuration Completed You can proceed with trying out the Bank Simulator")
input("Press Enter to exit")
