from model.Servicemodel import ServiceRecord
from lxml import etree
class FreeDatingHelperCrawler():
    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        self.category = category
        self.servicename = servicename
        # http://www.freedatinghelper.com/reviews/fortyplus-singles/
        #TODO Need to check pick only first review: Refer Sandy : Done
        authors = []

        ratings =[]
        for node in response.xpath("//div[@class='comment_area']/div[@class='comment-content clearfix']/div/span/p"):
            reviews.append(node.xpath('string()').extract());
        rat = response.xpath("//li/article/div[@class='comment_postinfo']/div[@itemscope]").extract()
        authors = response.xpath("//div[@class='comment_postinfo']/div[2]/span[@class='fn']/span/text()").extract()
        for content in rat:
            # print(content)
            root = etree.HTML(content)
            if(len(root.xpath("//table/tr/td/img/@alt"))>0):
                ratings.append(root.xpath("//table/tr/td/img/@alt")[0])
            else:
                ratings.append("")


        website_name= response.xpath("//html/head/meta[8]/@content").extract()[0]
        # print("Reviews ", len(reviews), reviews)
        # print("Authors ", len(authors), authors)
        # print("Rating ", len(ratings), ratings)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], None, None, authors[item],
                                         category, servicename, reviews[item], None, website_name)
            servicename1.save()