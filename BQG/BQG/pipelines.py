# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook


class ExcelPipeline(object):
    def __init__(self):
        self.wb = Workbook() # 类实例化
        self.ws = self.wb.active # 激活工作表
        self.ws.append(['书名', '详情链接', '最新章节', '作者']) # 添加表头
    def process_item(self, item, spider):  # 工序具体内容
        line = [item['title'], item['link'], item['new_chapter'], item['author']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('BQG.xlsx')
        print('保存成功')
        return item

