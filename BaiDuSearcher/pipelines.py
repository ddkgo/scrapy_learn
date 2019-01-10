# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import logging
import hashlib
from twisted.enterprise import adbapi
import pymysql

class BaidusearcherPipeline(object):
    def __init__(self, dbpool,mysqlList):
        self.dbpool = dbpool
        self.mysqlList = mysqlList

    @classmethod
    def from_settings(cls, settings):
        mysqlList = [settings['MYSQL_HOST'],settings['MYSQL_USER'],settings['MYSQL_PASSWD'],settings['MYSQL_DBNAME']]
        dbpool = pymysql.connect(mysqlList[0],mysqlList[1],mysqlList[2],mysqlList[3])
        # 使用 execute() 方法执行 SQL，如果表不存在就创建
        cursor = dbpool.cursor()

        # 使用预处理语句创建表
        sqlDel = "DROP TABLE IF EXISTS BAIDU_RESULT;"

        sql = """CREATE TABLE IF NOT EXISTS BAIDU_RESULT(
                        Id INT PRIMARY KEY AUTO_INCREMENT,
                        rank VARCHAR(100),
                        title VARCHAR(100),
                        lading VARCHAR(100),
                        page INT(64),
                        query VARCHAR(1000),
                        baiduQuery VARCHAR(1000),
                        mail VARCHAR(1000))"""

        sqlMail = """CREATE TABLE IF NOT EXISTS EMAIL_BAIDU_RESULT(
                                Id INT PRIMARY KEY AUTO_INCREMENT,
                                email VARCHAR(100),
                                times INT(100),
                                lastStamp DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"""

        sqlGoogle = """CREATE TABLE IF NOT EXISTS GOOGLE_RESULT(
                                        Id INT PRIMARY KEY AUTO_INCREMENT,
                                        url VARCHAR(1000),
                                        mail VARCHAR(1000),
                                        lastStamp DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"""

        # cursor.execute(sqlDel)
        cursor.execute(sql)
        cursor.execute(sqlGoogle)
        cursor.execute(sqlMail)
        return cls(dbpool,mysqlList)

    def dbHandle(self):
        mysqlList = self.mysqlList
        dbpool = pymysql.connect(mysqlList[0],mysqlList[1],mysqlList[2],mysqlList[3])
        return dbpool
    # pipeline默认调用
    def process_item(self, item, spider):
        print(item)
        dbObject = self.dbpool
        cursor = dbObject.cursor()
        if spider.name == 'search':
            sql = "INSERT INTO BAIDU_RESULT(rank,title,lading,page,query,baiduQuery,mail) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            try:
                cursor.execute(sql, (
                    item['rank'], item['title'], item['lading'], item['page'], item['query'], item['baiduQuery'],
                    item['mail']))
                cursor.connection.commit()
            except BaseException as e:
                print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
                dbObject.rollback()
        if spider.name == 'googlesearch':
            sql = "INSERT INTO GOOGLE_RESULT(url,mail) VALUES(%s,%s)"
            try:
                cursor.execute(sql, (
                    item['url'],item['mail']))
                cursor.connection.commit()
            except BaseException as e:
                print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
                dbObject.rollback()
        elif spider.name == 'emailSend':
            sql = "INSERT INTO EMAIL_BAIDU_RESULT(email,times) VALUES(%s,%s)"
            try:
                cursor.execute(sql, (
                    item['email'],0))
                cursor.connection.commit()
            except BaseException as e:
                print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
                dbObject.rollback()

        return item




