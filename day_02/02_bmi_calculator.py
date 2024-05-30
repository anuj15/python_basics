# Program to calculate the BMI: weight / height * height
height = float(input('Enter height in meters: '))
weight = float(input('Enter weight in kilograms: '))
bmi = weight // (height ** 2)
print(f'Your BMI is: {bmi}')
