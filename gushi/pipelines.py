# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonLinesItemExporter
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors


# class GushiPipeline(object):
#     def __init__(self):
#         dbparams = {
#             "host": '127.0.0.1', # 数据库ip
#             "port": 3306, # 端口
#             "user": "root", # 用户
#             "password": "password", # 密码
#             "database": "jianshu", # 需要连接的数据库
#             "charset": "utf8", # 以utf-8形式
#         }
#         self.conn = pymysql.connect(**dbparams)
#         self.cursor = self.conn.cursor()
#         self._sql = None
#
#     def process_item(self, item, spider):
#         self.cursor.execute(self.sql, (item["text"],item['title']))
#         self.conn.commit()
#         return item
#
#     @property
#     def sql(self):
#         if not self._sql:
#             # sql语句
#             self._sql = """
#             insert into abc(id,text,title) values(null,%s,%s)
#             """
#             return self._sql
#         return self._sql

# 异步方法存储到pymysql
# class GushiTwistedPipeline(object):
#     def __init__(self):
#         dbparams = {
#             "host":"127.0.0.1",
#             "port":"3306",
#             "user":"root",
#             "password":"password",
#             "database":"jianshu",
#             "charset":"utf8",
#             "cursorclass":cursors.DictCursor # 游标的类
#         }
#         self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
#         self._sql = None
#         # return self.dbpool
#
#
#     @classmethod
# #     def sql(self):
# #         if not self._sql:
# #             # sql语句
#             self._sql = """
#                 insert into abc(id,title,text) values(null,%s,%s)
#                 """
#             return self._sql
#         return self._sql
#
#     def process_item(self, item, spider):
#         defer = self.dbpool.runInteraction(self.insert_item,item)
#         defer.addErrback(self.handle_error,item,spider)
#
#     def insert_item(self,cursor,item):
#
#         cursor.execute(self.sql, (item["title"],item['text']))
#
#     def handle_error(self,error,item,spider):
#         print("-" * 10 + "error" + '-' * 10)
#         print(error)
#         print("-" * 10 + "error" + '-' * 10)

class GushiTwistedPipeline(object):
    def __init__(self):
        dbparams = {
                        "host": '127.0.0.1', # 数据库ip
                        "port": 3306, # 端口
                        "user": "root", # 用户
                        "password": "password", # 密码
                        "database": "jianshu", # 需要连接的数据库
                        "charset": "utf8", # 以utf-8形式
                    }
        # 使用Twisted中的adbapi获取数据库连接池对象
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)


    def process_item(self, item, spider):
        # 使用数据库连接池对象进行数据库操作,自动传递cursor对象到第一个参数
        query = self.dbpool.runInteraction(self.do_insert, item)
        # query = self.dbpool.runInteraction(self.do_insert,item)
        # 设置出错时的回调方法,自动传递出错消息对象failure到第一个参数
        query.addErrback(self.on_error, spider)
        return item

    def do_insert(self, cursor, item):
        sql = 'insert into abc(id,title,text) values(null,%s,%s)'
        args = (item['title'], item['text'])
        cursor.execute(sql, args)

    def on_error(self, failure, spider):
        spider.logger.error(failure)
