from datetime import datetime as dt

import requests


def get_exercise_data():
    app_id = '4418d9a9'
    api_key = '700c6d3ba143ee884872f5e8efe1145f'
    endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
    headers = {
        'x-app-id': app_id,
        'x-app-key': api_key,
    }
    nlp_parameters = {
        'query': 'ran 5k and cycled for 20 minutes',
    }
    response = requests.post(url=endpoint, json=nlp_parameters, headers=headers)
    return [[x['name'].title(), x['duration_min'], x['nf_calories']] for x in response.json()['exercises']]


def set_exercise_data():
    date_now = dt.now().strftime('%d/%m/%Y')
    time_now = dt.now().strftime('%H:%M:%S')
    user_name = 'b0275f7af437836b333007208e74149d'
    project_name = 'myWorkouts'
    sheet_name = 'workouts'
    endpoint = f'https://api.sheety.co/{user_name}/{project_name}/{sheet_name}'
    for data in get_exercise_data():
        parameters = {
            'workout': {
                'date': date_now,
                'time': time_now,
                'exercise': data[0],
                'duration': data[1],
                'calories': data[2],
            }
        }
        headers = {
            'Authorization': 'Basic dGVzdHVzZXI6dGVzdHB3ZA=='
        }
        requests.post(url=endpoint, json=parameters, headers=headers)


set_exercise_data()
