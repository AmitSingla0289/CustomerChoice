from scrapy import Spider, Request
from lxml import etree

from services.MacUpdate import MacUpdate


urlssss = []
class MacUpdateURLCrawler(Spider):
    def __init__(self,category):
        self.url_list = []
        self.category = category
    def parsing(self, response):
        return self.crawl(response)
    def crawl(self, response):
        url = []
        urlnext = []
        servicelistnext = []
        serviceList= []

        url = response.xpath("//a[@class='js-search-suggest-app stwb-boxcol']/@href").extract()
        servicelist = response.xpath("//a[@class='js-search-suggest-app stwb-boxcol']/h4[@class='stwbbc-appname']/text()").extract()



        print("serviceList  ", len(servicelist), servicelist)
        print("URL ", len(url), url)
        i=0


        while i< len(url):
            crawler = MacUpdate(self.category, servicelist[i], url[i])
            # yield Request(url=url[i], callback=crawler.parsing)
            yield response.follow(url=url[i], callback=crawler.parsing)
            # print(url[i][j])
            i=i+1
        # next_page = response.xpath("//li[@class='pagination-next']/a[@class='hasTooltip pagenav']/@href").extract()
        # if next_page is not None:
        #     next_page_url = "".join(next_page)
        #     if next_page_url and next_page_url.strip():
        #         yield response.follow(url=next_page_url, callback=self.parsing)
