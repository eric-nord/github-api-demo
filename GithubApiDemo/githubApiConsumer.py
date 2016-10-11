import requests
from requests.auth import HTTPBasicAuth
import json

####config.py######
#username = "github_username"
#password = "github_password"
import config
import orgUrls
import listMembers
import checkprofiles
import s3Connect

#With provided username and password polls GitHub APIs for users in organizations
#without a "user" attribute. Then saves list of the users to AWS S3 and emails
#users inviting them to update their profile name"
def main():
  #get org urls
  orgs = orgUrls.getOrgs()
  #print(orgs)
  
  #get member list from each orgUrls
  members = listMembers.listMembers(orgs)
  #print(members)
  
  #get members without a "name" attribute 
  profilesWithoutNames = checkprofiles.checkForNull("name", members)
  print(profilesWithoutNames)
  
  #store list on S3
  pushStatus = s3Connect.upload(profilesWithoutNames)
  print(pushStatus)
  
  #email users with link to github to update their profile "name"

#run main#############################################################  
main()