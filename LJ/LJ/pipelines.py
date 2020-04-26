# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs
import pymongo
from LJ import settings

class LjPipeline(object):
    def process_item(self, item, spider):
        return item



# 保存到CSV文件中
class CsvPipeline(object):

    def __init__(self):
        self.file = codecs.open('a.csv', 'w', encoding='utf_8_sig')

    def process_item(self, item, spider):
        fieldnames = ['name', 'money', 'lease','type','aspect_floor']
        w = csv.DictWriter(self.file, fieldnames=fieldnames)
        w.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()



# 存储至mongodb

class LjSpiderPipeline(object):
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