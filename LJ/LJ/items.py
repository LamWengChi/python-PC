# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 价格
    money = scrapy.Field()
    # 租赁方式
    lease = scrapy.Field()
    # 房屋类型
    type = scrapy.Field()
    # 朝向楼层
    aspect_floor = scrapy.Field()
