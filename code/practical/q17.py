'''
17. WAP to connect to MySQL database named student and display the contents of the table.
'''
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user="root",passwd="password123",database="student")
cur=mycon.cursor()
cur.execute("select * from student")
data=cur.fetchall()
for i in data:
    print(i)