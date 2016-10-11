"""
NAme
does this
"""
__version__ = "0.0.1"
__author__ = "Eric Nord"
__all__ [,,,] # for import *

import json
import config
import requests
from requests.auth import HTTPBasicAuth

def get_orgs():
  """
  Provides list of organizations the user is associated with
  Includes private and public members
  """
  orgUrls = []
  orgs = requests.get('https://api.github.com/user/orgs', 
                      auth=HTTPBasicAuth(config.username, config.password))
  
  orgs_data = json.loads(orgs.text)
  
  for org in orgs_data:
    orgUrls.append(org["url"])
  return orgUrls