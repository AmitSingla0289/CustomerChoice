from model.Servicemodel import ServiceRecord
from scrapy import Spider, Request
from lxml import etree

# TODO : DONE
class ReviewOpedia(Spider):

    def __init__(self):
        pass
    def parsing(self, response):
        return self.crawl(response,self.category,self.servicename)

    def crawl(self, response, category, servicename):
        reviews = []
        self.category = category
        self.servicename = servicename

        for node in response.xpath("//div[@id='review-results']/div[@class='item-info review']/div[@class='review-text']/p"):
            reviews.append(node.xpath('string()').extract());
        ratings =  response.xpath("//div[@id='review-results']/div[@class='item-info review']/div[@class='item-info-text user']/div[@class='prod-block-line']/div[@class='review-result-rating']/div[@class='average_rating average_rating_10']/meta/@content").extract()
        dates = response.xpath("//div[@id='review-results']/div[@class='item-info review']/div[@class='item-info-text user']/div[@class='prod-block-line']/div[@class='review-date']/text()").extract()
        headings =  response.xpath("//div[@id='review-results']/div[@class='item-info review']/div[@class='item-info-text user']/h4[@class='item-title']/text()").extract()
        authors =  response.xpath("//div[@class='item-info review']/div[@class='review-result-left']/div[@class='review-result-author']/div[@class='reviewed-by']/a/text()").extract()
        website_name =  "reviewopedia.com"
        # img_src = response.xpath("//div[@class='review_result']/div[@class='review_result_left']/img[@class='review_author_img']/@src").extract()
        # print("Reviews ", len(reviews), reviews)
        # print("Headings ", len(headings), headings)
        # print("Authors ", len(authors), authors)
        # print("Rating ", len(ratings), ratings)
        # print("Dates ", len(dates), dates)
        # print("Img_src ", len(img_src), img_src)
        for item in range(0, len(reviews)):
            servicename1 =ServiceRecord(response.url, ratings[item],headings[item], dates[item], authors[item], category,
                          servicename, reviews[item], None,website_name)
            servicename1.save()

        # next_page = response.xpath("//div[@class='container']/div[@class='navigator']/a[last()]/@href").extract()
        # if next_page is not None:
        #     next_page_url = "".join(next_page[0])
        #     print(next_page_url)
        #     if next_page_url and next_page_url.strip():
        #         yield Request(url=next_page_url,  callback=self.parsing)
