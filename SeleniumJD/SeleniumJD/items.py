# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy


class JdspiderItem(scrapy.Item):
    # 链接
    url = scrapy.Field()
    # 名称
    name_s = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 评论
    comment = scrapy.Field()

