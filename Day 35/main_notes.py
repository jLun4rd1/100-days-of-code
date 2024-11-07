import requests
import json
import os

api_key = os.environ.get('API_KEY')
LAT = '-25.395694'
LON = '-54.206384'

api_call = f"https://api.openweathermap.org/data/2.5/forecast"
api_params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "units": 'metric',
    "cnt": 4
}

will_rain = False
response = requests.get(url=api_call, params=api_params)
response.raise_for_status() # <<< catches the response exception
weather_data = response.json()
for index in weather_data['list']:
    condition_code = index['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.")       
