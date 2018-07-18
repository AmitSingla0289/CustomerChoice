from model.Servicemodel import ServiceRecord
from utils.utils import getStarts
from services.siteservices.BaseSiteURLCrawler import BaseSiteURLCrawler
from lxml import etree
# http://www.bestdatingreviews.org/datingreviews/S2997
class BestDatingReviews(BaseSiteURLCrawler):

    def __init__(self,category,servicename,url):

        self.category = category
        self.servicename = servicename
        self.link = {"ServiceName": servicename,
                "Category": category,
                "url": url}
        super(BestDatingReviews,self).__init__()
        self.createCategory(self.link)
        pass
    def parsing(self, response1):
        return self.crawl(response1)

    def crawl(self, response):
        reviews = []
        headings = []
        ratings = []
        print("review from blackpeoplemeet.pissedconsumer.com")
        data = response.xpath("//dl/dt").extract()
        for content in data:
            root = etree.HTML(content)
            if len(root.xpath("//div[@class='all_sites_list_c']/text()"))>0:
                reviews.append(root.xpath("//div[@class='all_sites_list_c']/text()"))
            if len(root.xpath("//div[@class='all_sites_list_a']/a/text()"))>0:
                headings.append(root.xpath("//div[@class='all_sites_list_a']/a/text()")[0])
            if len (root.xpath("//div[@class='all_sites_list_b']/img"))>0:
                ratings.append(len(root.xpath("//div[@class='all_sites_list_b']/img")))
        dates1 = response.xpath("//dl/dt/div[@class='all_sites_list_a']/span/text()").extract()
        website_name = "bestdatingreviews.org"
        dates1 = list(map(lambda foo: foo.replace(u'\xa0', u''), dates1))
        dates1 = list(map(lambda foo: foo.replace('By', ''), dates1))
        dates1 = list(map(lambda foo: foo.replace(',', ''), dates1))
        dates = []
        authors = []
        i=0
        while i < len(dates1):
            if(i%2==0):
                dates.append(dates1[i])
            else:
                c= dates1[i].split('|')
                authors.append(c[0])
            i = i+1
        print("Authors ", len(authors), authors)
        print("headings ", len(headings), headings)
        print("Rating ", len(ratings), ratings)
        print("Dates ", len(dates), dates)
        print("reviews ", len(reviews), reviews)
        print("websites ", len(website_name), website_name)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], headings[item], dates[item], authors[item],
                                         self.category, self.servicename, reviews[item], None, website_name)
            self.save(servicename1)

        next_page = response.xpath("//div[@class='sites_list_more']/a/@href").extract()
        if next_page is not None:
            next_page_url = "".join(next_page)
            if next_page_url and next_page_url.strip():
                print(type(next_page_url))
                print(next_page_url)
                # yield Request(url=next_page_url, callback=self.parse, dont_filter=True)
                yield response.follow(next_page_url, callback=self.parsing)
        self.pushToServer()





