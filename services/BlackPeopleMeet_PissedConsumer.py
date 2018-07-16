from model.Servicemodel import ServiceRecord
from lxml import etree


#TODO ask sahil
from services.siteservices.BaseSiteURLCrawler import BaseSiteURLCrawler
class BlackPeopleMeet_PissedConsumer(BaseSiteURLCrawler):

    def __init__(self,category,servicename,url):

        self.category = category
        self.servicename = servicename
        self.link = {"ServiceName": servicename,
                "Category": category,
                "url": url}
        super(BlackPeopleMeet_PissedConsumer,self).__init__()
        self.createCategory(self.link)
        pass
    def parsing(self, response1):
        return self.crawl(response1)

    def crawl(self, response):
        reviews = []
        print("review from blackpeoplemeet.pissedconsumer.com")
        for node in response.xpath("//div[@class='middleware-review-container'][1]/div/div[@class='f-component-info']/div[@class='f-component-text']/div[@class='overflow-text']"):
            reviews.append(node.xpath('string()').extract());
        ratings = response.xpath("//body/section[@class='row body inside']/section[@class='comments-block']/section[@class='commentblock  ']/div[@class='comment  ']/ul[@class='postby']/li[2]/span[@class='smallStars']/@data-score").extract()
        dates = response.xpath("//div[@class='middleware-review-container']/div/div[@class='f-component-info']/div[@class='f-component-info-header']/time[@class='post-time secondary-info']/text()").extract()
        website_name = response.xpath("//div[@class='wpcr3_item_name']/a/text()").extract()
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], None, dates[item], None,
                                         self.category, self.servicename, reviews[item], None, website_name)
            self.save(servicename1)
        self.pushToServer()





