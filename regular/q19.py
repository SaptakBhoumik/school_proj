'''
18. WAP to find the roll no and name of student with marks greater than 25 from the database.
'''
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user="root",passwd="password123",database="student")
cur=mycon.cursor()
cur.execute("select roll_no,data from student where student.marks>25")
data=cur.fetchall()
print("The students with marks greater than 25 are:-")
for i in data:
    print(i)