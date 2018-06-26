from product.amazon import AmazonController, Amazon
from utils import GetProxyList
urllist = []
def crawlAmazon(urls):
    global  urllist
    urllist = urls
    GetProxyList.getProxy();
    onProxyUpdated()
def onProxyUpdated():
    for url in urllist:
        Amazon.ParseReviews(url)

if __name__ == '__main__':
    crawlAmazon(["https://www.amazon.com/BMW-2-Door-Convertible-Titanium-Metallic/dp/B011AYQSKA/ref=sr_1_19?s=vehicles&ie=UTF8&qid=1529960662&sr=1-19&refinements=p_4%3ABMW"])
