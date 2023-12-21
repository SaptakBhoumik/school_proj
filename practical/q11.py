'''
11. WAP to generate a random password 
'''
import random
def generate_password(length):
    string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
    password=""
    for i in range(length):
        n=random.randint(0,len(string)-1)
        password+=string[n]
    return password
n=int(input("Enter the length of password:-"))
print("Password:-",generate_password(n))
