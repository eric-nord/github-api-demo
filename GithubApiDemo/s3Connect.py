__version__ = "0.0.1"
__author__ = "Eric Nord"

import datetime

import tinys3

import config

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
  
  response = conn.upload(datetimestamp + ' profiles_without_names',f,'github-api-demo')
  f.close()
  return response