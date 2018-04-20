from model.Servicemodel import ServiceRecord


class PickuphostCrawler():
    def __init__(self):
        pass

    def crawl(self, response, category, servicename):
        reviews = []
        #http://pickuphost.com/review/bluehost/#customer_review_shap
        for node in response.xpath("//div[@class='one_rew']/div[@class='rewiwer_post']/span"):
            reviews.append(node.xpath('string()').extract());
        ratings =  response.xpath("//div[@class='col-md-12 avg_ratting_bg text-center']/div[@class='avg_ratting text-center']/text()").extract()
        headings = response.xpath("//div[@id='rew_replace_div']/div[@class='one_rew']/h4/b/text()").extract()
        dates = response.xpath("//div[@id='rew_replace_div']/div[@class='one_rew']/span[@class='rewiwer_data']/span[2]/text()").extract()
        authors = response.xpath("//div[@id='rew_replace_div']/div[@class='one_rew']/span[@class='rewiwer_data']/span[1]/text()").extract()
        website_name =
        for item in range(1, len(reviews)):
            servicename1 = ServiceRecord(response.url, ratings[item], headings[item], dates[item], authors[item], category,
                          servicename, reviews[item],"",website_name);
            servicename1.save()