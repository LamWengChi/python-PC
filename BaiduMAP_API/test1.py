"""
注册百度地图API账号进行开发者认证
目标:获取全国公园信息并保存至MySQL数据库中
地点检索详情链接:
http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥 //GET请求

基础地址
http://api.map.baidu.com/place/v2/search
参数:
    query:公园
    region:武汉市
    scope:2
    page_size:20
    output:json
    ak:ZFYL6UZmBIPQd7yOQI0GpahpU9U5tkaL
"""
import requests

def getjson(loc,page_num=0):
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3'
    }
    # http://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行&region=北京&output=json&ak=您的ak //GET请求
    data = {
        'query':"公园",
        'region':loc,
        'scope':"2",
        'page_size':20,
        'page_num':page_num,
        'output':"json",
        'ak':'ZFYL6UZmBIPQd7yOQI0GpahpU9U5tkaL'
    }
    url = 'http://api.map.baidu.com/place/v2/search'
    res = requests.get(url,params=data,headers=headers)
    decodejson = res.json()

    return decodejson
a = getjson("武汉市")
print(a)