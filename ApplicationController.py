from services.ServiceController import crawl_services
from product import ProductController
if __name__ == '__main__':
    urls = [];
    urls.append({"ServiceName":"Bluehost",
                "Category":"Hosting Service",
                "url": "https://www.whoishostingthis.com/hosting-reviews/bluehost/"})

    urls.append({"ServiceName":"zoosk.compy",
                "Category":"Dating site",
                "url": "https://www.sitejabber.com/reviews/zoosk.com"})
    crawl_services(urls)