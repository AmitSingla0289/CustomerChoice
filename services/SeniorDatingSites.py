from model.Servicemodel import ServiceRecord
from lxml import etree
from utils.utils import getStarts

class SeniorDatingSites():
    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        self.category = category
        self.servicename = servicename
        print("review from seniordatingsites.com")
        # https://www.highya.com/coinbase-reviews
        for node in response.xpath("//div[@id='main-inner']/ul[@id='user-reviews']/li/div[@class='userrev']/div[@class='user-review']"):
            reviews.append(node.xpath('string()').extract());
            ratings1 = response.xpath("//div[@id='main-inner']/ul[@id='user-reviews']/li/div[@class='userrev']/div[@class='user-stars']/img/@src").extract()
        i = 0
        ratings = []
        while i < len(ratings1):
            star = getStarts(ratings1[i])
            ratings.append(str(star))
            i = i + 1
        ratings = map(lambda foo: foo.replace('.', ''), ratings)
        # dates = response.xpath("//div[@class='review-sub-cntnr']/div[@class='review-one-all']/div[@class='review-profile']/div[@class='review-mid']/p/text()").extract()
        # img_src = response.xpath("//div[@class='logo-profile']/img/@src").extract()
        authors = response.xpath("//div[@id='main-inner']/ul[@id='user-reviews']/li/div[@class='userrev']/div[@class='user-name']/text()").extract()
        website_name = response.xpath("//div[@id='container']/div[@id='header']/div[@class='left eight columns']/div/a[@class='logo']/img/@title").extract()
        authors = map(lambda foo: foo.replace(u'Submitted By ', u''), authors)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], None, None, authors[item],
                                         category, servicename, reviews[item], None, website_name)
            servicename1.save()


