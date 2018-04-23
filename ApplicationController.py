from restapis import Login
from services.ServiceController import crawl_services
if __name__ == '__main__':
    #Login.getUrl()
    urls = [];
    urls.append({"ServiceName": "Expressvpn",
                 "Category": "VPN Service",
                 "url": "http://www.totallyonlinedating.com/usa-online-dating-services/senior-dating-sites/seniorpeoplemeet.com-review.html"})



    crawl_services(urls)