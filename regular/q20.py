'''
20. WAP to find the BMI of the student
'''
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user="root",passwd="password123",database="student")
cur=mycon.cursor()
cur.execute("select roll_no,student,weight/(height*height) as bmi from student")
data=cur.fetchall()
print("BMI of students are:-")
for i in data:
    print(i)