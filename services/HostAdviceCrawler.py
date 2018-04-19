from model.Servicemodel import ServiceRecord


class HostAdviceCrawler():
    def __init__(self):
        pass

    def crawl(self, response, category, servicename):
        reviews = []
        print("Hostadvice.com")
        # https://hostadvice.com/hosting-company/godaddy-reviews/
        for node in response.xpath("//div[@id='reviews']/ul[@class='no-list list-review']/li/span/div[@class='description']"):
            reviews.append(node.xpath('string()').extract());
        ratings = response.xpath("//div[@class='review-rating clearfix']/span[@class='review-score']/text()").extract()
        headings = response.xpath("//div[@class='review-content']/h3[@class='review_header']/text()").extract()
        authors = response.xpath("//div[@class='review-author']/strong/text()").extract()
        img_src = response.xpath("//div[@class='col-md-offset-1 col-md-5 col-xs-6']/img[ @class='attachment-post-thumbnail size-post-thumbnail wp-post-image']/@src").extract()
        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], headings[item], None, authors[item], category,
                          servicename, reviews[item],img_src,"");
            servicename1.save()