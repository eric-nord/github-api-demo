"""GitHub util module.

Functions for pulling data from GitHub APIs
"""

__version__ = "0.0.1"
__author__ = "Eric Nord"

import utils


def get_orgs():
  """ Provides list of github organization urls based on authenticated user. """
  
  url = "https://api.github.com/user/orgs"
  
  org_urls = []
  orgs = utils.get_json(url)
  
  for org in orgs:
    org_urls.append(org["url"])
    
  return org_urls


def list_members(orgs):
  """Provides a list of Member urls per organizations.
  
  param orgs either a list of urls pointing to organizations or a single org name
  return list of member urls
  """
  members =[]
  
  
  if isinstance(orgs, list):
    #if list of orgs for each org get members list
    for url in orgs:
      #append /member to url - member_url is not valid canidate without a member list
      url = url + "/members"
      print("Checking " + url)
      members_data = utils.get_json(url)

      for member in members_data:
        members.append(member["url"])
    return members
  
  
  else:
    #build url from input org name and return member list
    url = "https://api.github.com/orgs/" + orgs + "/members"
    members_data = utils.get_json(url)
    
    #check for invalid GitHub credentials or invalid github org name
    try:
      for member in members_data:
        members.append(member["url"])
      return members
    except TypeError:
      if(members_data["message"] == "Not Found"):
        print("That organization doesn't exist try again\n")
        raise SystemExit
      elif(members_data["message"] == "Bad credentials"):
        print("Please verify GitHub credentials are correct in config.py")
        raise SystemExit
      else:
        print (members_data)
      raise SystemExit
    
    

def check_for_null(attribute, memberUrls):
  """Provides a list of Member urls that have [attribute] is null.
  
  param attribute to check for null value
  params memberUrls List of member urls to check
  return list of member urls with null [attribute] field
  """
  attributeNotFound =[]
  
  for url in memberUrls:
    member_data = utils.get_json(url)
    
    if member_data[attribute] is None:
        #TODO: TBD Could grab email here if speed was an issue
        attributeNotFound.append(url)
  return attributeNotFound