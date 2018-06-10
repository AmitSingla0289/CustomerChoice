from model.Servicemodel import ServiceRecord
from scrapy import Spider, Request
from lxml import etree



class NetBusinessRating(Spider):

    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        reviews1 = []
        self.category = category
        self.servicename = servicename
        # https: // www.webhostinghero.com / reviews / bluehost /
        data = response.xpath("//div[@id='posted']/div[@class='blc']").extract()
        print len(data), data
        for node in response.xpath(
                "//div[@id='posted']/div[@class='blc']/div[@class='mc text']"):
            reviews.append(node.xpath('string()').extract());
        # ratings = response.xpath("//ol[@class='commentlist']/li/div[@class='commbox']/div[@class='comment-content-withreview']/div[@class='user_reviews_view simple_color']/div[@class='user_reviews_view_box']/div[@class='user_reviews_view_score']/div[@class='userstar-rating']/span").extract()
        dates = response.xpath("//div[@id='posted']/div[@class='blc']/div[@class='mc'][1]/div[@class='postingUser']/div[@class='clock icon-clock']/@title").extract()
        authors = response.xpath("//div[@class='blc']/div[@class='mc'][1]/div[@class='postingUser']/span[@class='help nopadding']/a[@class='titleLink']/text()").extract()
        img_src = response.xpath(
            "//div[@id='posted']/div[@class='blc']/div[@class='mc'][1]/a[@class='blcAvatar']/img/@src").extract()
        # headings = response.xpath("//div[@class='pr-review-wrap']/div[@class='pr-review-rating-wrapper']/div[@class='pr-review-rating']/p[@class='pr-review-rating-headline']/text()").extract()
        website_name = response.xpath("//div[@class='container ariane']/ol/li[1]/a/@href").extract()
        print("Reviews ", len(reviews), reviews)
        print("Authors ", len(authors), authors)
        # print("Rating ", len(ratings), ratings)
        print("Dates ", len(dates), dates)
        print("img_src ", len(img_src), img_src)
        print("websites ", len(website_name), website_name)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, None, None, dates[item], authors[item], category,
                                         servicename, reviews[item], img_src, website_name)
            servicename1.save()





