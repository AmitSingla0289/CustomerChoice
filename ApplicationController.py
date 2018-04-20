from restapis import Login
from services.ServiceController import crawl_services
if __name__ == '__main__':
    # Login.getUrl()
    webiste = []

    webiste.append({"ServiceName": "Bluehost",
                    "Category": "Hosting Service",
                    # "url": "http://www.affpaying.com/hotspot-shield-affiliate-program"})
                    "url": "https://www.vpnranks.com/nordvpn-review/"})
    crawl_services(webiste)
