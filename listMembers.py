import requests
from requests.auth import HTTPBasicAuth
import json
import config

#Provides a list of Member urls per organizations
#param List orgUrls
#return list of member urls
def listMembers(orgUrls):
  members =[]
  
  for url in orgUrls:
    #append /member to url - member_url is not valid canidate without a member list
    url = url + "/members"
    members_response = requests.get(url, auth=HTTPBasicAuth(config.username, config.password))
    members_data = json.loads(members_response.text)
    
    for member in members_data:
      members.append(member["url"])
  return members