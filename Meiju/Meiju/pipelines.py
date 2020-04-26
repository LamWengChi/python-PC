# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import codecs,json


class MeijuPipeline(object):
    def process_item(self, item, spider):
        return item


# class MejuSpiderPipeleline(object):
#     def __init__(self):
#         self.file = open('meiju.json', 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         # 数据存储
#         json.dump(dict(item), open("meiju.json", 'a'), ensure_ascii=False)
#         return item
#
#     def close_spider(self):
#         self.file.close()


class MejuSpiderPipeleline(object):
    def __init__(self):
        # 创建一个只读文件，编码格式为utf-8
        self.filename = codecs.open('novel.json', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(content)
        return item


    def close_spider(self, spider):
        self.filename.close()


