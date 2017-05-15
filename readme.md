# Runscope Environment Export/Import Scripts

These two scripts are designed to facilitate copying of shared environments from Runscope.

# Prerequisites
To use these scripts, you need to get a Runscope Token.
For more on getting a Runscope Token, read here: [https://www.runscope.com/docs/api/authentication](https://www.runscope.com/docs/api/authentication) 
You can use the personal access token when you have created the application

# Configuration
Once you have the token, fill the variables in the runscope_config.py file

 ```master_bucket_key```:  The bucket key to export from   
 ```master_env_id```:  The UUID of the shared environment to export  
 ```runscope_token```:  Runscope API token  
  ```runscope_dest_bucket```:  The bucket to copy to  

# Usage

## Export
usage: `python export_env.py`
will export a file with name of the environment to current directory

## Import
usage: `python import_env.py <environmentname.json>`
