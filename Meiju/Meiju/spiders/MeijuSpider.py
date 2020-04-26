# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from Meiju.items import MeijuSpiderItem


class MeijuspiderSpider(scrapy.Spider):
    name = 'MeijuSpider'
    allowed_domains = ['meijutt.tv']
    start_urls = ['https://www.meijutt.tv/new100.html']

    def parse(self, response):
        content = etree.HTML(response.body.decode('GBK'))
        movies = content.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movies:
            # print(movie)
            # 电影名
            a_list = movie.xpath('./h5/a')[0].text
            # 状态
            stats = movie.xpath('.//span[@class="state1 new100state1"]/font')[0].text
            # print(stats)

            item = MeijuSpiderItem()

            item['name'] = a_list
            item['staste'] = stats
            print(a_list,"..............",stats)

            yield item