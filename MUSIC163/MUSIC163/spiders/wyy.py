# -*- coding: utf-8 -*-
"""
歌曲外链
https://link.hhtjim.com/163/5146554.mp3
"""
# 导入模块
import urllib.request
import csv
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from MUSIC163.items import Music163Item
import time


class WyySpider(CrawlSpider):
    name = 'wyy'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/artist/album?id=7763']

    rules = (
        # 匹配歌单翻页
        Rule(LinkExtractor(allow=r'offset=\d+'), follow=True),
        # 匹配歌单详情
        Rule(LinkExtractor(restrict_xpaths=('//a[@class="tit s-fc0"]')), callback='parse_item'),
    )

    def parse_item(self, response):
        rows = []
        item = Music163Item()
        # 专辑名称
        title = response.xpath('//h2[@class="f-ff2"]/text()').get()
        # 歌手
        singer = response.xpath('//div[@class="topblk"]//p[@class="intr"]//span/a/text()').get()
        # 发行时间
        time = response.xpath('//div[@class="topblk"]//p/text()').get()
        # 专辑介绍
        # print(title)
        introduce1 = response.xpath('//div[@id="album-desc-dot"]//p')
        introduce = ''
        for introduces in introduce1:
            introduce = introduces.xpath('.//text()').get()

            # print(introduce)
        # print('......................')
        content = (title, singer, time,introduce)
        # print(content)
        rows.append(content)
        # 歌曲名称和歌曲id
        lis = response.xpath('//div[@id="song-list-pre-cache"]/ul/li')

        for li in lis:
            # 歌曲名称
            names = li.xpath('./a/text()').get()
            # 歌曲id
            id = li.xpath('./a/@href').get().strip('/song?id=')
            song_urls = 'https://link.hhtjim.com/163/{}.mp3'.format(id)
            # print(song_urls)
            try:
                print('正在下载', names)
                urllib.request.urlretrieve(song_urls, '/home/tlxy/桌面/项目练习/Scrapy_env/MUSIC163/MUSIC163/GEM/%s.mp3' % names)

                print('下载成功')
            except:
                print('下载失败')


        # # 存储为csv
        # head = ["专辑名称", "歌手", "发行时间", "专辑介绍"]
        # # 写入csv文件内容
        # with open('wyys.csv','a',newline='') as f:
        #     f_csv = csv.writer(f)
        #     f_csv.writerow(head)
        #     f_csv.writerow(rows)
        #

