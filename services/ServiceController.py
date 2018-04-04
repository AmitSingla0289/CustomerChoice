# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from services.BestVPN import BestVPN
from services.CapterraCrawler import CapterraCrawler
from services.ForexbrokerzCrawler import ForexbrokerzCrawler
# from scrapy.selector import HtmlXPathSelector
from services.HostAdviceCrawler import HostAdviceCrawler
from services.HostingFactsCrawler import HostingFactsCrawler
from services.ResellerRatingCrawler import ResellerRatingCrawler
from model.Response import Response
from services.SiteJabberCrawler import SiteJabberCrawler
from services.WhoIsHostingCrawler import WhoIsHostingCrawler
from model.Servicemodel import final_json
import json
from restapis import Login
final_dict_reviews= {}
dict_url={}

class ServiceController(scrapy.Spider):
    start_urls = []
    def __init__(self,url):
        for link in url:
            self.start_urls.append(link["url"])
            category = link["Category"];
            service_name = link["ServiceName"]
            dict_url[link["url"]]={"Category":category,
                      "Service Name":service_name}
            response = Response("Service");
            response.Service_Name = service_name
            response.Category = category
            response.URL = link["url"]
            final_json[service_name]={"response":response}
    def closed(self, reason):
        #with open("reviews.json","w") as f:
        #    json.dump(final_json,f)
        str1 = ""
        dictionary = {}
        buisness_units = []
        for k, v in final_json.items():
            responselist = []
            responselist.append(v["response"].dump())
            dictionary[k]={"scrapping_website_name":k,"scrapping_website_url":v["response"].URL,"response":responselist}
            buisness_units.append(dictionary[k])
        Login.postReview({"business_units":buisness_units})
        with open("reviews.json","w") as f:
            json.dump({"business_units":buisness_units},f)
    def parse(self, response):
        self.log('I just visited: ' + response.url)
        dict_reviews = {}
        reviews= []
        if(response.xpath('//div[@class="user-review-content"]')):
            crawler = HostingFactsCrawler()
        elif(response.xpath('//div[@class="review-summary"]')):
            crawler = HostAdviceCrawler()
        elif(response.xpath('//div[@class="comment pure-u-1 wcc"]')):
            crawler = WhoIsHostingCrawler()
        elif(response.xpath('//div[@class="review "]/p')):
#sitejabber
            crawler = SiteJabberCrawler()
        elif(response.xpath('//div[@class="comment-content"]')):
            crawler = BestVPN()

            #bestvpn
        elif(response.xpath('//p[@class="review-body"]')):
            crawler = ResellerRatingCrawler()

            #resellerrating

        elif(response.xpath('//div[@class="review-comments  color-text"]')):
            crawler = CapterraCrawler()

            #capterrra


        elif(response.xpath('//div[@class="review_top"]/p')):
            print("Reviews from Forexbrokerz.com")
            #forexbrokerz
            crawler = ForexbrokerzCrawler()




        else:
            print ("kuch nhi mila")

        crawler.crawl(response, dict_url[response.url]["Category"], dict_url[response.url]["Service Name"])
            
    
def crawl_services(urls):
   process = CrawlerProcess(get_project_settings())
   process.crawl(ServiceController,urls)
   process.start()
   #print final_dict_reviews

   # with open("reviews.json","w") as f:
   #          json.dump(final_dict_reviews,f)
   # print("Writing json file")