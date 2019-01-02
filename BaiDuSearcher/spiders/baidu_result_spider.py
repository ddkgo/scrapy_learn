# -*- coding: utf-8 -*-

import scrapy
import time
import re
from lxml import etree
from urllib import parse
from scrapy.http import Request
from BaiDuSearcher.items import BaidusearcherItem  # 导入item

class searchSpider(scrapy.Spider):
    name = "search"
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
        print('解析百度返回')
        print(response)
        return self.parseOnePage(response)

    # def start_request_next_page(self):
    #     for word in open('spiders/word.txt'):
    #         print(word)
    #         word = word.strip()
    #         url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=%s' % parse.quote(word)
    #         # start_urls.append(url)
    #         yield Request(url, self.parse)

    def parseOnePage(self,response):
        n = 0
        current_page = int(response.xpath('//div[@id="page"]/strong/span[@class="pc"]/text()').extract_first())
        lading = ''
        # lading = response.xpath('//div[@id="content_left"]/div[@class="result c-container "]/div[@class="c-abstract"]/text()').extract_first()
        print('当前页面')
        print(current_page)
        print(lading)

        if current_page > 1:
            return
        # 下一页
        nextUrlTemp = response.xpath('//div[@id="page"]/a[span[@class="pc"] = $val]/@href',val = current_page+1).extract()
        nextUrl = 'https://www.baidu.com' + nextUrlTemp[0]
        print('下一页路径')
        print(nextUrl)
        for sel in response.xpath('//div[@id="content_left"]/div[@class="result c-container "]'):
            print('解析页面')
            item = BaidusearcherItem()
            title = ''.join(sel.xpath('./h3/a/em/text() | ./h3/a/text()').extract())
            page = current_page
            baiduQuery = sel.xpath('./h3/a/@href').extract()
            querySel = sel.xpath('./div/div/div/a[@class="c-showurl"] | ./div/a[@class="c-showurl"]')
            query = ''
            for result in querySel.xpath('.'):
                query = query.join(result.xpath('string(.)').extract_first().strip())

            # 将正则表达式编译成Pattern对象
            pattern = re.compile(r'bike')
            match = pattern.findall(query)
            if match:
                n += 1
                item['rank'] = n
                item['title'] = title.encode('utf8')
                item['lading'] = lading.encode('utf8')
                item['page'] = page
                item['query'] = query
                item['baiduQuery'] = baiduQuery
                item['mail'] = 0
                yield item

        time.sleep(3)
        yield Request(nextUrl, self.parse)

    def parseMail(self,response):
        return 0
