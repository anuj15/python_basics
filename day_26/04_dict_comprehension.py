import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# list to dict
student_scores = {name: random.randint(30, 99) for name in names}

# dict to dict
passed_students = {name: score for (name, score) in student_scores.items() if score > 60}
failed_students = {name: score for (name, score) in student_scores.items() if score <= 60}
print(passed_students)
print(failed_students)

sentence = 'What is the Airspeed Velocity of an unladen Swallow?'
s_dict = {current_card: len(current_card) for current_card in sentence.split()}
print(s_dict)

weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24,
}
weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)
