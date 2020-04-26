# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs,json

class YgrxPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonYgPipeline(object):
    def __init__(self):
        # 创建一个只读文件，编码格式为utf-8
        self.filename = codecs.open('ygrx.json','w',encoding='utf-8')

    def process_item(self,item,spider):
        content = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.filename.write(content)
        return item

    def spider_closed(self,spider):
        # 关闭文件
        self.filename.close()
