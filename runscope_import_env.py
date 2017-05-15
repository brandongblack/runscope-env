# 2017-05-05
# Script to import a Runscope Environment
# Will read a JSON file that is Environment setting
# See https://www.runscope.com/docs/api/environments for 
# Runscope Documentation
# usage: python import_env.py <environmentname.json>
# For more on getting a Runscope Token, read here: 
# https://www.runscope.com/docs/api/authentication
# You can use the personal access token when you have
# created the application

import sys
import json
import requests
from runscope_config import *

url = 'https://api.runscope.com/buckets/' + runscope_dest_bucket + '/environments'



def upload_env(file_name):
	with open(file_name,'r') as myfile:
		env_data = myfile.read()
		env_data =json.loads(env_data)

	headers = dict(Authorization='Bearer ' + runscope_token)
	r = requests.post(url, headers=headers, json=env_data['data'])
	if r.status_code == 201:
		print 'Success - uploaded "' + env_data['data']['name'] + '" to bucket ' + runscope_dest_bucket
	else:
		print 'Failure - ' + r.text


##------- Run the function above
inputfile = str(sys.argv[1])
upload_env(inputfile)

