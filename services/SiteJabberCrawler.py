from model.Servicemodel import ServiceRecord


class SiteJabberCrawler():

    def __init__(self):
        pass


    def crawl(self, response, category, servicename):
        reviews = []
        print("Reviews from sitejabber.com")
        # https://www.sitejabber.com/reviews/zoosk.com
        for node in response.xpath('//div[@class="review "]/p'):
            reviews.append(node.xpath('string()').extract());
        ratings = response.xpath("//div[@class='star_rating']/@title").extract()
        dates = response.xpath("//div[@class='time tiny_text faded_text']/text()").extract()
        headings = response.xpath("//div[@class='review_title']/a/text()").extract()
        authors = response.xpath("//div[@class='author_name']/a/text()").extract()
        website_name = response.xpath("//div[@id='header_top']/a[@id='header_logo']/picture/img/@alt").extract()
        for item in range(1, len(reviews)):
            servicename1 =ServiceRecord(response.url, ratings[item],headings[item], dates[item], authors[item], category,
                          servicename, reviews[item], None,website_name);
            servicename1.save()
