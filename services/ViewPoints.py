from time import sleep

from model.Servicemodel import ServiceRecord
from scrapy import Spider, Request
from utils.utils import getStarts
from services.siteservices.BaseSiteURLCrawler import BaseSiteURLCrawler
from lxml import etree
from product.amazon.helpers import make_request

# http://www.viewpoints.com/Kayak-com-reviews
class ViewPoints(BaseSiteURLCrawler):

    def __init__(self,category,servicename,url):

        self.category = category
        self.servicename = servicename
        self.link = {"ServiceName": servicename,
                "Category": category,
                "url": url}
        super(ViewPoints,self).__init__()
        self.createCategory(self.link)
        pass
    def parsing(self, response1):
        return self.crawl(response1)

    def crawl(self, response):
        reviews = []
        response = response.replace('<br>',' ').replace('<br />', ' ')
        root1 = etree.HTML(response)
        print(" in viewPoints   " ,self.link["url"])
        # data = root1.xpath(".//div[@class='pr-contents-wrapper']")
        for node in root1.xpath(".//div[@class='pr-review-wrap']/div[@class='pr-review-main-wrapper']/div[@class='pr-review-text']/p[@class='pr-comments']"):
            reviews.append(node.xpath('string()'))
            # for node in root.xpath(
            #         ".//div[@class='pr-review-wrap']/div[@class='pr-review-main-wrapper']/div[@class='pr-review-text']/p[@class='pr-comments']/text()"):
            #     reviews.append(node.xpath('string()'));


        ratings =  root1.xpath(".//div[@class='pr-review-wrap']/div[@class='pr-review-rating-wrapper']/div[@class='pr-review-rating']/span[@class='pr-rating pr-rounded']/text()")
        dates = root1.xpath(".//div[@class='pr-review-wrap']/div[@class='pr-review-rating-wrapper']/div[@class='pr-review-author-date pr-rounded']/text()")
        authors = root1.xpath(".//div[@class='pr-review-wrap']/div[@class='pr-review-author']/div[@class='pr-review-author-info-wrapper']/p[@class='pr-review-author-name']/span/text()")
        headings = root1.xpath(".//div[@class='pr-review-wrap']/div[@class='pr-review-rating-wrapper']/div[@class='pr-review-rating']/p[@class='pr-review-rating-headline']/text()")
        website_name = "viewpoints.com"
        # img_src = response.xpath(
        #     "//div[@class='tabBody']/ul[@id='commentsul']/li/div/div/div[@class='userAvatar']/img/@src").extract()

        print("Reviews ", len(reviews) )
        print("Authors ", len(authors) )
        print("ratings ", len(ratings))
        print("Heading ", len(headings))
        print("Dates ", len(dates))

        print("websites ", len(website_name), website_name)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(self.link["url"], ratings[item], headings[item], None, authors[item], self.category,
                                         self.servicename, [reviews[item]], None, website_name)
            self.save(servicename1)
        next_page = root1.xpath(
            ".//div[@class='pr-page-nav-wrapper']/p[@class='pr-page-nav']/span[@class='pr-page-next']/a/@href")
        if next_page is not None:
            next_page_url = "".join(next_page)
            if next_page_url and next_page_url.strip():
                print(type(next_page_url))
                print("  urlllllllll  "+next_page_url)
                r = make_request("http://www.viewpoints.com"+next_page_url, False, False)
                self.crawl(r.content)
                # yield Request(url=next_page_url, callback=self.parse, dont_filter=True)
                # sleep(5)
                # yield response.follow(next_page_url, callback=self.parsing)

        self.pushToServer()


