import configparser
import json
import sys

from src.functions import unique
import requests
import pymysql
from src.sqldump import Sqldump

from src.functions import get_seconds

cp = configparser.RawConfigParser()
cp.read("program.ini")

driver_path = cp.get('program_cfg', "driver_path")
usercookie = cp.get('program_cfg', "usercookie")

now = get_seconds()
inow = int(now)

user = 5798809181

activity = 'answer_get_bonus'

url = 'https://www.wukong.com/wenda/web/ugcinvited/question/brow/?concern_id=%d&t=%s&activity=%s' % (user, inow, activity)

headersParameters = {  # 发送HTTP请求时的HEAD信息，用于伪装为浏览器
            'Connection': 'close',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
            'cookie': usercookie
        }

response = requests.get(url, headers = headersParameters)

if response.status_code == 200:
    html = response.text
else:
    html = u''
    print('[ERROR]', url, u'get此url返回的http状态码不是200')

json_dic = json.loads(html)
question_list = json_dic['wenda_invited_question_list']


db = Sqldump()
tags = db.select_data()

tags_list = []

for tag in tags:
    tags_list.append(int(list(tag)[0]))

print(tags_list)

db.close_conn()

