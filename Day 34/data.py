import requests
import json

url = 'https://opentdb.com/api.php'
params = {
    "amount": 10,
    "type": 'boolean',
}

response = requests.get(url, params)
response.raise_for_status()
data = response.json()

question_data = data['results']
