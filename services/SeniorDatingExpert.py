from model.Servicemodel import ServiceRecord
from utils.utils import getStarts
# https://www.seniordatingexpert.com/reviews/senior-people-meet/
#TODO Done
class SeniorDatingExpert():
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        self.category = category
        self.servicename = servicename
        print("review from seniordatingexpert.com")
        # https://www.seniordatingexpert.com/reviews/silversingles-review/

        for node in response.xpath("//div[@id='main-inner']/ul[@id='user-reviews']/li/div[@class='userrev']/div[@class='user-review']"):
            reviews.append(node.xpath('string()').extract());


        ratings = response.xpath("//div[@id='main-inner']/ul[@id='user-reviews']/li/div[@class='userrev']/div[@class='user-stars']/img/@src").extract()
        authors1 = response.xpath("//div[@id='main-inner']/ul[@id='user-reviews']/li/div[@class='userrev']/div[@class='user-name']/text()").extract()
        # authors = response.xpath("//div/table[@class='showcomment']/tbody/tr[1]/td[@class='commentid']/i/text()").extract()
        # img_src =  response.xpath("//div[@class='item-header-img']/span[@class='item-header-img-container']/img/@src").extract()
        website_name =  response.xpath("//div/header[@id='menu-right']/div[@class='wrapper']/a[@id='logo']/@href").extract()
        # dates = response.xpath("//div[@class='review-content']/div[@class='rating-md']/p/meta/@content").extract()
        # print("dates ", len(dates), dates)
        i = 0;
        ratings1=[];
        authors = [];
        while i < len(ratings):
            ratings1.append(getStarts(ratings[i]))
            i = i+1
        ratings1 = map(lambda foo: foo.replace('.', ''), ratings1)
        j=0
        while j< len(authors1):
            c= authors1[j].split(" By ")
            authors.append(c[1])
            j= j+1
        # print(" Reviews ", len(reviews), reviews)
        # print(" rating ", len(ratings1), ratings1)
        # print(" authors ", len(authors), authors)
        # print(" website_name ", len(website_name), website_name)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings1[item], None, None, authors[item], category,
                          servicename, reviews[item],None,website_name);
            servicename1.save()

        next_page = response.xpath("//div[@class='pagination-container']/ul[@class='pagination']/li[7]/a/@href").extract()
        if next_page is not None:
            next_page_url = "".join(next_page)
            if next_page_url and next_page_url.strip():
                print(type(next_page_url))
                print(next_page_url)
                # yield Request(url=next_page_url, callback=self.parse, dont_filter=True)
                yield response.follow(next_page_url, callback=self.parsing)