from restapis import Login
from services.ServiceController import crawl_services
if __name__ == '__main__':
    #Login.getUrl()
    urls = [];

    urls.append({"ServiceName": "NordVPN",
                 "Category": "Hosting Service",
                 "url": "http://www.freedatinghelper.com/reviews/ourtime-com/"})
    crawl_services(urls)