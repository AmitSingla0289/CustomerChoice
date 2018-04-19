from model.Servicemodel import ServiceRecord

class yelpCrawler():
    def __init__(self):
        pass
    def crawl(self, response,category,servicename):
        reviews = []
        # https://www.yelp.com/biz/fatcow-burlington
        for node in response.xpath('//div[@class="review-content"]'):
            reviews.append(node.xpath('string()').extract());
        ratings =  response.xpath("//div[@class='biz-rating biz-rating-large clearfix']/div/div/@title").extract()
        dates =  response.xpath("//div[@class='biz-rating biz-rating-large clearfix']/span[@class='rating-qualifier']/text()").extract()
        authors =  response.xpath("//div[@class='media-story']/ul[@class='user-passport-info']/li[@class='user-name']/a[@id='dropdown_user-name']/text()").extract()
        website_name =  response.xpath("//html/head/meta[6]/@content").extract()
        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url,ratings[item],None,dates[item],authors[item],category,servicename,reviews[item],"",website_name);
            servicename1.save()