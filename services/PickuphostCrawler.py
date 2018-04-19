from model.Servicemodel import ServiceRecord


class PickuphostCrawler():
    def __init__(self):
        pass

    def crawl(self, response, category, servicename):
        reviews = []
        # http://pickuphost.com/review/bluehost/
        for node in :
            reviews.append(node.xpath('string()').extract());
        ratings =
        headings =  response.xpath("//div[@class='one_rew']/h4/b/text()").extract()
        dates =
        authors =
        img_src =
        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], headings[item], None, authors[item], category,
                          servicename, reviews[item],img_src,"");
            servicename1.save()