# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from YGRX.items import YgrxItem

class YgrxSpider(CrawlSpider):
    name = 'ygrx'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&type=4&page=']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    # 每个页面的匹配规则
    pagelink = LinkExtractor(allow=r'page=\d')
    # print(pagelink)


    # 每个帖子的匹配规则
    contentlink = LinkExtractor(allow=r'index\?id\=\d+')

    rules = [
        Rule(pagelink,follow=True),
        Rule(contentlink,callback='parse_item'),
    ]

    def parse_item(self, response):
        # 标题
        title = response.xpath('//div[@class="mr-three"]/p/text()').extract()[0]
        # 编号
        numbers = response.xpath('//div[@class="mr-three"]/div[1]/span[4]/text()').get()
        number = numbers.split('：')[-1]
        # 内容
        content = response.xpath('//div[@class="details-box"]/pre/text()').extract()

        item = YgrxItem()
        item['title'] = title
        item['number'] = number
        item['content'] =content
        item['url']= response.url


        print(item)
        yield item