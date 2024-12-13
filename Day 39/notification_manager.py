import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
SMTP_SERVER = 'smtp.gmail.com'
MY_EMAIL = os.environ.get('MY_EMAIL')
EMAIL_PASSWORD = os.environ.get('MY_PASSWORD')

class NotificationManager:
   
    def send_mail(self, data, city):
        subject = f"✈ FLIGHT OFFER TO {city}: R${data.price} 💰!!!"
        body = f"""
        It's a trip {data.duration} long! 
        All the best, with only {data.n_of_stops} stops.
        
        You'll leave from Foz do Iguaçu at {data.departure_time} on {data.departure_date}
        """
        
        msg = MIMEMultipart()
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, "plain", 'utf-8'))
        print(msg)
        
        try:
            server = smtplib.SMTP(SMTP_SERVER, 587)
            server.starttls()
            server.login(MY_EMAIL, EMAIL_PASSWORD)
            
            server.sendmail(MY_EMAIL, MY_EMAIL, msg.as_string())
            print("E-mail sent successfuly!")
        except Exception as e:
            print(f"Error sending e-mail: {e}")
