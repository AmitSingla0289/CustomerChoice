
from services.siteservices.SiteServiceListController import crawl_services1
if __name__ == '__main__':
    urls=[]
    urls.append({"ServiceName": "Expressvpn",
                 "Category": "VPN Service",
                 "url": "https://hostingfacts.com"})
    crawl_services1(urls)

