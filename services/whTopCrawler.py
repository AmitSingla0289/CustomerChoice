from model.Servicemodel import ServiceRecord

class whTopCrawler():
    def __init__(self):
        pass
    def crawl(self, response,category,servicename):
        reviews = []
        # http://www.whtop.com/review/networksolutions.com
        for node in  response.xpath("//div[@class='review-content']"):
            reviews.append(node.xpath('string()').extract());
        ratings =
        dates = response.xpath("//div[@class='review-header clearer']/div[@class='review-date']/time/text()").extract()
        authors = response.xpath("//div[@class='review-header clearer']/div[@property='author']/span[@property='name']/text()").extract()
        website_name = response.xpath("//html/head/meta[9]/@content").extract()
        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url,ratings[item],"",dates[item],authors[item],category,servicename,reviews[item],"",website_name);
            servicename1.save()