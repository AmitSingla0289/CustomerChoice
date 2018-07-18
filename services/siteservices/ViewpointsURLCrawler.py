
from lxml import etree
from product.amazon.helpers import make_request

from services.ViewPoints import ViewPoints


urlssss = []
class ViewPointsURLCrawler():
    def __init__(self,category):
        self.url_list = []
        self.category = category
    def parsing(self, response):
        return self.crawl(response)
    def crawl(self, response):
        root = etree.HTML(response)

        url = root.xpath(".//div[@class='productListingInfo']/a[@class='buttonLink primary readReviews']/@href")
        servicelist = root.xpath(".//div[@class='productListingInfo']/header[@class='productListingHeader']/h3/a/text()")


        print("serviceList  ", len(servicelist), servicelist)
        print("URL ", len(url), url)
        i=0


        while i< len(url):
            crawler = ViewPoints(self.category, servicelist[i], url[i])
            r = make_request("http://www.viewpoints.com"+url[i], False, False)
            crawler.crawl(r.content)
            i=i+1
        # next_page = root.xpath(
        #         ".//div[@class='sortBar resultsSortBar'][1]/div[@class='paginate']/a[@class='next']/@href")
        # if next_page is not None:
        #     next_page_url = "".join(next_page)
        #     if next_page_url and next_page_url.strip():
        #         print(type(next_page_url))
        #         print(next_page_url)
        #         r = make_request("http://www.viewpoints.com"+next_page_url, False, False)
        #         self.crawl(r.content)








