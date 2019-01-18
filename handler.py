import json
import requests
import os

url_start = os.getenv('circleci_url', '1')
api_token =  os.getenv('api_token', '2')
secret_token = os.getenv('secret_token', 'abc123')

def circleci(event, context):
    
    payload = json.loads(event['body'])
    secret=payload['secret']

    if secret == secret_token:
        print("Inner loop...")
        url=url_start+'?circle-token='+api_token
        # EXAMPLE circleci curl
        # curl -X POST --header "Content-Type: application/json"  \
        # https://circleci.com/api/v1.1/project/github/Sortterfi/sortter/build\?circle-token\=TOKEN
        
        # curl -X POST --header "Content-Type: application/json" -d '{"branch":"master"}'
        # https://circleci.com/api/v1.1/project/:vcs-type/:username/:project/build?circle-token=:token
        #https://circleci.com/api/v1.1/project/github/Sortterfi/sortter/build
        #r=requests.post(url)
       
        headers = {
            "Content-Type": "application/json"
        }
        
        data = {
            "branch":"master"
        }

        r=requests.post(url,headers=headers,json=data)
  

    return {
        "statusCode": r.status_code,
        "body": json.dumps('It worked!')
    }
