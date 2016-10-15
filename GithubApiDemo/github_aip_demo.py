"""Main Module for executing GitHub Demo 

Executes GitHub API demo
"""

__version__ = '0.0.1'
__author__ = 'Eric Nord'

#Verifies user has followed installation instructions
try:
    import config
except ImportError:
    print("Please copy exampleconfig.py to config.py\n" 
          "and enter authentication information before proceeding")
    raise SystemExit

import github_utils
import s3Connect
import sendemails

def main():
  """  Polls GitHub APIs for users in all organizations without a "user" attribute, saves list of users to AWS S3 and emails users  """
  
  orgName = None
  
  while not orgName:
    orgName = str(raw_input(
      "\nEnter GitHub organization to find users without a profile name\n"
      "\"All\" will check all organizations associated with " + config.username + "\n"))
  
  
  if orgName == "All":
    #get all org urls associated with account
    print("\nChecking GitHub organizations associated with " + config.username)
    orgs = github_utils.get_orgs()

    #get member list from each organization url
    members = github_utils.list_members(orgs)

  else:
    #get member list from input organization name
    print("Checking " + orgName)
    members = github_utils.list_members(orgName)
 

  #get members without a "name" attribute 
  profilesWithoutNames = github_utils.check_for_null("name", members)
  print("Members without profile names: ")
  print(profilesWithoutNames)
  
  #store list on S3
  pushStatus = s3Connect.upload(profilesWithoutNames)
  print("Storing list to AWS S3 ")
  print(pushStatus)
  
  #email users with link to github to update their profile "name"
  for profile in profilesWithoutNames:
    sendemails.send(profile)

#run main#############################################################  
main()