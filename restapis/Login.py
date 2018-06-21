import threading
import os
import requests
import json
from product.ProductController import crawlAmazon

param = {
  "email": "data_miner@example.com",
  "password": "ATBdm9",
  "grant_type": "password"
}
url = ""
SUCCESS_STATUS = 200
base_url ="http://52.0.49.246/api/v1/"
custom_base_url = ""
def login():
  response = requests.post( base_url+"users/login", param)
  print(response)
  data = response.json()
  return data
def postReview(review):
  if(custom_base_url == ""):
      pass
    # data =login()
    # header = {'Content-Type': 'application/json', 'Authorization': 'bearer ' + data['data']['token']['access_token']}
    # requests.post(base_url + "data_miner/store_data", data=json.dumps(review), headers=header)
  else:
    header = {'Content-Type': 'application/json'}
    requests.post(custom_base_url, data=json.dumps(review), headers=header)
def crawling():
  data = login()
  header = {'Authorization': 'bearer ' + data['data']['token']['access_token']}
  response_website = requests.get(base_url + "scrapping_websites", headers=header)
  website_data = response_website.json()
  website_list = []
  amazon_list =[]
  i =0
  for element in (website_data['data']['scrapping_websites']):
    i = i+1
    if("www.amazon." in url):
      amazon_list.append(url)
    else:
      website_list.append({"ServiceName": "Bluehost"+str(i),
                         "Category": "Hosting Service"+str(i),
                         "url": element['url']})
  crawl_services1(website_list)
  crawlAmazon(amazon_list)
def google_search_post(callbackurl,search):
  header = {'Content-Type': 'application/json'}
  requests.post(callbackurl, data=json.dumps(search), headers=header)
def crawlURL(url,responseURL,categoryName):
    website_list = []
    amazon_list = []
    if ("www.amazon." in url):
        amazon_list.append(url)
    else:
        website_list.append({"ServiceName": "",
                                 "Category": categoryName,
                                 "url": url})
    global  custom_base_url
    custom_base_url = responseURL
    crawl_services1(website_list)
    crawlAmazon(amazon_list)

class MyThread(threading.Thread):
  def __init__(self, id,categoryName,url,callback_url):
    super(MyThread, self).__init__()
    self.responseURL = callback_url
    self.URL = url
    self.categoryName = categoryName
  def run(self):
    print("Mythread start")
    if(self.URL == ""):
      crawling()
    else:
      crawlURL(self.URL,self.responseURL,self.categoryName)