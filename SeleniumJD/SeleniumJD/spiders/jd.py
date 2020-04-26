import scrapy
import time
from SeleniumJD.items import JdspiderItem
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class JdSpider(scrapy.Spider):
    name = 'Jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=670,671,672']

    def __init__(self):
        """
        在爬虫内初始化 selenium
        减少selenium的开关次数
        """
        super().__init__()
        # 有界面
        self.browser = webdriver.Chrome()
        # 超时设置
        self.browser.set_page_load_timeout(30)

    def closed(self,spider):
        """爬虫结束自动关闭selenium"""
        self.browser.close()
        self.browser.quit()

    def parse(self, response):
        item = JdspiderItem()
        li_list = response.xpath('//ul[@class="gl-warp clearfix"]/li')
        for li in li_list:
            # 链接
            urls = li.xpath('.//div[@class="p-img"]/a/@href').getall()[0]
            url = 'https:' + urls
            # 名称
            name_s = li.xpath('.//div[@class="p-name"]/a/em/text()').getall()[0].strip()
            # 价格
            price = li.xpath('.//div[@class="p-price"]/strong/i/text()').getall()[0]
            # 评论
            comment = li.xpath('.//div[@class="p-commit p-commit-n"]/strong/a/text()').getall()[0]
            time.sleep(0.5)
            item['url'] = url
            item['name_s'] = name_s
            item['price'] = price
            item['comment'] = comment
            # print(item)
            yield item

            next_page = response.xpath('.//a[@class="pn-next"]/@href').getall()
            if next_page:
                next_page = "https://list.jd.com" + next_page[0]
                yield scrapy.Request(next_page,callback=self.parse)