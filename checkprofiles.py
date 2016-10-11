import requests
from requests.auth import HTTPBasicAuth
import json
import config

#Provides a list of Member urls that have [attribute] is null
#param attribute to check for null value
#params memberUrls List of member urls to check
#return list of member urls with null [attribute] field
def checkForNull(attribute, memberUrls):
  attributeNotFound =[]
  
  for url in memberUrls:
    print(url)
    member_response = requests.get(url, auth=HTTPBasicAuth(config.username, config.password))
    member_data = json.loads(member_response.text)
    
    print(member_data[attribute])
    if member_data[attribute] is None:
        #TODO: TBD Could grab email here if speed was an issue
        attributeNotFound.append(url)
  return attributeNotFound