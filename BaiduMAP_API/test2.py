import requests

def getjson(loc,page_num=0):
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3'
    }
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
   # '湖北省'
    return decodejson


provice_list = ['湖北省']
for eachprovience in provice_list:
    decodejson=getjson(eachprovience)
    for eachcity in decodejson['results']:
        print(eachcity)
        city = eachcity['name']
        num = eachcity['num']
        output = '\t'.join([city,str(num)])+'\n'
        with open('cities.txt','a',encoding="utf-8") as f:
            f.write(output)