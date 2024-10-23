import datetime as dt
import smtplib
import random

weekdays = {
    'Monday': 0, 
    'Tuesday': 1, 
    'Wednesday': 2, 
    'Thursday': 3, 
    'Friday': 4, 
    'Saturday': 5, 
    'Sunday': 6,
}

def send_mail(message):
    connection.sendmail(
        from_addr=my_email,
        to_addrs="lunardi.joao@scalasystems.com.br",
        msg=f"Subject: Weekly Motivation!\n\nHello my friend, here's some words that might cheer you up.\n\n{message}"
    )

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == weekdays['Tuesday']:
    with open('../data/quotes.txt') as data_file:
        contents = data_file.readlines()
        quotes_list = [x.strip() for x in contents]
    
    quote = random.choice(quotes_list)
    
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
    
        send_mail(quote)
    

