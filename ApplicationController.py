from product.amazon.helpers import make_request
from services.siteservices.SiteServiceListController import crawl_services1
if __name__ == '__main__':
    urls=[]
    urls.append({"ServiceName": "Expressvpn",
                 "Category": "VPN Service",
                 "url": "http://www.bestdatingreviews.org/datingsites/?categories=Match-Making&regions=Asian-Dating&Submit=+"})

    crawl_services1(urls)

