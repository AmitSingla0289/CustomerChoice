from model.Servicemodel import ServiceRecord
from scrapy import Spider, Request
from utils.utils import getStarts


class TrustPilot(Spider):

    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        self.category = category
        self.servicename = servicename
        # https: // www.webhostinghero.com / reviews / bluehost /
        for node in response.xpath(
                "//div[@class='card']/div[@class='review-stack']/article/section[@class='review-card__content-section']/section[@class='content-section__review-info']/div[@class='review-info__body']/p[@class='review-info__body__text']"):
            reviews.append(node.xpath('string()').extract());
        ratings1 =  response.xpath("//div[@class='card']/div[@class='review-stack']/article/section[@class='review-card__content-section']/section[@class='content-section__review-info']/div[@class='review-info__header']/div[@class='review-info__header__verified']/div[1]/@class").extract()
        dates = response.xpath("//div[@class='card']/div[@class='review-stack']/article/section[@class='review-card__content-section']/section[@class='content-section__review-info']/div[@class='review-info__header']/div[@class='review-info__header__verified']/div[@class='header__verified__date']/time/@title").extract()
        authors = response.xpath("//div[@class='card']/div[@class='review-stack']/article/section[@class='review-card__content-section']/aside[@class='content-section__consumer-info']/a[@class='consumer-info']/div[@class='consumer-info__details']/h3[@class='consumer-info__details__name']/text()").extract()
        headings = response.xpath("//div[@class='card']/div[@class='review-stack']/article/section[@class='review-card__content-section']/section[@class='content-section__review-info']/div[@class='review-info__body']/h2[@class='review-info__body__title']/a[@class='link link--large link--dark']/text()").extract()
        website_name = response.xpath("/html/head/meta[9]/@content").extract()
        # img_src = response.xpath(
        #     "//div[@class='tabBody']/ul[@id='commentsul']/li/div/div/div[@class='userAvatar']/img/@src").extract()
        ratings = []
        i = 0
        while i < len(ratings1):
            ratings.append(getStarts(ratings1[i]))
            i = i + 1
        ratings = map(lambda foo: foo.replace('-', ''), ratings)
        print("Reviews ", len(reviews), reviews)
        print("Headings ", len(headings), headings)
        print("Authors ", len(authors), authors)
        print("Rating ", len(ratings), ratings)
        print("Dates ", len(dates), dates)\
        # print("Img_src ", len(img_src), img_src)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], headings[item], None, authors[item], category,
                                         servicename, reviews[item], None, website_name)
            servicename1.save()


