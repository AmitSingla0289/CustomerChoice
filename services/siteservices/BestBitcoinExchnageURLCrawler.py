from scrapy import Spider, Request
from lxml import etree

from services.BestBitcoinExchange import BestBitcoinExchange


urlssss = []
class BestBitcoinExchangeURLCrawler(Spider):
    def __init__(self,category):
        self.url_list = []
        self.category = category
    def parsing(self, response):
        return self.crawl(response)
    def crawl(self, response):
        url = []
        urlnext = []
        servicelistnext = []
        servicelist= []

        url = response.xpath("//div[@class='entry overview provider']/a[@class='title']/@href").extract()
        serviceList = response.xpath("//div[@class='entry overview provider']/a[@class='title']/text()").extract()
        for content in serviceList:
            c= content.split(' ')
            servicelist.append(c[0])



        print("serviceList  ", len(servicelist), servicelist)
        print("URL ", len(url), url)
        i=0


        while i< len(url):
            crawler = BestBitcoinExchange(self.category, servicelist[i], url[i])
            yield Request(url=url[i], callback=crawler.parsing)
            # yield response.follow(url=url[i], callback=crawler.parsing)
            # print(url[i][j])
            i=i+1
        # next_page = response.xpath("//nav[@class='navi postnavi']/div[@class='next']/a/@href").extract()
        # if next_page is not None:
        #     if len(next_page)>0:
        #         next_page_url = "".join(next_page)
        #         if next_page_url and next_page_url.strip():
        #             yield Request(url=next_page_url, callback=self.parsing)
