from restapis import Login
from services.ServiceController import crawl_services
if __name__ == '__main__':
    #Login.getUrl()
    urls = [];

    urls.append({"ServiceName": "NordVPN",
                 "Category": "Hosting Service",
                 "url": "https://www.resellerratings.com/store/Nordvpn_com"})
    '''urls.append({"ServiceName": "NordVPN",
                 "Category": "VPN Service",
                "Category":"Hosting Service",
                "url": "https://www.whoishostingthis.com/hosting-reviews/bluehost/"})
    urls.append({"ServiceName":"zoosk.compy",
                "Category":"Dating site",
                "url": "https://www.sitejabber.com/reviews/zoosk.com"})
    urls.append({"ServiceName": "Hostgator",
                 "Category": "Hosting Service",
                 "url": "https://hostingfacts.com/hosting-reviews/hostgator-wordpress-managed/"})
    urls.append({"ServiceName": "GoDaddy.com",
                 "Category": "Hosting Service",
                 "url": "https://hostadvice.com/hosting-company/godaddy-reviews/"})

    urls.append({"ServiceName": "Expressvpn",
                 "Category": "VPN Service",
                 "url": "http://www.totallyonlinedating.com/usa-online-dating-services/senior-dating-sites/seniorpeoplemeet.com-review.html"})
'''
    crawl_services(urls)