# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeijuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 定义一个模型，用于明确要抓取的信息
class MeijuSpiderItem(scrapy.Item):
    name = scrapy.Field()  # 电影名
    staste = scrapy.Field()  # 状态
