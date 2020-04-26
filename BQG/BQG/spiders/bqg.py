# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from BQG.items import BqgItem
import time

class BqgSpider(CrawlSpider):
    name = 'bqg'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/fenlei/1_1.html']
    # 每一页链接
    page = LinkExtractor(allow=r'\d\_\d+\.html')
    # print(page)

    rules = (
        Rule(page,callback='parse_item',follow=True),
    )

    # # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        oods = response.xpath('//div[@class="l"]/ul/li')
        for ood in oods:
            #书名
            title = ood.xpath('./span[1]/a/text()').extract()[0]
            # 详情链接
            link = ood.xpath('./span[1]/a/@href').extract()[0]
            # 最新章节
            new_chapter = ood.xpath('./span[2]/a/text()').extract()[0]
            # 作者
            author = ood.xpath('./span[3]/text()').extract()[0]
            # print(title,link,new_chapter,author)
            item = BqgItem()
            item["title"] = title
            item["link"] = link
            item["new_chapter"] = new_chapter
            item["author"] = author
            time.sleep(0.1)
            print(title)
            yield item