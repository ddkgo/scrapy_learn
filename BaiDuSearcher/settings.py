# -*- coding: utf-8 -*-

# Scrapy settings for BaiDuSearcher project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os
import random
BOT_NAME = 'BaiDuSearcher'

SPIDER_MODULES = ['BaiDuSearcher.spiders']
NEWSPIDER_MODULE = 'BaiDuSearcher.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'BaiDuSearcher (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'BaiDuSearcher.middlewares.BaidusearcherSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'BaiDuSearcher.middlewares.BaidusearcherDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'BaiDuSearcher.pipelines.BaidusearcherPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

ITEM_PIPELINES = {
    'BaiDuSearcher.pipelines.BaidusearcherPipeline': 300,
}
# '''crawlera账号、密码'''
# CRAWLERA_ENABLED = True
# CRAWLERA_USER = '账号'
# CRAWLERA_PASS = '密码'
#
# '''下载中间件设置'''
# DOWNLOADER_MIDDLEWARES = {
#  'scrapy_crawlera.CrawleraMiddleware': 600
# }
USER_AGENTS = [
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# DEFAULT_REQUEST_HEADERS = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.0.4.3000 Chrome/47.0.2526.73 Safari/537.36',
# }

# '''下载中间件设置'''
# DOWNLOADER_MIDDLEWARES = {
#  'BaiDuSearcher.middlewares.RandomUserAgent': 1,
# }

def getCookie():
    cookie_list = [
    'BAIDUID=FEFB4A17B43F98A41516465DECA53344:FG=1; BIDUPSID=FEFB4A17B43F98A41516465DECA53344; PSTM=1541036391; BD_UPN=12314753; MCITY=-179%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ispeed_lsm=0; BDSFRCVID=1CAOJeC62ijlKRQ95rgXhejwTv-ocm3TH6aIYlwMc5V93fSB1t7HEG0PDM8g0Ku-fT5pogKKKgOTHICF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tbIJVI-yfIvbfP0kM4r5hnLfbeT22-ustm7C2hcH0KLKjJc1yp5GejLXbn73K4TfQTFLWbOEtMb1MRjVWtvbXtJ03GueKqJGt6Pfap5TtUJU8DnTDMRhqtK7jq3yKMniWKv9-pnY0hQrh459XP68bTkA5bjZKxtq3mkjbIOFfJOKHIC4j5LKjMK; H_PS_PSSID=1425_21096_28206_28131_26350_27750_28140_22160; sugstore=1; H_PS_645EC=8fcaQu06GNSjCXE6K3pf4gdM5BXBOTjaGe9izkJtFAMPRKMfEwPQGZuMIzovIOIErJ%2Fq; delPer=0; BD_CK_SAM=1; PSINO=7; BDSVRTM=0; ZD_ENTRY=empty', #自己从不同浏览器中获取cookie在添加到这
    'BDRCVFR[SL8xzxBXZJn]=mk3SLVN4HKm; delPer=0; PSINO=7; H_PS_PSSID=; BAIDUID=D2B6F51AE9CEF1B5D3F242753D235E41:FG=1; BIDUPSID=D2B6F51AE9CEF1B5D3F242753D235E41; PSTM=1546063227; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BD_CK_SAM=1; H_PS_645EC=788eSD0bTCWBr2wZt6f3dIim7%2FYSq5xweAU4L3fIheTNCeLyIgfIDtz7hh2h59PtGf2CAg; BD_UPN=1d314753',
    ]
    cookie = random.choice(cookie_list)
    return cookie

'''设置默认request headers'''
DEFAULT_REQUEST_HEADERS = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Host':'www.baidu.com',
'RA-Sid':'7739A016-20140918-030243-3adabf-48f828',
'RA-Ver':'3.0.7',
'Upgrade-Insecure-Requests':'1',
'Cookie':'%s' % getCookie()
}
DEFAULT_REQUEST_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.0.4.3000 Chrome/47.0.2526.73 Safari/537.36',
}

'''下载延时，即下载两个页面的等待时间'''
DOWNLOAD_DELAY = 0.5

'''并发最大值'''
CONCURRENT_REQUESTS = 100

'''对单个网站并发最大值'''
CONCURRENT_REQUESTS_PER_DOMAIN = 100

'''启用AutoThrottle扩展，默认为False'''
AUTOTHROTTLE_ENABLED = False

'''设置下载超时'''
DOWNLOAD_TIMEOUT = 10

'''降低log级别，取消注释则输出抓取详情'''
LOG_LEVEL = 'INFO'

MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'baidu_search_0'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'ou1314520'