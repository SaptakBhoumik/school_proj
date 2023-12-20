'''
18. WAP to find the students record greater than 25 BMI from the database.
'''
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user="root",passwd="password123",database="student")
cur=mycon.cursor()
cur.execute("select * from student where bmi>25")
data=cur.fetchall()
print("The students with BMI greater than 25 are:-")
for i in data:
    print(i)