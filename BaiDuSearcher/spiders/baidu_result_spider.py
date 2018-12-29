# -*- coding: utf-8 -*-

import scrapy, re,os
from urllib import parse
from scrapy.http import Request
from BaiDuSearcher.items import BaidusearcherItem  # 导入item

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["www.baidu.com"]

    # start_urls = ['http://www.baidu.com/s?q=&tn=baidulocal&ct=2097152&si=&ie=utf-8&cl=3&wd=seo%E5%9F%B9%E8%AE%AD']

    start_urls = []
    for word in open('spiders/word.txt'):
         print(word)
         word = word.strip()
         url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=%s' % parse.quote(word)
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
        n = 0
        print('解析百度返回')
        print(response)

        current_page = int(response.xpath('//div[@id="page"]/strong/span[@class="pc"]/text()').extract_first())
        lading = ''
        # lading = response.xpath('//div[@id="content_left"]/div[@class="result c-container "]/div[@class="c-abstract"]/text()').extract_first()
        print('当前页面')
        print(current_page)
        print(lading)
        for sel in response.xpath('//div[@id="content_left"]/div[@class="result c-container "]/h3/a'):
            print('解析页面')
            # query = parse.unquote(self.__get_url_query(response.url))

            item = BaidusearcherItem()
            title = ''.join(sel.xpath('./em/text() | ./text()').extract())
            page = current_page;
            query = sel.xpath('@href').extract()

            n += 1

            item['rank'] = n
            item['title'] = title.encode('utf8')
            item['lading'] = lading.encode('utf8')
            item['page'] = page
            item['query'] = query

            yield item