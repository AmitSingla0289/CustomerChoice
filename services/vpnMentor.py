from model.Servicemodel import ServiceRecord
from lxml import etree

class vpnMentor():
    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)
 #TODO Need to recheck and implement: done some error Done
    def crawl(self, response, category, servicename):
        reviews = []
        self.category = category
        self.servicename = servicename
        #print("review from vpnmentor.com")
        # https://www.vpnmentor.com/reviews/expressvpn/
        authors = []
        dates = []
        ratings = []
        reviews = []
        headings = []
        data = response.xpath("//div[@id='user-review']/span/div[@class='block-content']/div/div[@class='review-item style_prevu_kit ']").extract()
        for content in data:
            content = content.replace('<br>', '$')
            root = etree.HTML(content)
            if(len(root.xpath("//div/div/div/div/div/h5/text()"))>0):
                authors.append(root.xpath("//div/div/div/div/div/h5/text()")[0])
            else:
                authors.append("")
            if(len(root.xpath("//div[@class='review-head']/div[@class='row']/div[@class='col-md-4 col-xs-5']/div[@class='user']/div[@class='text-wrap']/h6/text()")) == 0):
                dates.append("")
            else:
                dates.append(str(root.xpath("//div[@class='review-head']/div[@class='row']/div[@class='col-md-4 col-xs-5']/div[@class='user']/div[@class='text-wrap']/h6/text()")[0]))
            headings.append(root.xpath("//div[@class='review-head']/div[@class='row']/div[@class='col-md-6 col-md-pull-2 col-xs-12']/div[@class='topic']/span/text()")[0])
            ratings.append(str(root.xpath("//div[@class='review-head']/div[@class='row']/div[@class='col-md-2 col-md-push-6 col-xs-7']/div[@class='rate']/ul/li[@class='fa']/text()")))
            reviews.append(root.xpath("///div[@class='review-content']/p/text()"))
        website_name = response.xpath("//div[@class='container']/div[@class='row']/div[@id='top1079leftFix']/a/@href").extract()[0]


        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], headings[item], dates[item], authors[item],
                                         category, servicename, reviews[item], None, website_name)
            servicename1.save()


