from model.Servicemodel import ServiceRecord
from scrapy import Spider, Request



class Anblik(Spider):

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
        for node in response.xpath(
                "//ol[@class='commentlist']/li/div/div[@class='comment-text']/div[@class='description']"):
            reviews.append(node.xpath('string()').extract());
        ratings = response.xpath("//div[@id='comments']/ol[@class='commentlist']/li/div/div[@class='comment-text']/div[@class='star-rating']/span/strong/text()").extract()
        dates = response.xpath("//ol[@class='commentlist']/li/div/div[@class='comment-text']/p[@class='meta']/time[@class='woocommerce-review__published-date']/text()").extract()
        authors = response.xpath("//ol[@class='commentlist']/li/div/div[@class='comment-text']/p[@class='meta']/strong[@class='woocommerce-review__author']/text()").extract()
        img_src = response.xpath(
            "//ol[@class='commentlist']/li/div/div[@class='img-thumbnail']/img/@src").extract()
        # headings = response.xpath("//div[@class='pr-review-wrap']/div[@class='pr-review-rating-wrapper']/div[@class='pr-review-rating']/p[@class='pr-review-rating-headline']/text()").extract()
        website_name = response.xpath("//div[@class='header-main']/div[@class='container']/div[@class='header-center']/div[@class='logo']/a/@href").extract()
        print("Reviews ", len(reviews), reviews)
        print("Authors ", len(authors), authors)
        print("Rating ", len(ratings), ratings)
        print("Dates ", len(dates), dates)
        print("img_src ", len(img_src), img_src)
        print("websites ", len(website_name), website_name)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], None, dates[item], authors[item], category,
                                         servicename, reviews[item], img_src, website_name)
            servicename1.save()





