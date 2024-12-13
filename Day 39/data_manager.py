import os
import requests

API_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")
API_ENDPOINT = os.getenv("SHEETY_FLIGHT_ENDPOINT")

class DataManager:
    
    def __init__(self):
        self.api_endpoint = API_ENDPOINT
        self.headers = {"Authorization": API_TOKEN}
        self.destination_data = {}
        
    def get_data_from_sheets(self):
        response = requests.get(url=self.api_endpoint, headers=self.headers)
        data = response.json()
        self.destination_data = data['prices']
        
        return self.destination_data
    
    def update_data_from_sheets(self, row, id):
        response = requests.put(url=self.api_endpoint + '/' + id, json=row, headers=self.headers)
        return response