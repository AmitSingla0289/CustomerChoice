import requests
import json

param = {
  "email": "data_miner@example.com",
  "password": "ATBdm9",
  "grant_type": "password"
}
url = ""
SUCCESS_STATUS = 200
base_url ="http://52.0.49.246/api/v1/"
def login():
  response = requests.post( base_url+"users/login", param)
  data = response.json()
  return data

def postReview(review):
  data =login()
  print(data['data']['token']['access_token'])
  header = {'Content-Type':'application/json','Authorization':'bearer '+data['data']['token']['access_token']}
  print(header)
  r = requests.post(base_url+"data_miner/store_data",data=json.dumps(review),headers=header)
  if(r.status_code ==  SUCCESS_STATUS):
    print(r.text)