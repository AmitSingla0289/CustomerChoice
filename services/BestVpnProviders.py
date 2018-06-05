from model.Servicemodel import ServiceRecord
from scrapy import Spider, Request
from utils.utils import getStarts



class BestPvnProviders(Spider):

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
                "//div[@class='wpcr3_review_item']/div[@class='wpcr3_item wpcr3_product']/div/blockquote[@class='wpcr3_content']"):
            reviews.append(node.xpath('string()').extract());
        ratings1 = response.xpath("//div[@class='wpcr3_item wpcr3_product']/div/div[@class='wpcr3_review_ratingValue']/div[@class='wpcr3_rating_style1']/div[@class='wpcr3_rating_style1_base ']/div/@style").extract()
        ratings = []
        j = 0
        while j < len(ratings1):
            c = int(getStarts(ratings1[j]))
            ratings.append((c) / 20.0)
            j = j + 1
        dates = response.xpath("//div[@class='wpcr3_item wpcr3_product']/div/div[@class='wpcr3_review_datePublished']/text()").extract()
        authors = response.xpath("//div[@class='wpcr3_item wpcr3_product']/div/div[@class='wpcr3_review_author']/span[@class='wpcr3_caps']/text()").extract()
        # img_src = response.xpath(
        #     "//div[@id='posted']/div[@class='blc']/div[@class='mc'][1]/a[@class='blcAvatar']/img/@src").extract()
        # headings = response.xpath("//div[@class='pr-review-wrap']/div[@class='pr-review-rating-wrapper']/div[@class='pr-review-rating']/p[@class='pr-review-rating-headline']/text()").extract()
        website_name = response.xpath("///head/meta[10]/@content").extract()
        print("Reviews ", len(reviews), reviews)
        print("Authors ", len(authors), authors)
        print("Rating ", len(ratings), ratings)
        print("Dates ", len(dates), dates)
        # print("img_src ", len(img_src), img_src)
        print("websites ", len(website_name), website_name)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], None, dates[item], authors[item], category,
                                         servicename, reviews[item], None, website_name)
            servicename1.save()





