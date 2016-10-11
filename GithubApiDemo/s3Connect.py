import tinys3
import datetime
import config

def upload(list):
  datetimestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
  print(datetimestamp)
  f = open('profiles_without_names', 'w+')
  for item in list:
    f.write("%s\n" % item)

  conn = tinys3.Connection(
    config.AWS_ACCESS_KEY_ID, 
    config.AWS_SECRET_ACCESS_KEY, 
    tls=True, 
    endpoint='s3-us-west-2.amazonaws.com')
  
  return conn.upload(datetimestamp + ' profiles_without_names',f,'github-api-demo')