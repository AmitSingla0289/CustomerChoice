from model.Servicemodel import ServiceRecord

class webhostinggeeksCrawler():
    def __init__(self):
        pass
    #TODO rating pending need to check pagination pending
    def crawl(self, response,category,servicename):
        reviews = []
        # https://webhostinggeeks.com/providers/hostgator?product=shared
        for node in response.xpath('//div[@class="text_description"]'):
            reviews.append(node.xpath('string()').extract());
        dates =  response.xpath("//div[@class='top_line']/span/text()").extract()
        headings = response.xpath("//div[@class='info_description']/p[@class='title_description ']/a/text()").extract()
        authors = response.xpath("//div[@class='user-text']/p/text()").extract()
        website_name =  response.xpath("/html/head/meta[9]/@content").extract()
        #print("Reviews ", len(reviews), reviews)
        #print("Headings ", len(headings), headings)
        #print("Authors ", len(authors), authors)
        # print("Rating ", len(ratings), ratings)
        #print("Dates ", len(dates), dates)
        # print("Img_src ", len(img_src), img_src)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url,None,headings[item],dates[item],authors[item],category,servicename,reviews[item],"",website_name);
            servicename1.save()