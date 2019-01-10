# -*- coding: utf-8 -*-

import scrapy
import time
import re
from urllib import parse
from scrapy.http import Request
from BaiDuSearcher.items import GoogleItem  # 导入item

class searchSpider(scrapy.Spider):
    name = "googlesearch"
    allowed_domains = ["www.google.com"]

    # start_urls = ['http://www.baidu.com/s?q=&tn=baidulocal&ct=2097152&si=&ie=utf-8&cl=3&wd=seo%E5%9F%B9%E8%AE%AD']

    start_urls = []
    for word in open('spiders/word.txt'):
         print(word)
         word = word.strip()
         url = 'https://www.google.com/search?q=%s' % parse.quote(word)
         start_urls.append(url)

    # def start_requests(self):
    #     for word in open('spiders/word.txt'):
    #         print(word)
    #         word = word.strip()
    #         url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=%s' % parse.quote(word)
    #         # start_urls.append(url)
    #         yield Request(url, self.parse)

    def __get_url_query(self, url):
         m = re.search("wd=(.*)", url).group(1)
         return m

    def parse(self,response):
        print('解析谷歌搜索返回')
        print(response)
        return self.parseOnePage(response)

    # def start_request_next_page(self):
    #     for word in open('spiders/word.txt'):
    #         print(word)
    #         word = word.strip()
    #         url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=%s' % parse.quote(word)
    #         # start_urls.append(url)
    #         yield Request(url, self.parse)

    def getMailAddFromFile(self, response):
        regex = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)
        mails = re.findall(regex, response.text)
        matchMails = {}
        for mail in mails:
            pattern = re.compile(r"/\.[jpg|gif|png]/i");
            match = pattern.findall(mail)
            if match:
                matchMails.append(mail)

        mails_str = ','.join(matchMails)
        return mails_str

    def parseMail(self, response):
        item = response.meta['item']
        item['mail'] = self.getMailAddFromFile(response)
        print('解析邮箱返回')
        print(item)
        yield item

    def parseOnePage(self,response):
        n = 0
        url_to_follow = response.css(".r>a::attr(href)").extract()
        url_to_follow = [url.replace('/url?q=', '') for url in url_to_follow]
        for url in url_to_follow:
            print('解析页面')
            print(url)
            item = GoogleItem()
            item['url'] = url
            request = Request(url, callback=self.parseMail, dont_filter=True)
            request.meta['item'] = item
            yield request

        next_pages_urls = response.css("#foot table a::attr(href)").extract()
        for page_num, url in enumerate(next_pages_urls):
            if (page_num < 11):
                next_page_url = response.urljoin(url)
                yield scrapy.Request(
                    url=next_page_url, callback=self.parse, dont_filter=True)
            else:
                break