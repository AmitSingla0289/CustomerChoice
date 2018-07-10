from scrapy import Spider, Request
from lxml import etree

from services.ProductreviewCrawler import ProductreviewCrawler


urlssss = []
class ProductreviewURLCrawler(Spider):
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

        url = response.xpath("//div[@class='gsc-webResult gsc-result']/div[@class='gs-webResult gs-result']/div[@class='gsc-thumbnail-inside']/div[@class='gs-title']/a[@class='gs-title']/@href").extract()
        servicelist = response.xpath("//div[@class='gsc-webResult gsc-result']/div[@class='gs-webResult gs-result']/div[@class='gsc-thumbnail-inside']/div[@class='gs-title']/a[@class='gs-title']/text()")


        print("serviceList  ", len(servicelist), servicelist)
        print("URL ", len(url), url)
        i=0


        # while i< len(url):
        #     if('reviews' in url[i]):
        #         crawler = ProductreviewCrawler(self.category, servicelist[i], url[i])
        #         # yield Request(url=url[i], callback=crawler.parsing)
        #         yield response.follow(url=url[i], callback=crawler.parsing)
        #         # print(url[i][j])
        #     i=i+1
        #     next_page = response.xpath(
        #         "//div[@id='left_column']/div[@class='navigation']/div[@class='paginator_next']/span/a[@class='button outline']/@href").extract()
        # if next_page is not None:
        #     next_page_url = "".join(next_page)
        #     if next_page_url and next_page_url.strip():
        #         print(type(next_page_url))
        #         print(next_page_url)
        #         # yield Request(url=next_page_url, callback=self.parse, dont_filter=True)
        #         yield response.follow(next_page_url, callback=self.parsing)






