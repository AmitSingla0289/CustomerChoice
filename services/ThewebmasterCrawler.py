from model.Servicemodel import ServiceRecord


class ThewebmasterCrawler():
    def __init__(self):
        pass

    def crawl(self, response, category, servicename):
        reviews = []
        # https://www.thewebmaster.com/web-hosting/shared/justhost-reviews/
        for node in response.xpath("//div[@class='usrv-Body']/div[@class='wys-Outer']/div[2]"):
            reviews.append(node.xpath('string()').extract())
        ratings =   response.xpath("//div[@class='usrv-Header_ScoreOuter']/div[@itemprop='ratingValue']/text()").extract()
        dates = response.xpath("//div[@class='usrv-Header_Content']/p[@class='usrv-Header_Text']/time[@class='usrv-Header_Time']/text()").extract()
        authors = response.xpath("//div[@class='usrv-Header_Content']/h4[@class='usrv-Header_Title']/text()").extract()
        website_name =  response.xpath("/html/head/meta[15]/@content").extract()
        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], None,dates[item], authors[item], category,
                          servicename, reviews[item],"",website_name);
            servicename1.save()