from services.ServiceController import crawl_services
from product import ProductController
if __name__ == '__main__':
    urls = [];
    urls.append({"ServiceName": "Bluehost",
                 "Category": "Hosting Service",
                 "url": "https://www.whoishostingthis.com/hosting-reviews/bluehost/"})
    urls.append({"ServiceName": "Hostgator",
                 "Category": "Hosting Service",
                 "url": "https://hostingfacts.com/hosting-reviews/hostgator-wordpress-managed/"})
    urls.append({"ServiceName": "GoDaddy.com",
                 "Category": "Hosting Service",
                 "url": "https://hostadvice.com/hosting-company/godaddy-reviews/"})
    urls.append({"ServiceName": "Expressvpn",
                 "Category": "VPN Service",
                 "url": "https://www.bestvpn.com/expressvpn-review/"})
    urls.append({"ServiceName": "NordVPN",
                 "Category": "VPN Service",
                 "url": "https://www.resellerratings.com/store/Nordvpn_com"})
    urls.append({"ServiceName": "Nordvpn",
                 "Category": "VPN Service",
                 "url": "https://www.capterra.com/p/166743/NordVPN/"})
    urls.append({"ServiceName": "Nordvpn",
                 "Category": "VPN Service",
                 "url": "https://bestcompany.com/vpn/company/nordvpn"})
    urls.append({"ServiceName": "Binance",
                 "Category": "Cryptocurrency Excahnges",
                 "url": "https://www.forexbrokerz.com/brokers/binance-review"})

    crawl_services(urls)