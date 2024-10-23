import pandas as pd
import datetime as dt
import smtplib
import random

##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
birthdays_dict = pd.read_csv('birthdays.csv').to_dict()

# Fill this in with your friends' names:
my_friends_list = [
    {
    'name': 'João Carlos',
    'email': 'lunardi.joao@scalasystems.com.br',
    'year': 1998,
    'month': 10,
    'day': 22,
    },
]

for friend in my_friends_list:
    birthdays_dict.update(friend)

pd.DataFrame([birthdays_dict]).to_csv('birthdays.csv', index=False)

# 2. Check if today matches a birthday in the birthdays.csv
birthdays_df = pd.read_csv('birthdays.csv')

now = dt.datetime.now()
month = now.month
day = now.day

for index, row in birthdays_df.iterrows():
    name = row['name']
    email = row['email']
    birthmonth = row['month']
    birthday = row['day']
    
    if month == birthmonth and day == birthday:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_index_list = [1,2,3]
        letter_index = random.choice(letter_index_list)

        with open(f'letter_templates/letter_{letter_index}.txt', encoding='utf-8') as letter_file:
            letter = letter_file.read().replace('[NAME]', name)
        
        with open('../data/credentials.txt') as creds:
            contents = creds.readlines()
            contents = [x.strip() for x in contents]

        my_email = contents[0]
        my_password = contents[1]     
            
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Make connection secure
            connection.starttls()
            # Log into your account
            connection.login(user=my_email, password=my_password)
            
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f'Subject: Happy B-Day!!\n\n{letter}'.encode('utf-8')
            )