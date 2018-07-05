# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue

import scrapy
from scrapy import Request
from scrapy.crawler import  CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from services.siteservices.SiteJabberURLCrawler import SiteJabberURLCrawler
from services.siteservices.HostingFactsURLCrawler import HostingFactsURLCrawler
from services.siteservices.HighyaURLCrawler import HighyaURLCrawler
from services.siteservices.AlterNativeToURLCrawler import AlterNativeToURLCrawler
from services.siteservices.SeniorDatingExpertURLCrawler import SeniorDatingExpertURLCrawler
from services.siteservices.TravelSiteCriticURLCrawler import TravelSiteCriticURLCrawler
from services.siteservices.NetBusinessRatingURLCrawler import NetBusinessRatingURLCrawler
from services.siteservices.ReviewCentreURLCrawler import ReviewCentreURLCrawler
from services.siteservices.ViewpointsURLCrawler import ViewPointsURLCrawler
from services.siteservices.CapterraURLCrawler import CapterraURLCrawler
from services.siteservices.BuyBitcoinWithCreditCardURLCrawler import BuyBitcoinWithCreditCardURLCrawler
from services.siteservices.AnblikURLCrawler import AnblikCrawlerURLCrawler
from services.siteservices.CoinJabberURLCrawler import CoinJabberURLCrawler
from services.siteservices.FreeDatingHelperURLCrawler import FreeDatingHelperURLCrawler
from services.SiteJabberCrawler import SiteJabberCrawler
from services.HostingFactsCrawler import HostingFactsCrawler
from services.HighYaCrawler import HighYaCrawler
from services.AlterNativeTo import AlterNativeTo
from services.SeniorDatingExpert import SeniorDatingExpert
from services.TravelSiteCritic import TravelSiteCritic
from services.NetBusinessRating import NetBusinessRating
from services.ReviewCentre import ReviewCentre
from services.ViewPoints import ViewPoints
from services.CapterraCrawler import CapterraCrawler
from services.BuyBitcoinsWithCreditCardCrawler import BuyBitcoinsWithCreditCardCrawler
from services.AnblikCrawler import AnblikCrawler
from services.CoinJabber import CoinJabber
from services.hostAdvisor import hostAdvisor
from services.FreeDatingHelperCrawler import FreeDatingHelperCrawler
from services.siteservices.bestdatingreviews import BestDatingReviewsCrawlerFactory

final_dict_urls= {}
dict_url = {}
class SiteServiceListController(scrapy.Spider):
    start_urls = []

    def __init__(self, link):
        if (len(self.start_urls) > 0):
            self.start_urls.pop(0)
        self.start_urls.append(link["url"])
        category = link["Category"];
        dict_url[link["url"]] = {"Category": category}

    def closed(self, reason):
        pass

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers,meta={'dont_merge_cookies': True})

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        if ('sitejabber.com' in response.url):
            if('reviews' in response.url):
                service  = response.url.split("/");
                serviceName = service[len(service)-1];
                print(" Servicesssss   ", serviceName)
                crawler = SiteJabberCrawler( dict_url[response.url]["Category"],serviceName,response.url)
            else:
                crawler = SiteJabberURLCrawler(dict_url[response.url]["Category"])
        elif('hostingfacts.com' in response.url):
            if ('reviews' in response.url):
                service = response.url.split("/");
                serviceName = service[len(service) - 1];
                print(" Servicesssss   ", serviceName)
                crawler = HostingFactsCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = HostingFactsURLCrawler(dict_url[response.url]["Category"])
        elif ('highya.com' in response.url):
            if ('reviews' in response.url):
                service = response.url.split("/");
                serviceName = service[len(service) - 1];
                print(" Servicesssss   ", serviceName)
                crawler = HighYaCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = HighyaURLCrawler(dict_url[response.url]["Category"])
        elif ('alternativeto.net' in response.url):
            if ('browse' in response.url):
                crawler = AlterNativeToURLCrawler(dict_url[response.url]["Category"])
            else:
                service = response.url.split("/");
                serviceName = service[len(service) - 1];
                print(" Servicesssss   ", serviceName)
                crawler = AlterNativeTo(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('seniordatingexpert.com' in response.url):
            if len(response.url.split('/')) > 5:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = SeniorDatingExpert(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = SeniorDatingExpertURLCrawler(dict_url[response.url]["Category"])
        elif ('travelsitecritic.com' in response.url):
            if len(response.url.split('/')) > 5:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = TravelSiteCritic(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = TravelSiteCriticURLCrawler(dict_url[response.url]["Category"])
        elif ('netbusinessrating.com' in response.url):
            if ('search' in response.url):
                crawler = NetBusinessRatingURLCrawler(dict_url[response.url]["Category"])
            else:
                service = response.url.split("/");
                serviceName = service[len(service) - 1];
                print(" Servicesssss   ", serviceName)
                crawler = NetBusinessRating(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('reviewcentre.com' in response.url):
            if('searchstring' not in response.url):
                service  = response.url.split("/");
                serviceName = service[len(service)-1];
                print(" Servicesssss   ", serviceName)
                crawler = ReviewCentre( dict_url[response.url]["Category"],serviceName,response.url)
            else:
                crawler = ReviewCentreURLCrawler(dict_url[response.url]["Category"])
        elif ('viewpoints.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = ViewPoints(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = ViewPointsURLCrawler(dict_url[response.url]["Category"])
        elif ('capterra.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = CapterraCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = CapterraURLCrawler(dict_url[response.url]["Category"])
        elif ('buybitcoinswithcreditcard.net' in response.url):
            if '?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = BuyBitcoinsWithCreditCardCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = BuyBitcoinWithCreditCardURLCrawler(dict_url[response.url]["Category"])
        elif ('anblik.com' in response.url):
            if '?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = AnblikCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = AnblikCrawlerURLCrawler(dict_url[response.url]["Category"])
        elif ('coinjabber.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = CoinJabber(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = CoinJabberURLCrawler(dict_url[response.url]["Category"])
        elif ('hostadvisor.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = hostAdvisor(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('freedatinghelper.com' in response.url):
            if '?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = FreeDatingHelperCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = FreeDatingHelperURLCrawler(dict_url[response.url]["Category"])
        elif ('bestdatingreviews.org' in response.url):
            crawler = BestDatingReviewsCrawlerFactory.getCrawler(response.url,dict_url[response.url]["Category"])


        else:
            print("Found Nothing")
        if (crawler != None):
            return crawler.crawl(response)

def f(q, ):
    try:
        configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
        runner = CrawlerRunner()
        deferred = runner.crawl(SiteServiceListController, q[1])
        deferred.addBoth(lambda _: reactor.stop())
        reactor.run()
        q[0].put(None)
    except Exception as e:
        q[0].put(e)

def run_spider(urls):
    q = Queue()
    p = Process(target=f, args=([q, urls],))
    p.start()
    result = q.get()
    p.join()
    if result is not None:
        raise result
def crawl_services1(urls):
    for i in urls:
        run_spider(i)

