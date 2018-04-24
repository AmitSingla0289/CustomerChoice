from model.Servicemodel import ServiceRecord


class HostAdvisorCrawler():
    def __init__(self):
        pass

    def crawl(self, response, category, servicename):
        reviews = []
        # https://hostadvice.com/hosting-company/godaddy-reviews/
        for node in :
            reviews.append(node.xpath('string()').extract());
        ratings =
        headings =  response.xpath("//div[@class='contents']/div[@class='textHolder']/h5/text()").extract()
        dates =
        authors =
        website_name =
        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], headings[item], None, authors[item], category,
                          servicename, reviews[item],img_src,"");
            servicename1.save()