from model.Servicemodel import ServiceRecord


class ThewebmasterCrawler():
    def __init__(self):
        pass

<<<<<<< HEAD
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        self.category = category
        self.servicename = servicename
=======
    def crawl(self, response, category, servicename):
        reviews = []
>>>>>>> upstream/master
        # https://www.thewebmaster.com/web-hosting/shared/justhost-reviews/
        for node in response.xpath("//div[@class='usrv-Body']/div[@class='wys-Outer']/div[2]"):
            reviews.append(node.xpath('string()').extract())
        ratings =   response.xpath("//div[@class='usrv-Header_ScoreOuter']/div[@itemprop='ratingValue']/text()").extract()
        dates = response.xpath("//div[@class='usrv-Header_Content']/p[@class='usrv-Header_Text']/time[@class='usrv-Header_Time']/text()").extract()
        authors = response.xpath("//div[@class='usrv-Header_Content']/h4[@class='usrv-Header_Title']/text()").extract()
        website_name =  response.xpath("/html/head/meta[15]/@content").extract()
<<<<<<< HEAD
        print(" Ratings ", len(ratings), ratings)
        print("dates ", len(dates), dates)
        print(" Reviews ", len(reviews), reviews)
        # print(" headings ", len(headings), headings)
        print(" authors ", len(authors), authors)
        print(" website_name ", len(website_name), website_name)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], None,dates[item], authors[item], category,
                          servicename, reviews[item],None,website_name);
            servicename1.save()
        next_page = response.xpath(
               "//div[ @class ='pgn-Inner'] / a[@ class ='pgn-Next pgn-Prev-disabled']/@href").extract()
        if next_page is not None and "#" not in next_page:
            next_page_url = "".join(next_page)
            if next_page_url and next_page_url.strip():
                print(type(next_page_url))
                print(next_page_url, "    url")
                yield response.follow(url=next_page_url, callback=self.parsing)

=======
        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], None,dates[item], authors[item], category,
                          servicename, reviews[item],"",website_name);
            servicename1.save()
>>>>>>> upstream/master
