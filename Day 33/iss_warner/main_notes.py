#     An Application Programming Interface (API) is a set of commands
# functions, protocols, and objects that programmers can use to create
# software or interact with an external system.

#     Basically it is a barrier between your program and an external 
# system

#     We're trying to use the rules established by the API to use the
# data inside that external system

#     If you follow the rules, the external system will respond to
# your request with that wanted piece of data

#     API Endpoints are where the API are located. It's usually just a
# URL. Besides knowing the URL, you should also make a request

import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.") <<< There's a simpler way!
data = response.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)

print(iss_position)
