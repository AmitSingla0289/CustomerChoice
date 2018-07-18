from product.amazon.helpers import make_request
from services.siteservices.SiteServiceListController import crawl_services1
if __name__ == '__main__':
    urls=[]
    urls.append({"ServiceName": "Expressvpn",
                 "Category": "VPN Service",
                 "url": "https://www.macupdate.com/app/mac/52417/purevpn"})

    crawl_services1(urls)

