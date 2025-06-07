#DONE BY INNOENT MUTALE MWELWA

import smtplib
import csv
import os
from email.message import EmailMessage
from dotenv import load_dotenv

#Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWWORD = os.getenv("EMAIL_PASS")

def send_emails():
    with open('contacts.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            email = row['email']

            msg = EmailMessage()
            msg['from'] = EMAIL_ADDRESS
            msg['to'] = email
            msg['subject'] = "Let's connect"
            #Load Templet and costomize
            with open('email_templet.txt','r') as f:
                content = f.read()
                msg.set_content(content.format(name = name))
            #Attach file(optional)
            with open('CV.pdf','rb') as attachment:
                msg.add_attachment(attachment.read(), maintype='application', subtype='pdf', filename='CV.pdf')
            
            #semd Email
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWWORD)
                print(f"Email sent to{name} ({email})")


if __name__ == "__main__":
    send_emails()


#DONE BY INNOENT MUTALE MWELWA