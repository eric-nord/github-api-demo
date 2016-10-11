import json
import config
import requests
from requests.auth import HTTPBasicAuth

#Provides list of organizations the user is associated with
#Includes private and public members
def getOrgs():
  orgUrls = []
  orgs = requests.get('https://api.github.com/user/orgs', 
                      auth=HTTPBasicAuth(config.username, config.password))
  
  orgs_data = json.loads(orgs.text)
  
  for org in orgs_data:
    orgUrls.append(org["url"])
  return orgUrls