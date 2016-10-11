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
  print member_data["email"]
  return member_data["email"]

 
def send(profile):
  fromaddr = config.gmailuser
  toaddr = getEmailAddress(profile)
  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = "Profile update request"

  body = "Noticed you don't have a profile name on your Github account. Here's a link to your github profile to update it. But really I'd recommend going to Github through your browser - it's safer that way. Links in emails are not secure."
  msg.attach(MIMEText(body, 'plain'))

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.ehlo()
  server.starttls()
  server.login(fromaddr, config.gmailpass)
  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  server.quit()