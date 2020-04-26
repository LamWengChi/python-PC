# -*- coding: utf-8 -*-
import scrapy
import time
from urllib.parse import quote
from taobao_s.items import TaobaoSItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    base_url = 'https://s.taobao.com/search?q='

    # 拼接url,获取settings里的KEYWORDS,MAX_PAGE
    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield scrapy.Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        products = response.xpath('//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class, "item")]')
        for product in products:
            item = TaobaoSItem()
            # 图片链接
            image = ''.join(product.xpath('.//div[@class="pic"]//img[contains(@class, "img")]/@data-src').extract()[0])
            # 价格
            price = ''.join(product.xpath('//div[@class="price g_price g_price-highlight"]/strong/text()').extract()[0])
            # 付款人数
            deal = product.xpath('.//div[contains(@class, "deal-cnt")]//text()').extract_first()
            # 标签
            title = ''.join(product.xpath('.//div[@class="row row-2 title"]/a/text()').extract()).strip()
            # 店铺名
            shop = ''.join(product.xpath('.//div[@class="shop"]/a/span/text()').extract()).strip()
            # 地址
            location = product.xpath('.//div[@class="row row-3 g-clearfix"]/div[2]/text()').extract()[0]
            time.sleep(1)
            item['price'] = price
            item['title'] = title
            item['shop'] = shop
            item['image'] = image
            item['deal'] = deal
            item['location'] = location
            print(item)
            yield item

