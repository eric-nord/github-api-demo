"""Main Module for executing GitHub Demo 

Executes GitHub API demo
"""

__version__ = '0.0.1'
__author__ = 'Eric Nord'

import github_utils
import s3Connect
import sendemails

def main():
  """  Polls GitHub APIs for users in all organizations without a "user" attribute, saves list of users to AWS S3 and emails users  """
  
  orgName = input("Enter organization name to check - \"All\" will check all organizations associated with your account: ")
  print orgName
  
  if orgName == "All":
    #get all org urls associated with account
    orgs = github_utils.get_orgs()
    #print(orgs)
    
    #get member list from each organization url
    members = github_utils.listMembers(orgs)
    #print(members)
  else:
    #get member list from input organization name
    members = github_utils.listMembers(orgName)
    #print(members)
    
  
  #get members without a "name" attribute 
  profilesWithoutNames = github_utils.checkForNull("name", members)
  print(profilesWithoutNames)
  
  #store list on S3
  pushStatus = s3Connect.upload(profilesWithoutNames)
  print(pushStatus)
  
  #email users with link to github to update their profile "name"
  for profile in profilesWithoutNames:
    sendemails.send(profile)

#run main#############################################################  
main()