#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_data_from_sheets()
# print(sheet_data)

from flight_search import FlightSearch
flight_search = FlightSearch()

from notification_manager import NotificationManager
notification_manager = NotificationManager()

for dict in sheet_data:
    iata_code = dict['iataCode']
    if iata_code == '' or iata_code == 'Not Found!':
        
        city = dict['city']
        id = str(dict['id'])
        row = {'price': dict} # Sheety API requires data to be nested inside 'price'
        
        dict['iataCode'] = flight_search.get_city_code(city)
        
        data_manager.destination_data = sheet_data
        data_manager.update_data_from_sheets(row, id)

for dict in data_manager.destination_data:
    iata_code = dict['iataCode']
    city = dict['city']
    
    lowest_price_data = flight_search.get_price_offers(iata_code, city)
    
    lowest_price = float(lowest_price_data['price']['total'])
    duration = lowest_price_data['itineraries'][0]['duration'].split('PT')[1]
    departure_date = lowest_price_data['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
    departure_time = lowest_price_data['itineraries'][0]['segments'][0]['departure']['at'].split('T')[1]
    n_of_stops = len(lowest_price_data['itineraries'][0]['segments'])
    print(lowest_price, duration, departure_date, departure_time, n_of_stops)

    lowest_flight_data = FlightData(price=lowest_price, duration=duration, departure_date=departure_date, departure_time=departure_time, n_of_stops=n_of_stops)
    if float(dict['lowestPrice']) < lowest_price:
        print('New lowest price found! Sending mail...')
        dict['lowestPrice'] = lowest_price
        
        id = str(dict['id'])
        row = {'price': dict}
        
        data_manager.update_data_from_sheets(row, id)
        
        notification_manager.send_mail(lowest_flight_data, city)
        
        