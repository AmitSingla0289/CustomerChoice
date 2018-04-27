from model.Servicemodel import ServiceRecord
from scrapy import Spider, Request
from lxml import etree

class DatingWise(Spider):

    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        self.category = category
        self.servicename = servicename
        #https: // www.webhostinghero.com / reviews / bluehost /
        for node in response.xpath("//div[@class='tabBody']/ul[@id='commentsul']/li/div[@class='userComments']/div[@class='callout border-callout']"):
            reviews.append(node.xpath('string()').extract());
        ratings =  response.xpath("//div[@class='review_result']/div[@class='review_result_content']/div[@class='review_result_item']/div[@class='review-result-rating-main']").extract()
        dates = response.xpath("//div[@class='tabBody']/ul[@id='commentsul']/li/div[@class='userComments']/div[@class='userDetails']/div[@class='userLocation']/p[1]/span[@class='pIcn']/text()").extract()
        authors =  response.xpath("//div[@class='tabBody']/ul[@id='commentsul']/li/div[@class='userComments']/div[@class='userDetails']/div[@class='userLocation']/p[1]/span[@class='pIcn']/span/a/text()").extract()
        headings = response.xpath("//div[@class='tabBody']/ul[@id='commentsul']/li/div[@class='userComments']/div[@class='userDetails']/div[@class='userLocation']/p[@class='clear']/span[@class='unRcmnded']/text()").extract()
        website_name =  response.xpath("/html/head/meta[9]/@content").extract()
        img_src = response.xpath("//div[@class='tabBody']/ul[@id='commentsul']/li/div/div/div[@class='userAvatar']/img/@src").extract()
        print("Reviews ", len(reviews), reviews)
        print("Headings ", len(headings), headings)
        print("Authors ", len(authors), authors)
        print("Rating ", len(ratings), ratings)
        print("Dates ", len(dates), dates)
        # print("Img_src ", len(img_src), img_src)
        for item in range(0, len(reviews)):
            servicename1 =ServiceRecord(response.url, None,None, dates[item], authors[item], category,
                          servicename, reviews[item], img_src,website_name)
            servicename1.save()

        next_page = response.xpath("//div[@class='pagination']/ul[@id='yw2']/li[@class='next']/a/@href").extract()
        if next_page is not None:
            next_page_url = "".join(next_page[0])
            print(next_page_url)
            if next_page_url and next_page_url.strip():
                yield response.follow(url=next_page_url,  callback=self.parsing)
