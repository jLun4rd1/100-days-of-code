import requests
import os
from datetime import datetime

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
GRAPH_ID = 'graph1'


pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Gaming Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

day = datetime(year=2024, month=11, day=28)
formatted_day = day.strftime("%Y%m%d")
# print(today.strftime("%Y%m%d"))

graph_update_params = {
    "date": formatted_day,
    "quantity": "1"
}

# response = requests.post(url=graph_update_endpoint, json=graph_update_params, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_day}"

pixel_update_params = {
    "quantity": "3",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_day}"

response = requests.delete(url=pixel_update_endpoint, headers=headers)