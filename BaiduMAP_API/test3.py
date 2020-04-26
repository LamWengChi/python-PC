import requests
import json
from BaiduMAP_API.MysqlAPI import Sql
import time
import random

# 代理
proxy_list = [
    {"https":"171.35.162.90"},
    {"https":"113.121.21.175"},
    {"http":"123.180.211.79"}

]

# 随机取一个
proxies = random.choice(proxy_list)

city_list = []
with open('/home/tlxy/桌面/项目练习/BaiduMAP_API/cities.txt', 'r', encoding='utf-8') as f:
    for eachline in f:
        # print(eachline)
        fileds = eachline.split('\t')
        city = fileds[0]
        city_list.append(city)


# print(city_list)
# print(len(city_list))

def getjson(loc, page_num=0):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3'
    }
    data = {
        'query': "公园",
        'region': loc,
        'scope': "2",
        'page_size': 20,
        'page_num': page_num,
        'output': "json",
        'ak': 'ZFYL6UZmBIPQd7yOQI0GpahpU9U5tkaL'
    }
    url = 'http://api.map.baidu.com/place/v2/search'
    res = requests.get(url, params=data, headers=headers,proxies=proxies)
    # decodejson = res.json()
    decodejson = json.loads(res.text)
    # '湖北省'
    return decodejson


for eachcity in city_list:
    flag = True
    page_num = 0
    while flag:
        decodejson = getjson(eachcity, page_num)
        # print(eachcity,page_num)
        if decodejson['results']:
            for eachone in decodejson['results']:
                # print(eachone)
                try:
                    park = eachone['name']
                except:
                    park = None
                try:
                    location_lat = eachone['loaction']['lat']
                except:
                    location_lat = None
                try:
                    location_lng = eachone['loaction']['lng']
                except:
                    location_lng = None
                try:
                    address = eachone['address']
                except:
                    address = None
                try:
                    street_id = eachone['street_id']
                except:
                    street_id = None
                try:
                    uid = eachone['uid']
                except:
                    uid = None

                print(eachcity,park,location_lat,location_lng,address,street_id,uid)
                Sql.insert_city(eachcity,park,location_lat,location_lng,address,street_id,uid)
            page_num += 1
            time.sleep(2)
        else:
            flag = False
