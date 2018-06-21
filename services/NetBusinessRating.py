from model.Servicemodel import ServiceRecord
from scrapy import Spider, Request
from lxml import etree


# https://netbusinessrating.com/en/review-17955-localbitcoinscom
class NetBusinessRating(Spider):

    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)
# TODO: only got some reviews not all from other page
    def crawl(self, response, category, servicename):
        reviews = []
        reviews1 = []
        self.category = category
        self.servicename = servicename

        data = response.xpath("//div[@id='posted']/div[@class='blc']").extract()

        for node in response.xpath(
                "//div[@id='scn']/div[@id='posted']/div[@class='blc ']/div[@class='mc text']"):
            reviews.append(node.xpath('string()').extract());
        ratings1 = response.xpath("//div[@id='posted']/div[@class='blc ']/div[@class='mc'][1]/div[@class='postingUser']").extract()
        dates = response.xpath("//div[@id='posted']/div[@class='blc ']/div[@class='mc'][1]/div[@class='postingUser']/div[@class='clock icon-clock']/@title").extract()
        authors = response.xpath("//div[@id='posted']/div[@class='blc ']/div[@class='mc']/div[@class='postingUser']/span[@class='help nopadding']/a[@class='titleLink']/text()").extract()
        img_src = response.xpath(
            "//div[@class='screenshotContainer']/img[@class='screenshot']/@src").extract()
        # headings = response.xpath("//div[@class='pr-review-wrap']/div[@class='pr-review-rating-wrapper']/div[@class='pr-review-rating']/p[@class='pr-review-rating-headline']/text()").extract()
        website_name = response.xpath("//div[@class='container ariane']/ol/li[1]/a/@href").extract()
        ratings2 = []
        ratings = []
        for content in ratings1:
            root = etree.HTML(content)
            if(len(root.xpath("//span/span/@class"))>0):
                ratings2.append(root.xpath("//span/span/@class"))
            else:
                ratings2.append("")
        i=0
        while i < len(ratings2):
            ratings2[i] = map(lambda foo: foo.replace('icon-star', ''), ratings2[i])
            ratings2[i] = map(lambda foo: foo.replace('-', ''), ratings2[i])
            j=0
            c = 0
            while j< len(ratings2[i]):
                if(ratings2[i][j]=='3'):
                    c= c+1
                j= j+1
            ratings.append(c)

            i = i +1
        print("Reviews ", len(reviews), reviews)
        print("Authors ", len(authors), authors)
        print("Rating ", len(ratings), ratings)
        print("Dates ", len(dates), dates)
        print("img_src ", len(img_src), img_src)
        print("websites ", len(website_name), website_name)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, None, None, dates[item], authors[item], category,
                                         servicename, reviews[item], img_src, website_name)
            servicename1.save()





