from services.ServiceController import crawl_services
from product import ProductController
if __name__ == '__main__':
    category = {"ServiceName":"category",
                "Category":"subcategory"}
    crawl_services("https://www.whoishostingthis.com/hosting-reviews/bluehost/",category)