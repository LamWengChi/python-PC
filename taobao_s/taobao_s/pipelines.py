# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from openpyxl import Workbook
from taobao_s import settings

class TaobaoSPipeline(object):
    def process_item(self, item, spider):
        return item


# 存储至mongodb
class MongodbPipeline(object):
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

class ExcelPipeline(object):
    def __init__(self):
        self.wb = Workbook() # 类实例化
        self.ws = self.wb.active # 激活工作表
        self.ws.append(['标签', '价格', '付款人数', '店铺名', '地址', '图片链接']) # 添加表头
    def process_item(self, item, spider):  # 工序具体内容
        line = [item['title'], item['price'], item['deal'], item['shop'], item['location'], item['image']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('info.xlsx')
        return item


