import requests
import urllib3

urllib3.disable_warnings()
parameters = {
    'amount': 10,
    'type': 'boolean',
    'category': 18,
}
response = requests.get(url='https://opentdb.com/api.php', params=parameters, verify=False)
response.raise_for_status()
question_data = response.json()['results']
