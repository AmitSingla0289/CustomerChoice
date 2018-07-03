from model.Servicemodel import ServiceRecord
from services.siteservices.BaseSiteURLCrawler import BaseSiteURLCrawler

class HostingFactsCrawler(BaseSiteURLCrawler):

    def __init__(self,category,servicename,url):

        self.category = category
        self.servicename = servicename
        self.link = {"ServiceName": servicename,
                "Category": category,
                "url": url}
        super(HostingFactsCrawler,self).__init__()
        self.createCategory(self.link)
        pass
    def parsing(self, response):
        return self.crawl(response)

    def crawl(self, response):
        reviews = []
        print("review from Hostingfacts.com                    ", self.link["url"])
        # https://hostingfacts.com/hosting-reviews/hostgator-wordpress-managed/
        print "reviews ", len(reviews)
        for node in response.xpath('//div[@class="user-review-content/p"]'):
            reviews.append(node.xpath('string()').extract());
        ratings = response.xpath("//div[@class= 'user-review']/header/section/span[@class='user-review-rating']/span[@class='value']/text()").extract()
        dates = response.xpath("//div[@class= 'user-review']/header/section/span[@class='user-review-meta']/text()").extract()
        headings = response.xpath("//div[@class= 'user-review']/section/p[@class='user-review-title']/text()").extract()
        authors = response.xpath("//div[@class='user-review']/header/section/p[@class='user-review-name']/a/span/text()").extract()
        img_src = response.xpath("//div[@class='sidebar-padder']/aside/img[@class='img-responsive banner-image center-block']/@src").extract()
        website_name = response.xpath("//div[@class='navbar-header']/a[@class='navbar-brand']/text()").extract()

        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url,ratings[item],headings[item],dates[item],authors[item],"category",self.servicename,reviews[item],img_src,website_name);
            servicename1.save()
        # self.pushToServer()