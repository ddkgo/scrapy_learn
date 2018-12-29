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
        sql = """CREATE TABLE IF NOT EXISTS BAIDU_RESULT(
                Id INT PRIMARY KEY AUTO_INCREMENT,
                rank VARCHAR(100),  
                title VARCHAR(100), 
                lading VARCHAR(100), 
                page INT(64), 
                query VARCHAR(1000))"""

        cursor.execute(sql)
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
        # cursor.execute("USE BAIDU_RESULT")
        sql = "INSERT INTO BAIDU_RESULT(rank,title,lading,page,query) VALUES(%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql, (
            item['rank'], item['title'], item['lading'], item['page'], item['query']))
            cursor.connection.commit()
        except BaseException as e:
            print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
            dbObject.rollback()
        return item


