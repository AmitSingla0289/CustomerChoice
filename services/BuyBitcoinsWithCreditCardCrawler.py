from model.Servicemodel import ServiceRecord
from lxml import etree

class BuyBitcoinsWithCreditCardCrawler():
    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        self.category = category
        self.servicename = servicename
        # http://www.buybitcoinswithcreditcard.net/en/coinbase-com/
        '''temp_dates =  response.xpath("//div[@class='box']/ol[@class='comment-list']/li/div/div[@class='comment-author vcard rc']/text()").extract()
        dates = []
        for j in range(1, len(dates)):
            if (j % 2 != 0):
                dates.append(dates[j])
        authors = response.xpath("//div[@class='box']/ol[@class='comment-list']/li/div/div[@class='comment-author vcard rc']/cite[@class='fn']/text()").extract()'''
        text = response.xpath("//div[@id='reviews']/div[@class='box']/ol[@class='comment-list']/li").extract()
        for content in text:
            root = etree.fromstring(content)
            print(root)
            for element in root:
                print(element.text)

        '''for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], headings[item], dates[item], authors[item],
                                         category, servicename, reviews[item], None, website_name)
            servicename1.save()'''

