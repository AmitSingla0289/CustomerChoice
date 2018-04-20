# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from services.vpnRanks import vpnRanks
from services.vpnMentor import vpnMentor
from services.restorePrivacy import restorePrivacy
from services.affPaying import affPaying
from services.webHostingmedia import webHostingmedia
from services.hostAdvisor import hostAdvisor
from services.hostingCharges import hostingCharges
from services.top11Hosting import top11Hosting
from services.ThewebmasterCrawler import ThewebmasterCrawler
from services.yelpCrawler import yelpCrawler
from services.consumerAffairsCrawler import consumerAffairsCrawler
from services.HighYaCrawler import HighYaCrawler
from services.whtop import whtop
from services.bestVPNForYou import bestVPNForYou
from services.webshostingFatcow import webshostingFatcow
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
import restapis.Login
import json

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
            # restapis.Login.postReview({"business_units":buisness_units})
        with open("reviews.json","w") as f:
            json.dump({"business_units":buisness_units},f)
    def parse(self, response):
        self.log('I just visited: ' + response.url)
        dict_reviews = {}
        reviews= []
        print("xpath     ", response.xpath)
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

        elif(response.xpath('//div[@class="comments_user_comment"]')):
            print("Reviews from webshosting")
            crawler = webshostingFatcow()

        elif (response.xpath('//div[@class="comment-text"]')):
            print("Reviews from bestvpnforyou.com")
            crawler = bestVPNForYou()

        elif (response.xpath('//div[@class="review-main"]')):
            print("Reviews from whtop.com")
            crawler = whtop()


        elif (response.xpath(
                "//div[@class='left-col col-lg-8 col-lg']/div[@id='reviews']/ul[@class='no-list list-review']/li/span/div[@class='description']")):
            crawler = HighYaCrawler()

        elif (response.xpath(
                "//div[@class='campaign-reviews__regular-container js-campaign-reviews__regular-container']/div/div[@class='rvw-bd ca-txt-bd-2']/p")):
            crawler = consumerAffairsCrawler()

        elif ('yelp.com' in response.url):
            crawler = yelpCrawler()

        elif ('thewebmaster.com' in response.url):
            crawler = ThewebmasterCrawler()

        elif('/top11hosting.com' in response.url):
            crawler = top11Hosting()

        elif(response.xpath('//div[@class="review-one-all"]')):
            crawler = hostingCharges()

        elif (response.xpath('//div[@class="textHolder"]')):
            crawler = hostAdvisor()

        elif (response.xpath('//div[@class="customer-review"]')):
            crawler = webHostingmedia()

        elif (response.xpath('//div[@id="thecomments"]')):
            crawler = affPaying()

        elif (response.xpath('//div[@class="commentmetadata"]')):
            crawler = restorePrivacy()

        elif (response.xpath('//div[@class="review-item style_prevu_kit "]')):
            crawler = vpnMentor()

        elif (response.xpath('//div[@class="comment-body"]')):
            crawler = vpnRanks()



        else:
            print ("kuch nhi mila")
        print(dict_url)
        print(response.url)
        return crawler.crawl(response, dict_url[response.url]["Category"], dict_url[response.url]["Service Name"])
            
    
def crawl_services(urls):
   process = CrawlerProcess(get_project_settings())
   process.crawl(ServiceController,urls)
   process.start()
