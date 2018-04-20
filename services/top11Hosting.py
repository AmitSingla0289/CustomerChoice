from model.Servicemodel import ServiceRecord

class top11Hosting():
    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        self.category = category
        self.servicename = servicename
        print("review from top11hosting.com")
        # https://www.highya.com/coinbase-reviews
        for node in response.xpath("//div[@class='wpcr3_item wpcr3_business']/div/blockquote[@class='wpcr3_content']"):
            reviews.append(node.xpath('string()').extract());
        ratings = response.xpath("//div[@class='wpcr3_rating_style1_average']/@style").extract()
        ratings.pop(0)
        ratings.pop(0)
        dates = response.xpath("//div[@class='wpcr3_review_datePublished']/text()").extract()
        # headings = response.xpath("//div[@class='width64 floatleft']/h4[3]").extract()
        authors = response.xpath("//div[@class='wpcr3_review_author']/span[@class='wpcr3_caps']/text()").extract()
        website_name = response.xpath("//div[@class='wpcr3_item_name']/a/text()").extract()
        print(" Ratings ", len(ratings), ratings)
        print("dates ", len(dates), dates)
        print(" Reviews ", len(reviews), reviews)
        # print(" headings ", len(headings), headings)
        print(" authors ", len(authors), authors)
        print(" website_name ", len(website_name), website_name)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], None, dates[item], authors[item],
                                         category, servicename, reviews[item], None, website_name)
            servicename1.save()


