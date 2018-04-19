# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from services.BestVPN import BestVPN
from services.CapterraCrawler import CapterraCrawler
from services.ForexbrokerzCrawler import ForexbrokerzCrawler
# from scrapy.selector import HtmlXPathSelector
from services.HighYaCrawler import HighYaCrawler
from services.HostAdviceCrawler import HostAdviceCrawler
from services.HostingFactsCrawler import HostingFactsCrawler
from services.ResellerRatingCrawler import ResellerRatingCrawler
from model.Response import Response
from services.SiteJabberCrawler import SiteJabberCrawler
from services.WhoIsHostingCrawler import WhoIsHostingCrawler
from services.consumerAffairsCrawler import consumerAffairsCrawler
from services.yelpCrawler import yelpCrawler
from services.affgadgetsCrawler import AffgadgetsCrawler
from services.ProductreviewCrawler import ProductreviewCrawler
from services.ReviewDatingSitesCrawler import ReviewDatingSitesCrawler
from services.ThewebmasterCrawler import ThewebmasterCrawler
from model.Servicemodel import final_json
import json
from restapis import Login

final_dict_reviews = {}
dict_url = {}


class ServiceController(scrapy.Spider):
    start_urls = []

    def __init__(self, url):
        for link in url:
            self.start_urls.append(link["url"])
            category = link["Category"];
            service_name = link["ServiceName"]
            dict_url[link["url"]] = {"Category": category,
                                     "Service Name": service_name}
            response = Response("Service");
            response.Service_Name = service_name
            response.Category = category
            response.URL = link["url"]
            final_json[service_name] = {"response": response}

    def closed(self, reason):
        # with open("reviews.json","w") as f:
        #    json.dump(final_json,f)
        str1 = ""
        dictionary = {}
        buisness_units = []
        for k, v in final_json.items():
            responselist = []
            responselist.append(v["response"].dump())
            dictionary[k] = {"scrapping_website_name": k, "scrapping_website_url": v["response"].URL,
                             "response": responselist}
            buisness_units.append(dictionary[k])
        #Login.postReview({"business_units": buisness_units})
        with open("reviews.json", "w") as f:
            json.dump({"business_units": buisness_units}, f)

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        dict_reviews = {}
        reviews = []
        crawler = None
        '''if (response.xpath('//div[@class="user-review-content"]')):
            crawler = HostingFactsCrawler()
        elif (response.xpath('//div[@class="review-summary"]')):
            crawler = HostAdviceCrawler()
        elif (response.xpath('//div[@class="comment pure-u-1 wcc"]')):
            crawler = WhoIsHostingCrawler()
        elif (response.xpath('//div[@class="review "]/p')):
            # sitejabber
            crawler = SiteJabberCrawler()
        elif (response.xpath('//div[@class="comment-content"]')):
            crawler = BestVPN()
        elif (response.xpath('//p[@class="review-body"]')):
            crawler = ResellerRatingCrawler()
        elif (response.xpath('//div[@class="review-comments  color-text"]')):
            crawler = CapterraCrawler()
        elif (response.xpath('//div[@class="review_top"]/p')):
            crawler = ForexbrokerzCrawler()
        elif(response.xpath("//div[@class='left-col col-lg-8 col-lg']/div[@id='reviews']/ul[@class='no-list list-review']/li/span/div[@class='description']")):
            crawler = HighYaCrawler()
        if(response.xpath("//div[@class='campaign-reviews__regular-container js-campaign-reviews__regular-container']/div/div[@class='rvw-bd ca-txt-bd-2']/p")):
            crawler = consumerAffairsCrawler()
        elif('yelp.com' in response.url):
            crawler = yelpCrawler()'''
        if('affgadgets.com' in response.url):
            crawler = AffgadgetsCrawler()
        elif('productreview.com' in response.url):
            crawler = ProductreviewCrawler()
        elif('reviewsdatingsites.com' in response.url):
            crawler = ReviewDatingSitesCrawler()
        elif('thewebmaster.com' in response.url):
            crawler = ThewebmasterCrawler()
        else:
            print("kuch nhi mila")
        if(crawler!=None):
            crawler.crawl(response, dict_url[response.url]["Category"], dict_url[response.url]["Service Name"])


def crawl_services(urls):
    process = CrawlerProcess(get_project_settings())
    process.crawl(ServiceController, urls)
    process.start()
    # print final_dict_reviews

    # with open("reviews.json","w") as f:
    #          json.dump(final_dict_reviews,f)
    # print("Writing json file")
