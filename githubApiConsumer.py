import requests
from requests.auth import HTTPBasicAuth
import json

####config.py######
#username = "github_username"
#password = "github_password"
import config
import orgUrls
import listMembers

##Global data##


        
#With provided username and password polls GitHub APIs for users in organizations
#without a "user" attribute. Then saves list of the users to AWS S3 and emails
#users inviting them to update their profile name"
def main():
  #get org urls
  orgs = orgUrls.getOrgs()
  print(orgs)
  
  #get member list from each orgUrls
  listMembers.listMembers(orgs)
  
  #check each member to see if they have a "name" attribute - if not store the org, login, email
  
  #store list on S3
  
  #email users with link to github to update their "name"

#run main#############################################################  
main()