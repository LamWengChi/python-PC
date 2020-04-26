# -*- coding: utf-8 -*-
import scrapy
import os
import time
from urllib import request
from LJ.items import LjItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']

    # start_urls = ['http://lianjia.com/']

    # 定义url地址
    def start_requests(self):
        start_urls = []
        # 循环取出5页
        for page in range(1, 2):
            url = 'https://wh.lianjia.com/zufang/hongshan/pg{}/'.format(str(page))
            start_urls.append(url)
        for start_url in start_urls:
            yield scrapy.Request(url=start_url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # 详情链接
        links = response.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[1]/a/@href').extract()
        for link in links:
            link = 'https://wh.lianjia.com' + link
            yield scrapy.Request(url=link,  callback=self.parse_url, )
            # print(link)
            time.sleep(0.5)

    def parse_url(self, response):
        item = LjItem()
        # 名字
        name = response.xpath('//div[@class="content clear w1150"]/p/text()').extract()[0]

        # 租赁方式
        lease = response.xpath('//ul[@class="content__aside__list"]/li[1]/text()').extract()[0]
        # 价格
        money = response.xpath('//*[@id="aside"]/div/span/text()').extract()[0]
        # 房屋类型
        type = response.xpath('//*[@id="aside"]/ul/li[2]/text()').extract()[0]
        # 朝向楼层
        aspect_floor = response.xpath('//*[@id="aside"]/ul/li[3]/text()').extract()[0]
        item['name'] = name
        item['lease'] = lease
        item['money'] = money
        item['type'] = type
        item['aspect_floor'] = aspect_floor
        # yield item
        print(item)

        # # 图片链接
        # img_urls = response.xpath('//*[@id="prefix"]/li/img/@src').extract()
        # # print(img_urls)
        # # 图片地址
        # house_imgdir = '/home/tlxy/桌面/项目练习/Scrapy_env/LJ/LJ/img/' + name
        # print(house_imgdir)
        # # 如果图片不为空：
        # if len(img_urls) != 0:
        #     for img_url in img_urls:
        #         # 图片名称
        #         img_name = str(time.time()) + '.jpg'
        #         # 判断图片存储路径是否存在，如果不存在则创建目录
        #         if not os.path.exists(house_imgdir):
        #             os.makedirs(house_imgdir)
        #         # 图片下载
        #         request.urlretrieve(img_url, house_imgdir + "/" + img_name)
        #         time.sleep(0.5)