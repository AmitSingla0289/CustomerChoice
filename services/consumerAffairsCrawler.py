from model.Servicemodel import ServiceRecord

class consumerAffairsCrawler():
    def __init__(self):
        pass
    def crawl(self, response,category,servicename):
        reviews = []
        dates = []
        print("review from Consumeraffairs.com")
        # https://www.consumeraffairs.com/internet/godaddy.html
        for node in response.xpath("//div[@class='campaign-reviews__regular-container js-campaign-reviews__regular-container']/div/div[@class='rvw-bd ca-txt-bd-2']/p"):
            reviews.append(node.xpath('string()').extract());
        ratings = response.xpath("//div[1]/div/div/meta[@itemprop='ratingValue']/@content").extract()
        temp_dates = response.xpath("//div[@class='rvw-bd ca-txt-bd-2']/span[@class='ca-txt-cpt ca-txt--clr-gray']/text()").extract()
        for date in temp_dates:
            dates.append(date.split(":")[1])
        authors =  response.xpath("//div[@class='rvw-aut']/div[@class='rvw-aut__inf']/strong[@class='rvw-aut__inf-nm']/text()").extract()
        website_name = response.xpath("//html/head/meta[3]/@content").extract()
        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url,ratings[item],None,dates[item],authors[item],category,servicename,reviews[item],"",website_name);
            servicename1.save()