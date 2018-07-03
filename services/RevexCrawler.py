from model.Servicemodel import ServiceRecord
from scrapy import Spider, Request
from lxml import etree

# TODO: Done

class RevexCrawler(Spider):

    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        ratings1 = []
        dates = []
        authors = []
        self.category = category
        self.servicename = servicename
        # https://revex.co/bittrex/
        data =response.xpath(".//ol[@class='commentlist']/li/div[@class='commbox']").extract()

        for content in data:
            content = content.replace('<p>','')
            content = content.replace('</p>', '')
            content = content.replace('<br>', '')
            root = etree.HTML(content)
            if(len(root.xpath("//div[@class='comment-content']/span"))>0):
                reviews.append(root.xpath("//div[@class='comment-content']/span/text()")[0])
            elif(len(root.xpath("//div[@class='comment-content-withreview']/div[@class='user_reviews_view simple_color']/div[@class='user_reviews_view_proscons']/div[@class='comm_text_from_review']/span"))>0):
                reviews.append(root.xpath("//div[@class='comment-content-withreview']/div[@class='user_reviews_view simple_color']/div[@class='user_reviews_view_proscons']/div[@class='comm_text_from_review']/span/text()")[0])
            else:
                reviews.append(root.xpath(
                    "//div[@class='comment-content-withreview']/div[@class='user_reviews_view simple_color']/div[@class='user_reviews_view_proscons']/div[@class='comm_text_from_review']/text()")[
                                   0])
            if(len(root.xpath("//div[@class='comment-content-withreview']/div[@class='user_reviews_view simple_color']/div[@class='user_reviews_view_box']/div[@class='user_reviews_view_score']/div[@class='userstar-rating']/span/strong/text()"))>0):
                ratings1.append(root.xpath("//div[@class='comment-content-withreview']/div[@class='user_reviews_view simple_color']/div[@class='user_reviews_view_box']/div[@class='user_reviews_view_score']/div[@class='userstar-rating']/span/strong/text()")[0])
            else:
                ratings1.append("")
            if(len(root.xpath("//div[@class='comment-author vcard clearfix']/div[@class='comm_meta_wrap']/span[@class='time']"))>0):
                dates.append(root.xpath("//div[@class='comment-author vcard clearfix']/div[@class='comm_meta_wrap']/span[@class='time']/text()")[0])
            else:
                dates.append("")
            if(len(root.xpath("//div[@class='comment-author vcard clearfix']/div[@class='comm_meta_wrap']/span[@class='fn']/a"))>0):
                authors.append(root.xpath("//div[@class='comment-author vcard clearfix']/div[@class='comm_meta_wrap']/span[@class='fn']/a/text()")[0])
            else:
                authors.append("")
        website_name = response.xpath("//div[@class='logo_section_wrap']/div[@class='logo-section header_first_style clearfix']/div[@class='logo']/a/@href").extract()[0].split("//")[1]
        print("Reviews ", len(reviews), reviews)
        print("Authors ", len(authors), authors)
        print("Rating ", len(ratings1), ratings1)
        print("Dates ", len(dates), dates)
        # print("img_src ", len(img_src), img_src)
        print("websites ", len(website_name), website_name)
        for item in range(0, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings1[item], None, dates[item], authors[item], category,
                                         servicename, reviews[item], None, website_name)
            servicename1.save()





