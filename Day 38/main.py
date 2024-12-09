import os
import requests
from datetime import datetime

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
API_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")
TODAY = datetime.now().strftime('%Y/%m/%d')

def post_data_on_sheets(name, duration, calories):    
    api_endpoint = 'https://api.sheety.co/041ad1056af19f3b32cccd5eb49d66ed/myWorkouts/workouts'
    params = {
        "workout": {
            "date": TODAY,
            "time": time,
            "exercise": str(name).capitalize(),
            "duration": float(duration),
            "calories": float(calories)
        }
    }
    headers = {
        "Authorization": API_TOKEN
    }
    
    response = requests.post(url=api_endpoint, json=params, headers=headers)
    print(response.text)

api_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

query = input("Tell me what your exercise was: ")
time = input('What time was that? (Ex.: 15:00) ')

params = {
    "query": query
}

response = requests.post(url=api_endpoint, json=params, headers=headers)
data = response.json()
print(data)

for exercise in data['exercises']:
    name = exercise['user_input']
    duration = exercise['duration_min']
    calories = exercise['nf_calories']
    post_data_on_sheets(name, duration, calories)