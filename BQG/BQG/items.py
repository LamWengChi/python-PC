# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BqgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 书名
    title = scrapy.Field()
    # 详情链接
    link = scrapy.Field()
    # 最新章节
    new_chapter = scrapy.Field()
    # 作者
    author = scrapy.Field()
