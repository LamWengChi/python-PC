"""
url = 'http://api.map.baidu.com/place/v2/detail'
http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥
http://api.map.baidu.com/place/v2/detail?uid=ab36688b39cd18da0aa8d485&output=json&scope=2&ak=ZFYL6UZmBIPQd7yOQI0GpahpU9U5tkaL
"""
import requests
import json
from BaiduMAP_API.MysqlAPI import Sql
import time
import random

# 代理
proxy_list = [
    {"https":"117.67.142.159:54825"},
    {"https":"223.241.79.79:8010"},
    {"http":"221.122.91.66:80"},
    {"https": "193.112.152.199:3128"},

]

# 随机取一个
proxies = random.choice(proxy_list)


def getjson(uid):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3'
    }
    data = {
        'uid':uid,
        'scope': "2",
        'output': "json",
        'ak': 'ZFYL6UZmBIPQd7yOQI0GpahpU9U5tkaL'
    }
    url = 'http://api.map.baidu.com/place/v2/detail'
    res = requests.get(url, params=data, headers=headers,proxies=proxies)
    # decodejson = res.json()
    decodejson = json.loads(res.text)
    # '湖北省'
    return decodejson



# 从数据库中获取uid号
results = Sql.read_city()
# print(results)
# print(type(results[0])) #类型为元祖
for item in results:
    uid = item[0]
    decodejson = getjson(uid)
    # print(decodejson)
    infos = decodejson['result']
    # print(infos)
    #获取想要的信息


    try:
        #uid
        uid = infos['uid']
    except:
        uid = None
    try:
        #streed_id
        street_id = infos['street_id']
    except:
        street_id = None

    try:
        #name
        name = infos['name']
    except:
        name = None

    try:
        #address
        address = infos['address']
    except:
        address = None
    try:
        #shop_hours
        shop_hours = infos['detail_info']['shop_hours']
    except:
        shop_hours = None

    try:
        #detail_url
        detail_url = infos['detail_info']['detail_url']
    except:
        detail_url = None

    try:
        #content_tag
        content_tag = infos['detail_info']['content_tag']
    except:
        content_tag = None

    print(uid,street_id,name,address,shop_hours,detail_url,content_tag)
    Sql.insert_park(uid,street_id,name,address,shop_hours,detail_url,content_tag)
    time.sleep(0.5)