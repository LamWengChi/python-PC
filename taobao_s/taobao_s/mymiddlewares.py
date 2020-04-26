from selenium import webdr项目名称：爬取淘宝商品信息
开发环境：Linux +Pycharm + Python3 + Scrapy + Selenium
项目描述：使用Scrapy Selenium模拟用户操作，设置随机代理ip，使用xpath提取页面内容并保存至MySQL
iver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
import time


class SeleniumMiddleware():
    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.Chrome(service_args=service_args)
        # 设置窗口大小
        self.browser.set_window_size(1400, 700)
        # 设置页面加载超时
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)


    def __del__(self):
        # 关闭当前窗口
        self.browser.close()

    def process_request(self, request, spider):
        """

        :param request: Requset对象
        :param spider: Spider对象
        :return: HtmRespose
        """
        self.logger.debug('PhantomJS is Starting')
        page = request.meta.get('page', 1)
        try:
            self.browser.get(request.url)
            if page > 1:
                input = self.wait.until(
                    # 等待直到出现元素
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
                submit = self.wait.until(
                    # 判断元素是否可点击
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
                # clear()清除所有元素
                input.clear()
                # send_keys()输入内容
                input.send_keys(page)
                # click()点击
                submit.click()
                time.sleep(2)
            self.wait.until(
                # 判断文本是否存在
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
            self.wait.until(
                # 等待直到出现元素
                EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
            # browser.page_source 获取网页源码
            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))

