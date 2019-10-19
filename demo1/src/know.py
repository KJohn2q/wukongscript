'''
查询百度知道搜索结果

@author john

@date  2019.6.9
'''

import re
import requests
import traceback
from urllib.parse import quote
import sys
import importlib
import string
import json
from lxml import etree
from bs4 import BeautifulSoup

importlib.reload(sys)

class crawler:
    '''爬百度搜索结果的爬虫'''
    url = u''
    urls = []
    o_urls = []
    targetUrls = []
    html = ''
    headersParameters = {    #发送HTTP请求时的HEAD信息，用于伪装为浏览器
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    results = ''

    def __init__(self, keyword):
        self.url = u'https://www.baidu.com/baidu?wd='+quote(keyword)+'&tn=monline_dg&ie=utf-8'

    def set_current_url(self, url):
        '''设置当前url'''
        self.url = url

    def get_html(self):
        '''爬取当前url所指页面的内容，保存到html中'''
        r = requests.get(self.url , headers=self.headersParameters)
        if r.status_code==200:
            self.html = r.text
        else:
            self.html = u''
            print('[ERROR]',self.url,u'get此url返回的http状态码不是200')

    def get_urls(self):
        '''从当前html中解析出搜索结果的url，保存到o_urls'''
        o_urls = re.findall('href\=\"(http\:\/\/www\.baidu\.com\/link\?url\=.*?)\" class\=\"c\-showurl\"', self.html)
        o_urls = list(set(o_urls))  #去重
        self.o_urls = o_urls
        #取下一页地址
        next = re.findall(' href\=\"(\/s\?wd\=[\w\d\%\&\=\_\-]*?)\" class\=\"n\"', self.html)
        if len(next) > 0:
            self.next_page_url = 'https://www.baidu.com'+next[-1]
        else:
            self.next_page_url = ''

    def get_real(self, o_url):
        '''获取重定向url指向的网址'''
        r = requests.get(o_url, allow_redirects = False)    #禁止自动跳转
        if r.status_code == 302:
            try:
                return r.headers['location']    #返回指向的地址
            except:
                pass
        return o_url    #返回源地址

    def transformation(self):
        '''读取当前o_urls中的链接重定向的网址，并保存到urls中'''
        self.urls = []
        for o_url in self.o_urls:
            self.urls.append(self.get_real(o_url))

    def match_urls(self,urls):
        self.targetUrls = []
        for url in urls:
            if re.match(r"(.+)zhidao(.+)", url) != None:
                self.targetUrls.append(url)

    def print_urls(self):
        '''输出当前urls中的url'''
        for url in self.urls:
            print(url)

    def get_results(self):
        if(self.targetUrls.__len__() != 0):
            targeturl = self.targetUrls[0]
            response = requests.get(targeturl, headers=self.headersParameters)
            response.encoding = "gb2312"
            r_text = response.text
            soup = BeautifulSoup(r_text, 'lxml')
            sel_text = soup.select(".wgt-best .answer .content .best-text")

            if len(sel_text) != 0:
                item = sel_text[0]
                str = item.get_text()
                str_new = str.replace('展开全部','').strip()
                self.results = str_new  # 去掉空行

    def run(self):
        self.get_html()
        self.get_urls()
        self.transformation()
        self.match_urls(self.urls)  # 这一步出错了
        # print(self.targetUrls)
        self.get_results()
        return self.results




