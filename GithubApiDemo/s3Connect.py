__version__ = "0.0.1"
__author__ = "Eric Nord"

import datetime

import requests

import config

try:
    import tinys3
except ImportError:
    print("'pip install tinys3' first please.\n" 
          "Also ensure you're running in Python 2")
    raise SystemExit

def upload(list):
  """Uploads list of links to user profiles
  
  params list list of user profile urls
  returns status code response from AWS S3 - Ok 200 = successful write
  """
  datetimestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
  
  f = open('profiles_without_names', 'w+')
  for item in list:
    f.write("%s\n" % item)

  conn = tinys3.Connection(
    config.AWS_ACCESS_KEY_ID, 
    config.AWS_SECRET_ACCESS_KEY, 
    tls=True, 
    endpoint='s3-us-west-2.amazonaws.com')
  
  try:
    response = conn.upload(datetimestamp + ' profiles_without_names',f,'github-api-demo')
  except requests.exceptions.HTTPError:
    print("\nUnable to connect to AWS S3 while storing user list\n"
          "Check AWS S3 credentials in config.py and\n"
          "verify AWS S3 user is in S3FullAccess security group in IAM\n")
    raise SystemExit
  f.close()
  return response