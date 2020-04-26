# -*- coding: utf-8 -*-
import os
import scrapy
from urllib import request
from JBPDF.items import JbpdfItem


class JbpdfSpider(scrapy.Spider):
    name = 'jbpdf'
    allowed_domains = ['jb51.net']
    # start_urls = ['https://www.jb51.net/books/list45_1.html']

    # 定义url地址
    def start_requests(self):
        start_urls = []
        # 循环取出4页
        for page in range(1, 3):
            url = 'https://www.jb51.net/books/list15_{}.html'.format(str(page))
            start_urls.append(url)

        for start_url in start_urls:
            yield scrapy.Request(url=start_url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        infos = response.xpath('//ul[@class="c-list clearfix"]/li/div/p/a/@href').extract()
        for info in infos:
            info = 'https://www.jb51.net' + info
            # print(info)

            yield scrapy.Request(url=info,callback=self.parse_info,dont_filter=True)

    def parse_info(self, response):
        item = JbpdfItem()
        # 书名
        title = response.xpath('//*[@id="soft-name"]/h1/text()').get()

        # 链接
        links = response.xpath('//ul[@class="ul_Address"]/li[1]/a/@href').get()
        link = [links]
        item['title'] = title
        item['file_urls'] = link
        # print(link)
        yield item








