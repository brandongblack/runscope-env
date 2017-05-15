# 2017-05-05
# Script to export a Runscope Environment
# Will write to a file JSON configuration of an Environment
# See https://www.runscope.com/docs/api/environments for 
# Runscope Documentation
# usage: python runscope_export_env.py
# will export a file with name of the environment to current directory
# For more on getting a Runscope Token, read here: 
# https://www.runscope.com/docs/api/authentication
# You can use the personal access token when you have
# created the application

import requests
import json
from runscope_config import *

url = 'https://api.runscope.com/buckets/' + master_bucket_key + '/environments/' + master_env_id
headers = dict(Authorization='Bearer ' + runscope_token)
r = requests.get(url, headers=headers)
env_name = r.json()["data"]["name"]
g = open(env_name + '.json', 'w')
g.write(r.text)
