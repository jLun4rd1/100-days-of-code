import requests
from datetime import datetime
import time
import smtplib

MY_LAT = -25.395793
MY_LONG = -54.206333

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

email_sent = False

def check_distance():
    print('Checking distance from ISS...')
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    iss_position = (iss_latitude, iss_longitude)
    my_position = (MY_LAT, MY_LONG)
    # difference = (iss_position[0] - my_position[0], iss_position[1] - my_position[1])
    # if difference > (-5,-5) and difference < (5,5):
    
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True, iss_position, my_position
    else:
        return False, iss_position, my_position
    
def is_night():
    print('Checking time...')
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = int(time_now.hour)
    
    if sunset <= hour <= sunrise:
        return True
    else:
        return False

def send_mail(already_sent):
    with open('../data/credentials.txt') as creds:
        contents = creds.readlines()
        contents = [x.strip() for x in contents]

    my_email = contents[0]
    my_password = contents[1] 

    # Establish connection using with  
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Make connection secure
        connection.starttls()
        # Log into your account
        connection.login(user=my_email, password=my_password)
        # Send mail
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:ISS IS ABOVE YOU ☝!!\n\nYou should take a loot outside right now!")
        already_sent = True
    
    return already_sent
    
while email_sent == False:    
    close_enough, iss_position, my_position = check_distance()
    
    if close_enough:
        print(f"You're close! \nYour position: {my_position} \nTheir position: {iss_position}")
        is_dark = is_night()
        
        if is_dark:
            print("It's dark!!! Sending mail...")
            email_sent = send_mail(email_sent)
        else:
            print("Unfortunately, it's daytime.")
    else:
        print("You're too far away ☹")
    time.sleep(60)



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
