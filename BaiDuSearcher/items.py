# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidusearcherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    lading = scrapy.Field()
    page = scrapy.Field()
    query = scrapy.Field()
    baiduQuery = scrapy.Field()
    mail = scrapy.Field()
    pass


class BaiduSendEmailItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    email = scrapy.Field()
    pass

class GoogleItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    mail = scrapy.Field()
    pass