'''
15. WAP to find the BMI (Body Mass Index) of a person
'''
def calculate_bmi(weight, height):
    return weight / (height ** 2)
h=float(input("Enter your height in meters:-"))
w=float(input("Enter your weight in kilograms:-"))
bmi=calculate_bmi(w,h)
print("Your BMI is:-",bmi)
