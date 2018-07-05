
from services.siteservices.SiteServiceListController import crawl_services1
if __name__ == '__main__':
    urls=[]
    urls.append({"ServiceName": "Expressvpn",
                 "Category": "VPN Service",
                 "url": "http://www.bestdatingreviews.org/datingsites/"})
    crawl_services1(urls)

