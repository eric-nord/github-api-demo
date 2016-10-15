import config
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import requests
from requests.auth import HTTPBasicAuth
import json


def getEmailAddress(url):
  member_response = requests.get(url, auth=HTTPBasicAuth(config.username, config.password))
  member_data = json.loads(member_response.text)
  return member_data["email"]

 
def send(profile):
  fromaddr = config.gmailuser
  toaddr = getEmailAddress(profile)
  
  
  willSend = str(raw_input("Send email to " + toaddr + "? (Y/N)" ))
  
  if willSend.lower() != "y":
    print("Skipping email to " + toaddr)
    return
  else:
    #userprofile = "https://github.com/" + username
    username = profile.rsplit('/', 1)[-1]
    
    profilelink = "https://github.com/account"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Profile update request"

    body = "Noticed you don't have a profile name on your Github account. Here's a link to your github profile " + profilelink + ". I'd recommend going to Github through your browser - it's safer that way. Links in emails are not secure."
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    try:
      server.login(fromaddr, config.gmailpass)
    except smtplib.SMTPAuthenticationError:
      print ("\nPlease verify gmail credentials in config.py\n"
             "verify less secure apps is enabled and\n"
             "Captcha is disabled for gmail SMTP provider\n"
             "see readme for more details\n")
      raise SystemExit
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Email sent to " + toaddr)
    return
