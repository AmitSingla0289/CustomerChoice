from model.Servicemodel import ServiceRecord
# http://reviewsdatingsites.com/site/elitesingles
# TODO: need to check Dates : Done
class ReviewDatingSitesCrawler():
    def __init__(self):
        pass

    def crawl(self, response, category, servicename):
        reviews = []
        print("Review Datingsites")
        # http://reviewsdatingsites.com/site/elitesingles
        for node in response.xpath("//div[@id='reviews']/div[@class='review']/div[@class='row']/div[@class='col-md-9']/div[@class='review-content']/p"):
            reviews.append(node.xpath('string()').extract())
        ratings =  response.xpath("//div[@class='col-md-9']/h4[@class='m-t-0']/span[@class='stars']/span[@itemprop='ratingValue']/@content").extract()
        authors =   response.xpath("//div[@class='media-body text-center']/div/strong/a[@itemprop='author']/text()").extract()
        website_name = response.xpath("//html/body/div[1]/meta[1]/@content").extract()
        dates1 = response.xpath("//div[@id='overview']/div[@class='review']/div[@class='row']/div[@class='col-md-9']/h4[@class='m-t-0']/strong[@class='text-muted date']/text()").extract()
        dates = []
        for content in dates1:
            dates.append(content.strip())
        # print "reviews ", len(reviews), reviews
        # # print "headings ", len(headings), headings
        # print "dates ", len(dates), dates
        # print "ratings ", len(ratings), ratings
        # print "authors ", len(authors), authors
        # print "websites ", len(website_name), website_name
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], None, None, authors[item], category,
                          servicename, reviews[item],None,website_name);
            servicename1.save()