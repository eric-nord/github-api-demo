__version__ = '0.0.1'
__author__ = 'Eric Nord'

import json

import requests
from requests.auth import HTTPBasicAuth

import config

def get_json(url):
  """Provides Python Object representation of JSON response given a url
  
  Args:
  url - location of recources  
  
  Returns:
    json HTTP response example:
    {
      "login": "Picolab",
      "id": 10158417,
      "url": "https://api.github.com/user/orgs",
    }
    
  """
  response = requests.get(url, auth=HTTPBasicAuth(config.username, config.password))
  data = json.loads(response.text)
  return data