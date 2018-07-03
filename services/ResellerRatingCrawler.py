from model.Servicemodel import ServiceRecord


class ResellerRatingCrawler():

    def __init__(self):
        pass

    def crawl(self, response, category, servicename):
        reviews = []
        print("Reviews from Resellerrating.com")
        # https://www.resellerratings.com/store/Nordvpn_com
        for node in  response.xpath("//div[@class='comment']/p[@class='review-body']/span"):
            reviews.append(node.xpath('string()').extract());
        headings =  response.xpath("//div[@class='comment']/p[@class='review-title']/span/text()").extract()
        dates =  response.xpath("//div[@class='comment']/div[@class='date fr']/span/text()").extract()
        ratings = response.xpath("//div[@class='rating siteStars fl']/span[@class='ratingLabel']/span[@class='bold']/text()").extract()
        authors1 =  response.xpath("//div[@class='avatar']/div[@class='user-column']/a[@class='rr-purple show-for-large']/text()").extract()
        website_name = response.xpath("//html/head/meta[15]/@content").extract()
        authors = []
        for content in authors1:
            authors.append(content.strip())

        # print "reviews ",len(reviews), reviews
        # print "headings ", len(headings), headings
        # print "dates ", len(dates), dates
        # print "ratings ", len(ratings), ratings
        # print "authors ", len(authors), authors
        # print "websites ", len(website_name), website_name
        #TODO authors need to extract : Done
        img_src = None
        for item in range(0, len(reviews)):
            if(len(headings)==0):
                servicename1 = ServiceRecord(response.url, ratings[item],None, dates[item], authors[item],
                                             category,
                                             servicename, reviews[item], None,website_name);
            else:
                servicename1 = ServiceRecord(response.url, ratings[item],headings[item], dates[item], authors[item], category,
                          servicename, reviews[item],None, website_name);
            servicename1.save()
