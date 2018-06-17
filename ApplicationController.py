
from services.siteservices.SiteServiceListController import crawl_services1
from services.ServiceController import crawl_services
if __name__ == '__main__':
   #Login.crawling()
    urls=[]
    urls.append({"ServiceName": "Expressvpn",
                 "Category": "VPN Service",
                 "url": "https://www.sitejabber.com/search?q=hosting"})
    crawl_services1(urls)

