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


def listMembers(orgs):
  """Provides a list of Member urls per organizations.
  
  param orgs either a list of urls pointing to organizations or a single org name
  return list of member urls
  """
  members =[]
  
  
  if isinstance(orgs, list):
    for url in orgUrls:
      #append /member to url - member_url is not valid canidate without a member list
      url = url + "/members"
      members_data = utils.get_json(url)

      for member in members_data:
        members.append(member["url"])
    return members
  
  else:
    #build url from input org name and return member list
    url = "https://api.github.com/orgs/" + orgs
    members_data = utils.get_json(url)

    for member in members_data:
      members.append(member["url"])
    return members
    

def checkForNull(attribute, memberUrls):
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