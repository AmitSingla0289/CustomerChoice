from model.Servicemodel import ServiceRecord


class WhoIsHostingCrawler():
    def __init__(self):
        pass

    def crawl(self, response, category, servicename):
        reviews = []
        print("whoishostingthis.com")
        # https://www.whoishostingthis.com/hosting-reviews/bluehost/
        for node in response.xpath('//div[@class="comment pure-u-1 wcc"]'):
            reviews.append(node.xpath('string()').extract());
        ratings = response.xpath("//div[@class='user-info pure-u-1']/img[@class='stars overall']/@alt").extract()
        dates = response.xpath("//div[@class='user-info pure-u-1']/time[@class='published']/text()").extract()
        authors = response.xpath("//div[@class='author']/span[@class='name']/text()").extract()
        img_src = response.xpath("//div[@class='host-info wcc']/a[1]/img[@class=' logo']/@src").extract()
        for item in range(1, len(reviews)):

            servicename1 = ServiceRecord(response.url, ratings[item], None, None, authors[item], category,
                          servicename, reviews[item],img_src,"");
            servicename1.save()