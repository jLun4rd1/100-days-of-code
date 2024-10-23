# import smtplib

# # Create a credentials.txt file with your email and password
# with open('credentials.txt') as creds:
#     contents = creds.readlines()
#     contents = [x.strip() for x in contents]

# my_email = contents[0]
# my_password = contents[1]  
    
# connection = smtplib.SMTP("smtp.gmail.com")
# # Make connection secure
# connection.starttls()
# # Log into your account
# connection.login(user=my_email, password=my_password)
# # Send your mail. 'Subject' tells it's going to be a subject.
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="lunardi.joao@scalasystems.com.br",
#     msg='Subject: Greeting\n\nHello my friend')
# connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1998, month=12, day=11, hour=9)
print(date_of_birth)