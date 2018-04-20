from model.Servicemodel import ServiceRecord
from lxml import etree
class affPaying():
    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        self.category = category
        self.servicename = servicename
        print("review from affPaying.com")
        # https://www.highya.com/coinbase-reviews
        for node in response.xpath("//div[3]/p[1]"):
            reviews.append(node.xpath('string()').extract());
        ratings = response.xpath("//div[@class='s_rate_mid']/span/meta[@itemprop='ratingValue']/@content").extract()
        dates = response.xpath("//div[@class='s_comment_date']/meta[@itemprop='datePublished']/@content").extract()
        # headings = response.xpath("//div[@class='width64 floatleft']/h4[3]").extract()
        authors = response.xpath("//div/dl[@class='s_comment']/h4/span/text()").extract()
        website_name = response.xpath("//div[@class='wpcr3_item_name']/a/text()").extract()
        # authors = [''.join(item.split()) for item in authors]
        print(" Ratings ", len(ratings), ratings)
        print("dates ", len(dates), dates)
        print(" Reviews ", len(reviews), reviews)
        # print(" headings ", len(headings), headings)
        print(" authors ", len(authors), authors)
        print(" website_name ", len(website_name), website_name)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], None, dates[item], authors[item],
                                         category, servicename, reviews[item], None, website_name)
            servicename1.save()


