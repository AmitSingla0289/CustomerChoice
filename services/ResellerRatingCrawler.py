from model.Servicemodel import ServiceRecord


class ResellerRatingCrawler():

    def __init__(self):
        pass


    def crawl(self, response, category, servicename):
        reviews = []
        print("Reviews from Resellerrating.com")
        # https://www.resellerratings.com/store/Nordvpn_com
        for node in response.xpath('//p[@class="review-body"]'):
            reviews.append(node.xpath('string()').extract());
        dates = response.xpath("//div[@class='comment']/div[2]/div[@class='date fr']/span/text()").extract()
        ratings = response.xpath("//div[@class='rating fl']/meta[@itemprop='ratingValue']/@content").extract()
        authors = response.xpath(
            "//div[@class='review'][1]/div[@class='row']/div[@class='three mobile-one columns']/div[@class='avatar']/div[@class='user']/meta/@content").extract()

        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item],None, dates[item], authors[item], category,
                          servicename, reviews[item], None);
            servicename1.save()
