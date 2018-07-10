# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue

import scrapy
from scrapy import Request
from scrapy.crawler import  CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from services.siteservices.SiteJabberURLCrawler import SiteJabberURLCrawler
from services.siteservices.HostingFactsURLCrawler import HostingFactsURLCrawler
from services.siteservices.HighyaURLCrawler import HighyaURLCrawler
from services.siteservices.AlterNativeToURLCrawler import AlterNativeToURLCrawler
from services.siteservices.SeniorDatingExpertURLCrawler import SeniorDatingExpertURLCrawler
from services.siteservices.TravelSiteCriticURLCrawler import TravelSiteCriticURLCrawler
from services.siteservices.NetBusinessRatingURLCrawler import NetBusinessRatingURLCrawler
from services.siteservices.ReviewCentreURLCrawler import ReviewCentreURLCrawler
from services.siteservices.ViewpointsURLCrawler import ViewPointsURLCrawler
from services.siteservices.CapterraURLCrawler import CapterraURLCrawler
from services.siteservices.BuyBitcoinWithCreditCardURLCrawler import BuyBitcoinWithCreditCardURLCrawler
from services.siteservices.AnblikURLCrawler import AnblikCrawlerURLCrawler
from services.siteservices.CoinJabberURLCrawler import CoinJabberURLCrawler
from services.siteservices.FreeDatingHelperURLCrawler import FreeDatingHelperURLCrawler
from services.siteservices.bestdatingreviews import BestDatingReviewsCrawlerFactory
from services.siteservices.InfluensterURLCrawler import InfluensterURLCrawler
from services.siteservices.RevexURLCrawler import RevexURLCrawler
from services.siteservices.ReviewOpediaURLCrawler import ReviewOpediaURLCrawler
from services.siteservices.AffgadgetsURLCrawler import AffgadgetsURLCrawler
from services.siteservices.AffpayingURLCrawler import AffPayingURLCrawler
from services.siteservices.BestVPNURLCrawler import BestVPNURLCrawler
from services.siteservices.BestVpnForYouURLCrawler import BestVpnForYouURLCrawler
from services.siteservices.ProductReviewURLCrawler import ProductreviewURLCrawler
from services.siteservices.ResellerRatingsURLCrawler import ResellerRatingsURLCrawler
from services.siteservices.RestorePrivacyURLCrawler import RestorePrivacyURLCrawler
from services.siteservices.TheWebMasterURLCrawler import ThewebmasterURLCrawler
from services.siteservices.WhtopURLCrawler import WhtopURLCrawler
from services.siteservices.YelpURLCrawler import YelpURLCrawler
from services.siteservices.YscamURLCrawler import YscamURLCrawler
from services.siteservices.DatingSitesReviewsURLCrawler import DatingSitesReviewsURLCrawler
from services.siteservices.TopSiteGratisURLCrawler import TopSiteGratisURLCrawler
from services.siteservices.VpnPickURLCrawler import VpnPickURLCrawler
from services.siteservices.PickUpHostURLCrawler import PickuphostURLCrawler
from services.siteservices.BestBitcoinExchnageURLCrawler import BestBitcoinExchangeURLCrawler
from services.siteservices.TrustPilotURLCrawler import TrustPilotURLCrawler
from services.siteservices.VirtualBankingURLCrawler import VirtualBankingURLCrawler

from services.SiteJabberCrawler import SiteJabberCrawler
from services.HostingFactsCrawler import HostingFactsCrawler
from services.HighYaCrawler import HighYaCrawler
from services.AlterNativeTo import AlterNativeTo
from services.SeniorDatingExpert import SeniorDatingExpert
from services.TravelSiteCritic import TravelSiteCritic
from services.NetBusinessRating import NetBusinessRating
from services.ReviewCentre import ReviewCentre
from services.ViewPoints import ViewPoints
from services.CapterraCrawler import CapterraCrawler
from services.BuyBitcoinsWithCreditCardCrawler import BuyBitcoinsWithCreditCardCrawler
from services.AnblikCrawler import AnblikCrawler
from services.CoinJabber import CoinJabber
from services.hostAdvisor import hostAdvisor
from services.FreeDatingHelperCrawler import FreeDatingHelperCrawler
from services.InfluensterCrawler import InfluensterCrawler
from services.RevexCrawler import RevexCrawler
from services.ReviewOpedia import ReviewOpedia
from services.affgadgetsCrawler import affgadgetsCrawler
from services.affPaying import affPaying
from services.BestVPN import BestVPN
from services.HostAdviceCrawler import HostAdviceCrawler
from services.bestVPNForYou import bestVPNForYou
from services.ProductreviewCrawler import ProductreviewCrawler
from services.ResellerRatingCrawler import ResellerRatingCrawler
from services.restorePrivacy import restorePrivacy
from services.ThewebmasterCrawler import ThewebmasterCrawler
from services.vpnMentor import vpnMentor
from services.webhostinggeeksCrawler import webhostinggeeksCrawler
from services.WhoIsHostingCrawler import WhoIsHostingCrawler
from services.whtop import whtop
from services.yelpCrawler import yelpCrawler
from services.Yscam import Yscam
from services.hostingCharges import hostingCharges
from services.DatingSitesReviewsCrawler import DatingSitesReviewsCrawler
from services.TopSiteGratis import TopSiteGratis
from services.DatingWiseCrawler import DatingWiseCrawler
from services.VPNpickCrawler import VPNpickCrawler
from services.PickuphostCrawler import PickuphostCrawler
from services.BestBitcoinExchange import BestBitcoinExchange
from services.TrustPilot import TrustPilot
from services.VirtualBanking import VirtualBanking

final_dict_urls= {}
dict_url = {}
class SiteServiceListController(scrapy.Spider):
    start_urls = []

    def __init__(self, link):
        if (len(self.start_urls) > 0):
            self.start_urls.pop(0)
        self.start_urls.append(link["url"])
        category = link["Category"];
        dict_url[link["url"]] = {"Category": category}

    def closed(self, reason):
        pass

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers,meta={'dont_merge_cookies': True})

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        if ('sitejabber.com' in response.url):
            if('reviews' in response.url):
                service  = response.url.split("/");
                serviceName = service[len(service)-1];
                print(" Servicesssss   ", serviceName)
                crawler = SiteJabberCrawler( dict_url[response.url]["Category"],serviceName,response.url)
            else:
                crawler = SiteJabberURLCrawler(dict_url[response.url]["Category"])
        elif('hostingfacts.com' in response.url):
            if ('reviews' in response.url):
                service = response.url.split("/");
                serviceName = service[len(service) - 1];
                print(" Servicesssss   ", serviceName)
                crawler = HostingFactsCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = HostingFactsURLCrawler(dict_url[response.url]["Category"])
        elif ('highya.com' in response.url):
            if ('reviews' in response.url):
                service = response.url.split("/");
                serviceName = service[len(service) - 1];
                print(" Servicesssss   ", serviceName)
                crawler = HighYaCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = HighyaURLCrawler(dict_url[response.url]["Category"])
        elif ('alternativeto.net' in response.url):
            if ('browse' in response.url):
                crawler = AlterNativeToURLCrawler(dict_url[response.url]["Category"])
            else:
                service = response.url.split("/");
                serviceName = service[len(service) - 1];
                print(" Servicesssss   ", serviceName)
                crawler = AlterNativeTo(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('seniordatingexpert.com' in response.url):
            if len(response.url.split('/')) > 5:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = SeniorDatingExpert(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = SeniorDatingExpertURLCrawler(dict_url[response.url]["Category"])
        elif ('travelsitecritic.com' in response.url):
            if len(response.url.split('/')) > 5:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = TravelSiteCritic(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = TravelSiteCriticURLCrawler(dict_url[response.url]["Category"])
        elif ('netbusinessrating.com' in response.url):
            if ('search' in response.url):
                crawler = NetBusinessRatingURLCrawler(dict_url[response.url]["Category"])
            else:
                service = response.url.split("/");
                serviceName = service[len(service) - 1];
                print(" Servicesssss   ", serviceName)
                crawler = NetBusinessRating(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('reviewcentre.com' in response.url):
            if('searchstring' not in response.url):
                service  = response.url.split("/");
                serviceName = service[len(service)-1];
                print(" Servicesssss   ", serviceName)
                crawler = ReviewCentre( dict_url[response.url]["Category"],serviceName,response.url)
            else:
                crawler = ReviewCentreURLCrawler(dict_url[response.url]["Category"])
        elif ('viewpoints.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = ViewPoints(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = ViewPointsURLCrawler(dict_url[response.url]["Category"])
        elif ('capterra.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = CapterraCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = CapterraURLCrawler(dict_url[response.url]["Category"])
        elif ('buybitcoinswithcreditcard.net' in response.url):
            if '?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = BuyBitcoinsWithCreditCardCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = BuyBitcoinWithCreditCardURLCrawler(dict_url[response.url]["Category"])
        elif ('anblik.com' in response.url):
            if '?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = AnblikCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = AnblikCrawlerURLCrawler(dict_url[response.url]["Category"])
        elif ('coinjabber.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = CoinJabber(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = CoinJabberURLCrawler(dict_url[response.url]["Category"])
        elif ('hostadvisor.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = hostAdvisor(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('freedatinghelper.com' in response.url):
            if '?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = FreeDatingHelperCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = FreeDatingHelperURLCrawler(dict_url[response.url]["Category"])
        elif ('bestdatingreviews.org' in response.url):
            crawler = BestDatingReviewsCrawlerFactory.getCrawler(response.url,dict_url[response.url]["Category"])
        elif ('influenster.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = InfluensterCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = InfluensterURLCrawler(dict_url[response.url]["Category"])
        elif ('revex.co' in response.url):
            if '/?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = RevexCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = RevexURLCrawler(dict_url[response.url]["Category"])
        elif ('reviewopedia.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = ReviewOpedia(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = ReviewOpediaURLCrawler(dict_url[response.url]["Category"])
        elif ('affgadgets.com' in response.url):
            if '/?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = affgadgetsCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = AffgadgetsURLCrawler(dict_url[response.url]["Category"])
        elif ('affpaying.com' in response.url):
            if '/?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = affPaying(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = AffPayingURLCrawler(dict_url[response.url]["Category"])
        elif ('bestvpn.com' in response.url):
            if len(response.url.split('/')) > 5:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = BestVPN(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = BestVPNURLCrawler(dict_url[response.url]["Category"])
        elif ('hostadvice.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = HostAdviceCrawler(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('bestvpnforyou.com' in response.url):
            if '/?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = bestVPNForYou(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = BestVpnForYouURLCrawler(dict_url[response.url]["Category"])
        elif ('productreview.com.au' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = ProductreviewCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = ProductreviewURLCrawler(dict_url[response.url]["Category"])
        elif ('resellerratings.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = ResellerRatingCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = ResellerRatingsURLCrawler(dict_url[response.url]["Category"])
        elif ('restoreprivacy.com' in response.url):
            if '/?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = restorePrivacy(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = RestorePrivacyURLCrawler(dict_url[response.url]["Category"])
        elif ('thewebmaster.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = ThewebmasterCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = ThewebmasterURLCrawler(dict_url[response.url]["Category"])
        elif ('vpnmentor.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 2]
                print(" Servicesssss   ", serviceName)
                crawler = vpnMentor(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('webhostinggeeks.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = webhostinggeeksCrawler(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('whoishostingthis.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = WhoIsHostingCrawler(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('whtop.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = whtop(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = WhtopURLCrawler(dict_url[response.url]["Category"])
        elif ('yelp.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = yelpCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = YelpURLCrawler(dict_url[response.url]["Category"])
        elif ('yscam.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = Yscam(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = YscamURLCrawler(dict_url[response.url]["Category"])
        elif ('hostingcharges.in' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = hostingCharges(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('datingsitesreviews.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = DatingSitesReviewsCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = DatingSitesReviewsURLCrawler(dict_url[response.url]["Category"])
        elif ('topsitegratis.com.br' in response.url):
            if '/?q=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = TopSiteGratis(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = TopSiteGratisURLCrawler(dict_url[response.url]["Category"])
        elif ('datingwise.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 2]
                print(" Servicesssss   ", serviceName)
                crawler = DatingWiseCrawler(dict_url[response.url]["Category"], serviceName, response.url)
        elif ('vpnpick.com' in response.url):
            if '/?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 2]
                print(" Servicesssss   ", serviceName)
                crawler = VPNpickCrawler(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = VpnPickURLCrawler(dict_url[response.url]["Category"])
        elif ('bestbitcoinexchange.net' in response.url):
            if '/?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 2]
                print(" Servicesssss   ", serviceName)
                crawler = BestBitcoinExchange(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = BestBitcoinExchangeURLCrawler(dict_url[response.url]["Category"])
        elif ('trustpilot.com' in response.url):
            if 'search' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = TrustPilot(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawtler = TrustPilotURLCrawler(dict_url[response.url]["Category"])
        elif ('virtualbanking.com' in response.url):
            if '/?s=' not in response.url:
                service = response.url.split("/")
                serviceName = service[len(service) - 1]
                print(" Servicesssss   ", serviceName)
                crawler = VirtualBanking(dict_url[response.url]["Category"], serviceName, response.url)
            else:
                crawler = VirtualBankingURLCrawler(dict_url[response.url]["Category"])
        else:
            print("Found Nothing")
        if (crawler != None):
            return crawler.crawl(response)

def f(q, ):
    try:
        configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
        runner = CrawlerRunner()
        deferred = runner.crawl(SiteServiceListController, q[1])
        deferred.addBoth(lambda _: reactor.stop())
        reactor.run()
        q[0].put(None)
    except Exception as e:
        q[0].put(e)

def run_spider(urls):
    q = Queue()
    p = Process(target=f, args=([q, urls],))
    p.start()
    result = q.get()
    p.join()
    if result is not None:
        raise result
def crawl_services1(urls):
    for i in urls:
        run_spider(i)

