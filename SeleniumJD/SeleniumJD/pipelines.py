# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from SeleniumJD import settings

# 存储至mongodb
class MongodbPipeline (object):
    def __init__(self):
        host = settings.MONGO_HOST
        port = settings.MONGO_PORT
        dbname = settings.MONGO_DBNAME
        sheetname = settings.MONGO_SHEETNAME
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host,port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.post = mydb[sheetname]

    def process_item(self,item,spider):
        data = dict(item)
        self.post.insert(data)
        return item

