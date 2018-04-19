from model.Servicemodel import ServiceRecord

class webhostinggeeksCrawler():
    def __init__(self):
        pass
    def crawl(self, response,category,servicename):
        reviews = []
        print("review from HighYa.com")
        # https://webhostinggeeks.com/providers/hostgator?product=shared
        for node in response.xpath('//div[@class="text_description"]'):
            reviews.append(node.xpath('string()').extract());
        ratings =
        dates =  response.xpath("//div[@class='top_line']/span/text()").extract()
        headings = response.xpath("//div[@class='info_description']/p[@class='title_description ']/a/text()").extract()
        authors = response.xpath("//div[@class='user-text']/p/text()").extract()
        website_name =  response.xpath("/html/head/meta[9]/@content").extract()
        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url,ratings[item],headings[item],dates[item],authors[item],category,servicename,reviews[item],"",website_name);
            servicename1.save()