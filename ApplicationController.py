from restapis import Login
from services.ServiceController import crawl_services
from product.ProductController import crawlAmazon
if __name__ == '__main__':
<<<<<<< HEAD
    #Login.getUrl()
    urls = [];

    urls.append({"ServiceName": "NordVPN",
                 "Category": "Hosting Service",
                 "url": "http://www.freedatinghelper.com/reviews/ourtime-com/"})
    crawl_services(urls)
=======

    #Login.crawling()
    urls=[]
    urls.append({"ServiceName": "Expressvpn",
                 "Category": "VPN Service",
                 "url": "https://webhostinggeeks.com/providers/hostgator?product=shared"})
    crawl_services(urls)
    #crawlAmazon("https://www.amazon.com/Bluetooth-Headphones-Sweatproof-Earphones-Cancelling/dp/B076V4H8BR/ref=sr_1_25?s=aht&ie=UTF8&qid=1524751368&sr=1-25")

>>>>>>> upstream/master
