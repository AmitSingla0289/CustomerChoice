# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 21:49:30 2018

@author: madhvi.gupta
"""

import json
import re
from time import sleep

import requests
from dateutil import parser as dateparser
from lxml import html
from requests import RequestException

from product.amazon import settings
from product.amazon.helpers import get_proxy, log
from utils import utils


def ParseReviews(url):
    # for i in range(5):
    #     try:
    # This script has only been tested with Amazon.com
    #Todo: check for subcategory and append it in json
    amazon_url =  url
    print(url)
    # Add some recent user agent to prevent amazon from blocking the request 
    # Find some chrome user agent strings  here https://udger.com/resources/ua-list/browser-detail?browser=Chrome
    proxies = []
    proxies = get_proxy()
    print(proxies)
    try:
        page = requests.get(url, headers=settings.headers, proxies=proxies)
    except RequestException as e:
        log("WARNING: Request for {} failed, trying again.".format(url))
          # try request again, recursively
    page_response = page.text
    parser = html.fromstring(page_response)
    XPATH_AGGREGATE = '//span[@id="acrCustomerReviewText"]'
    XPATH_REVIEW_SECTION_1 = '//div[contains(@id,"reviews-summary")]'
    XPATH_REVIEW_SECTION_2 = '//div[@data-hook="review"]'
    XPATH_AGGREGATE_RATING = '//table[@id="histogramTable"]//tr'
    XPATH_PRODUCT_NAME = '//h1//span[@id="productTitle"]//text()'
    XPATH_PRODUCT_PRICE = '//span[@id="priceblock_ourprice"]/text()'
    XPATH_PRODUCT_AVAILABILITY = '//div[@id="availability"]/span/text()'
    XPATH_PRODUCT_CATEGORY = '//div[@id="wayfinding-breadcrumbs_feature_div"]/ul[@class="a-unordered-list a-horizontal a-size-small"]/li[1]/span[@class="a-list-item"]/a[@class="a-link-normal a-color-tertiary"]/text()'
    XPATH_PRODUCT_LIST_PRICE = '//span[@class="a-text-strike"]/text()'
    XPATH_PRODUCT_BRAND = '//div[@class="a-section a-spacing-none"]/a[@id="bylineInfo"]/text()'

    XPATH_SUB_CATEGORY = '//div[@id="wayfinding-breadcrumbs_feature_div"]/ul[@class="a-unordered-list a-horizontal a-size-small"]/li/span[@class="a-list-item"]/a[@class="a-link-normal a-color-tertiary"]/text()'
    XPATH_PRODUCT_BRAND = '//div[@class="a-section a-spacing-none"]/a[@id="bylineInfo"]/text()'
    raw_product_price = parser.xpath(XPATH_PRODUCT_PRICE)
    product_price = ''.join(raw_product_price).replace(',', '')
    product_brand = parser.xpath(XPATH_PRODUCT_BRAND)
    raw_product_name = parser.xpath(XPATH_PRODUCT_NAME)
    product_name = ''.join(raw_product_name).strip()
    total_ratings = parser.xpath(XPATH_AGGREGATE_RATING)
    availability = parser.xpath(XPATH_PRODUCT_AVAILABILITY)
    if (availability):
        availability = (availability)[0].strip().rstrip('.')
    category = parser.xpath(XPATH_PRODUCT_CATEGORY)
    if (category):
        category = (category)[0].strip()
    list_price = parser.xpath(XPATH_PRODUCT_LIST_PRICE)
    sub_category = parser.xpath(XPATH_SUB_CATEGORY)
    product_brand = parser.xpath(XPATH_PRODUCT_BRAND)
    reviews = parser.xpath(XPATH_REVIEW_SECTION_1)
    if not reviews:
        reviews = parser.xpath(XPATH_REVIEW_SECTION_2)
    ratings_dict = {}
    reviews_list = []
    details = []

    # grabing the rating  section in product page
    for ratings in total_ratings:
        extracted_rating = ratings.xpath('./td//a//text()')
        if extracted_rating:
            rating_key = extracted_rating[0]
            raw_raing_value = extracted_rating[1]
            rating_value = raw_raing_value
            if rating_key:
                ratings_dict.update({rating_key: rating_value})

    #getting url for all reviews
    next_page = parser.xpath(
        ".//div[@id='reviewsMedley']/div[@class='a-column a-span8']/div[@id='cr-medley-top-reviews-wrapper']/div[@id='reviews-medley-footer']/div[@class='a-row a-spacing-large']/a[@class='a-link-emphasis a-text-bold']/@href")
    print("next_page url intially     ", next_page)
    next_page = parser.xpath(
        "//div[@id='reviewsMedley']/div[@class='a-column a-span8']/div[@id='cr-medley-top-reviews-wrapper']/div[@id='reviews-medley-footer']/div[@class='a-row a-spacing-large']/a[@class='a-link-emphasis a-text-bold']/@href")
    print("next_page url intially     ", next_page)
    if(len(next_page)>0):
        print("on first page", product_name, category)
        details =  gettingIndividualReviews("https://www.amazon.com"+next_page[0], settings.headers, category, product_name)
    # Parsing individual reviews


    data =  {"business_item_data": {
            "business_type": "",
            "absolute_url": amazon_url,
            "category": category,
            "name": product_name,
            "sub_category": "",
            "picture_urls": "",
            "original_price": product_price,
            "sale_price": list_price,
            "availability": availability,
            "specifications": "",
            "website_name": "",
            "description": ""
        },
            "reviews": details

        }

    return data
    #     except ValueError:
    #         print("Retrying to get the correct response")

    # return {"error":"failed to process the page","asin":asin}


def ReadAsin():
    # Add your own ASINs here
    AsinList = ['B01K6FEU1I']
    extracted_data = []
    for asin in AsinList:
        print("Downloading and processing page http://www.amazon.com/dp/" + asin)
        extracted_data.append(ParseReviews(asin))
        sleep(5)
    f = open('data.json', 'w')
    json.dump(extracted_data, f, indent=4)

def gettingIndividualReviews(page_url, headers, category, product_name):
    proxies = get_proxy()
    page = requests.get(page_url, headers=settings.headers, proxies=proxies)
    page_response = page.text
    parser = html.fromstring(page_response)
    reviews_list = []
    next_page = parser.xpath(
        ".//div[@id='cm_cr-review_list']/div[@class='a-form-actions a-spacing-top-extra-large']/span[@class='a-declarative']/div[@id='cm_cr-pagination_bar']/ul[@class='a-pagination']/li[@class='a-last']/a/@href")
    print("next_page url in nexted     ", next_page, len(next_page))
    if len(next_page) > 0:
        reviews_list = gettingIndividualReviews("https://www.amazon.com" + next_page[0], headers, category, product_name)

    XPATH_REVIEW_SECTION_1 = '//div[contains(@id,"reviews-summary")]'
    XPATH_REVIEW_SECTION_2 = '//div[@data-hook="review"]'
    reviews = parser.xpath(XPATH_REVIEW_SECTION_1)
    if not reviews:
        reviews = parser.xpath(XPATH_REVIEW_SECTION_2)

    for review in reviews:
        XPATH_RATING = './/i[@data-hook="review-star-rating"]//text()'
        XPATH_REVIEW_HEADER = './/a[@data-hook="review-title"]//text()'
        XPATH_REVIEW_POSTED_DATE = './/span[@data-hook="review-date"]//text()'
        XPATH_REVIEW_TEXT_1 = '//span[@data-hook="review-body"]//text()'
        XPATH_REVIEW_TEXT_2 = './/div//span[@data-action="columnbalancing-showfullreview"]/@data-columnbalancing-showfullreview'
        XPATH_REVIEW_COMMENTS = './/span[@data-hook="review-comment"]//text()'
        XPATH_AUTHOR = './/span[contains(@class,"profile-name")]//text()'
        XPATH_REVIEW_TEXT_3 = './/div[contains(@id,"dpReviews")]/div/text()'


        raw_review_author = review.xpath(XPATH_AUTHOR)
        raw_review_rating = review.xpath(XPATH_RATING)
        raw_review_header = review.xpath(XPATH_REVIEW_HEADER)
        raw_review_posted_date = review.xpath(XPATH_REVIEW_POSTED_DATE)
        raw_review_text1 = review.xpath(XPATH_REVIEW_TEXT_1)
        raw_review_text2 = review.xpath(XPATH_REVIEW_TEXT_2)
        raw_review_text3 = review.xpath(XPATH_REVIEW_TEXT_3)

        # cleaning data
        author = ' '.join(' '.join(raw_review_author).split())
        review_rating = ''.join(raw_review_rating).replace('out of 5 stars', '')
        review_header = ' '.join(' '.join(raw_review_header).split())

        try:
            review_posted_date = dateparser.parse(''.join(raw_review_posted_date)).strftime('%d %b %Y')
        except:
            review_posted_date = None
        review_text = ' '.join(' '.join(raw_review_text1).split())

        # grabbing hidden comments if present
        if raw_review_text2:
            json_loaded_review_data = json.loads(raw_review_text2[0])
            json_loaded_review_data_text = json_loaded_review_data['rest']
            cleaned_json_loaded_review_data_text = re.sub('<.*?>', '', json_loaded_review_data_text)
            full_review_text = review_text + cleaned_json_loaded_review_data_text
        else:
            full_review_text = review_text
        if not raw_review_text1:
            full_review_text = ' '.join(' '.join(raw_review_text3).split())

        raw_review_comments = review.xpath(XPATH_REVIEW_COMMENTS)
        review_comments = ''.join(raw_review_comments)
        review_comments = re.sub('[A-Za-z]', '', review_comments).strip()
        review_dict = {
            # review_comment_count':review_comments,
            "absolute_url": "",
            "rating": utils.getStarts(review_rating),
            "review_title": review_header,
            "reviewed_at": utils.convertDate(review_posted_date),
            "reviewer_name": author,
            "category": category,
            "product_name": product_name,
            "review_text": full_review_text,
            "picture_urls": "",
            "website_name": "AMAZON"

        }
        reviews_list.append(review_dict)
    return reviews_list


if __name__ == '__main__':
    ReadAsin()