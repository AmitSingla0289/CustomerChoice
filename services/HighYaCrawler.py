from model.Servicemodel import ServiceRecord

class HighYaCrawler():
    def __init__(self):
        pass
    def crawl(self, response,category,servicename):
        reviews = []
        print("review from HighYa.com")
        # https://www.highya.com/coinbase-reviews
        for node in  response.xpath("//div[@class='left-col col-lg-8 col-lg']/div[@id='reviews']/ul[@class='no-list list-review']/li/span/div[@class='description']"):
            reviews.append(node.xpath('string()').extract());
        ratings = response.xpath("//div[@id='reviews']/ul[@class='no-list list-review']/li/span/span[@class='review']/meta[@itemprop='ratingValue']/@content").extract()
        dates =  response.xpath("//div[@id='reviews']/ul[@class='no-list list-review']/li/span/ul[@class='list-line options']/li[last()-1]/text()").extract()
        headings = response.xpath("//div[@id='reviews']/ul[@class='no-list list-review']/li/span/h3[@class='title']/text()").extract()
        authors = response.xpath("//div[@id='reviews']/ul[@class='no-list list-review']/li/span/ul[@class='list-line options']/li[1]/a/span/text()").extract()
        website_name =  response.xpath("//html/head/meta[7]/@content").extract()
        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url,ratings[item],headings[item],dates[item],authors[item],category,servicename,reviews[item],"",website_name);
            servicename1.save()