# Program to calculate BMI and provide its interpretation
height = float(input('Enter your height in meters: '))
weight = float(input('Enter your weight in kg: '))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f'Your BMI is {bmi}. You are under weight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}. You are over weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}. You are slightly over weight.')
elif bmi < 35:
    print(f'Your BMI is {bmi}. You are obese.')
else:
    print(f'Your BMI is {bmi}. You are clinically obese.')
