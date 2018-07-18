from lxml import etree
from scrapy import Spider
from services.BestDatingReviews import BestDatingReviews
class BestDatingReviewsCrawlURL(Spider):
    URLXPATH = ".//dt/div[@class='all_sites_list_a']/a/text()"
    HREFPATH =  ".//dt/div[@class='all_sites_list_a']/a/@href"
    def __init__(self,category):
        self.url_list = []
        self.category = category

    def parsing(self, response):
        return self.crawl(response)

    def crawl(self, response):
        url = response.xpath("//dt/div[@class='all_sites_list_a']/a/@href").extract()
        servicelist = response.xpath("//dt/div[@class='all_sites_list_a']/a/text()").extract()
        print("serviceList  ", len(servicelist), servicelist)
        print("URL ", len(url), url)
        i = 0
        while i < len(url):
            crawler = BestDatingReviews(self.category, servicelist[i], url[i])
            # yield Request(url=url[i], callback=crawler.parsing)
            yield response.follow(url=url[i], callback=crawler.parsing)
            i = i + 1
        next_page = response.xpath(
                "//div[@class='page_cut']/a/@href").extract()
        if next_page is not None:
            for next_page_url in next_page:
                yield response.follow(url=next_page_url, callback=self.parsing)

