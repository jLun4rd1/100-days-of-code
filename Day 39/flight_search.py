import os
import requests
from datetime import datetime, timedelta
from flight_data import FlightData

API_KEY = os.getenv('AMADEUS_API_KEY')
API_SECRET = os.getenv('AMADEUS_API_SECRET')
MY_IATA_CODE = os.getenv('MY_IATA_CODE')
TOKEN_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
IATA_ENDPOINT = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
FLIGHT_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

TOMORROW = datetime.strftime( datetime.now().date() + timedelta(days=1), '%Y-%m-%d' )
SIX_MONTHS_FROM_NOW = datetime.strftime( datetime.now().date() + timedelta(days=180), '%Y-%m-%d' )

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = API_KEY
        self.api_secret = API_SECRET
        self.token = self.get_new_token()
        
    def get_new_token(self):
        api_endpoint = TOKEN_ENDPOINT
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret,
        }
        
        response = requests.post(url=api_endpoint, data=data, headers=headers)
        data = response.json()
        token = data['access_token']
        expires_in = data['expires_in']
        print(f'Your token is: {token}')
        print(f'Your token expires in: {expires_in}')
        
        return token
       
    def get_city_code(self, city):
        api_endpoint = IATA_ENDPOINT
        headers = {'Authorization': f'Bearer {self.token}'}
        query = {
            'keyword': city,
            'max': 1,
            'include': ['AIRPORTS']
        }
        
        try:
            response = requests.get(url=api_endpoint, headers=headers, params=query)
            json_data = response.json()
            code = json_data['data'][0]['iataCode']
            print(f'Code for {city}: {code}')
        except Exception as e:
            print(f"Couldn't find IATA Code because:\n{e}")
            code = 'Not Found!'
            print(f'Code set to {code}')
            
        return code
    
    def get_price(self, d):
        return d['price']['total']
    
    def get_price_offers(self, iata_code, city):
        print(f'Getting prices for {city}...')
        api_endpoint = FLIGHT_ENDPOINT
        headers = {'Authorization': f'Bearer {self.token}'}
        query = {
            'originLocationCode': MY_IATA_CODE,
            'destinationLocationCode': iata_code,
            'departureDate': TOMORROW,
            'returnDate': SIX_MONTHS_FROM_NOW,
            'adults': 2,
            'nonStop': 'false',
            'currencyCode': 'BRL',
            'max': 10
        }
        response = requests.get(url=api_endpoint, params=query, headers=headers)
        json_data = response.json()['data']
        # print(json_data)
        lowest_price_data = min(json_data, key=self.get_price)
        print(f"{city}: {lowest_price_data['price']['total']}")
        
        return lowest_price_data
            
