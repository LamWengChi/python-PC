import random
from scrapy.http import HtmlResponse

class JdDownloaderMiddleware(object):
    def process_response(self,request,response,spider):
        if spider.name == 'Jd':
            # 使用selenium打开链接，返回渲染页面
            spider.browser.get(url=request.url)
            # 模拟下拉浏览器
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.get(url=response.url)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class ProxyMiddleware(object):
    '''
    设置Proxy
    '''

    def __init__(self, ip):
        self.ip = ip

    @classmethod
    def from_crawler(cls, crawler):
        return cls(ip=crawler.settings.get('PROXIES'))

    def process_request(self, request, spider):
        ip = random.choice(self.ip)
        request.meta['proxy'] = ip
