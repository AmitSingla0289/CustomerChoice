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
final_dict_reviews= {}
dict_url={}

class ServiceController(scrapy.Spider):
    start_urls = []
    def __init__(self,url,category):
        #with open("temp.txt", 'r') as f:
        self.start_urls.append(url)

        response = Response("Service");
        response.Service_Name = category["ServiceName"]
        response.Category = category["Category"]
        response.URL = self.start_urls
        final_json[""]={"Response":response}

    def closed(self, reason):
        #with open("reviews.json","w") as f:
        #    json.dump(final_json,f)
        str1 = ""
        dictionary = {}
        for k, v in final_json.items():
            dictionary[k]={"Response":v["Response"].dump()}

        with open("reviews.json","w") as f:
            json.dump(dictionary,f)
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

        crawler.crawl(response, "", "")
            
    
def crawl_services(urls,category):
   process = CrawlerProcess(get_project_settings())
   process.crawl(ServiceController,urls,category)
   process.start()
   #print final_dict_reviews

   # with open("reviews.json","w") as f:
   #          json.dump(final_dict_reviews,f)
   # print("Writing json file")