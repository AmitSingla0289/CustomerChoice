from restapis import Login
from services.ServiceController import crawl_services
if __name__ == '__main__':
    #Login.getUrl()
    urls = [];

    urls.append({"ServiceName": "NordVPN",
         "Category": "Hosting Service",
         "url": "https://www.seniordatingexpert.com/reviews/senior-people-meet/"})


    crawl_services(urls)