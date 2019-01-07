# -*- coding: utf-8 -*-
import scrapy, time
from datetime import datetime
from BaiDuSearcher.spiders.sendEmail import SendEmail
from BaiDuSearcher.items import BaiduSendEmailItem  # 导入item
from scrapy.utils.project import get_project_settings
import pymysql

class EmailSendSpider(scrapy.Spider):
    name = 'emailSend'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    # # 在爬虫启动和关闭的时候，分别发送邮箱，通知爬虫管理者。
    # def start_requests(self):
    #     email = SendEmail()
    #     content = '爬虫启动时间：{}'.format(datetime.now())
    #     email.sendEmail('xxxxxxxx@qq.com', 'yyyyyyyyyyy@qq.com', '爬虫启动', content)
    #
    #     for url in self.start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def cheack_email(self, mail):
        settings = get_project_settings()
        mysqlList = [settings['MYSQL_HOST'], settings['MYSQL_USER'], settings['MYSQL_PASSWD'], settings['MYSQL_DBNAME']]
        dbpool = pymysql.connect(mysqlList[0], mysqlList[1], mysqlList[2], mysqlList[3])
        cursor = dbpool.cursor()

        # SQL 查询语句
        sql = "SELECT * FROM EMAIL_BAIDU_RESULT where email='%s'"%(mail)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            if len(results)>0:
                print("%s,邮件已经发送过了，不重复发送"%mail)
                return False
            else:
                return True
        except:
            print("Error: unable to fetch data")

        # 关闭数据库连接
        dbpool.close()
        return False

    def parse(self, response):
        print('开始读取数据库邮件')
        settings = get_project_settings()
        mysqlList = [settings['MYSQL_HOST'], settings['MYSQL_USER'], settings['MYSQL_PASSWD'], settings['MYSQL_DBNAME']]
        dbpool = pymysql.connect(mysqlList[0], mysqlList[1], mysqlList[2], mysqlList[3])
        cursor = dbpool.cursor()
        totoalMails = []
        # SQL 查询语句
        sql = "SELECT mail FROM BAIDU_RESULT where mail <> ''"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            for row in results:
                mails = row[0]
                mailArry = mails.split(',')
                for mail in mailArry:
                    totoalMails.append(mail)
        except:
            print("Error: unable to fetch data")

        # 关闭数据库连接
        dbpool.close()

        if len(totoalMails) > 0:
            print("start send email!")
            for mail in totoalMails:
                print(mail)
                if self.cheack_email(mail):
                    item = BaiduSendEmailItem()
                    email = SendEmail()

                    # item['name'] = email.sendEmail(mail)
                    item['email'] = mail
                    yield item


    def closed(self, reason):
        # 爬虫关闭的时候，会调用这个方法
        email = SendEmail()
        content = '爬虫关闭时间：{}'.format(datetime.now())
        # email.sendEmail('740462016@qq.com')
