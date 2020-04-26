# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoSItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'products'
    # 图片链接
    image = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 付款人数
    deal = scrapy.Field()
    # 标签
    title = scrapy.Field()
    # 店铺名
    shop = scrapy.Field()
    # 地址
    location = scrapy.Field()



