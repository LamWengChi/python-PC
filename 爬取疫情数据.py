import requests
import json
import time
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

# 文件名称
ExcelName = '4.25疫情日报.csv'

#当前日期时间戳
number = int(format(time.time() * 100, '.0f'))

# 历史数据
# history_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=&_=%d' % number
# 实时数据
live_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' %number

datas = json.loads(requests.get(live_url,headers=headers).json()['data'])

print('更新时间：' + datas['lastUpdateTime'])

# 写入更新时间
with open(ExcelName,'a',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['更新时间：'+ datas['lastUpdateTime']])

for contry in datas['areaTree']:
    if contry['name'] == '中国':
        for province in contry['children']:
            print(province['name'])
            # 写入省份名称
            with open(ExcelName, 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([province['name']])
            # print('....................................................................')
            for city in province['children']:
                print(city['name'],'今日新增：'+ str(city['today']['confirm']),'确诊：'+ str(city['total']['confirm']),'治愈：'+ str(city['total']['heal']),'死亡：'+ str(city['total']['dead']))
                # 写入市的名称，新增，确诊，死亡，治愈的人数
                with open(ExcelName, 'a', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([city['name'],'今日新增：'+ str(city['today']['confirm']),'确诊：'+ str(city['total']['confirm']),'治愈：'+ str(city['total']['heal']),'死亡：'+ str(city['total']['dead'])])