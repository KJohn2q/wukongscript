'''

从悟空问答 答题得红包模块 爬取问题

@author john

@date 2019.6.9


'''
import requests
import time,sys
import json,random
from src.functions import get_seconds, unique
from fake_useragent import UserAgent


def get_tags(db):

    tags = db.select_data()
    print(tags)
    exit()

    tags_list = []

    for tag in tags:
        tags_list.append(list(tag)[0])

    return tags_list

def resque(headersParmeters, user):

    now = get_seconds()
    inow = int(now)

    activity = 'answer_get_bonus'

    url = 'https://www.wukong.com/wenda/web/ugcinvited/question/brow/?concern_id=%d&t=%s&activity=%s' % (user, inow, activity)


    # url = 'https://www.wukong.com/wenda/web/ugcinvited/question/brow/?concern_id=%d&t=%s'%(user, inow)

    requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数

    # s = requests.session()
    # s.keep_alive = False  # 关闭多余连接

    response = requests.get(url, headers=headersParmeters)

    if response.status_code == 200:
        html = response.text
    else:
        html = u''
        print('[ERROR]', url, u'get此url返回的http状态码不是200')

    json_dic = json.loads(html)
    question_list = json_dic['wenda_invited_question_list']

    return question_list


def get_question(db, usercookie):

    user = 5798809181  # 推荐你答

    ua = UserAgent(verify_ssl=False)

    # headersParameters = {  # 发送HTTP请求时的HEAD信息，用于伪装为浏览器
    #         'Connection': 'close',
    #         'Accept': 'text/html, application/xhtml+xml, */*',
    #         'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    #         'Accept-Encoding': 'gzip, deflate',
    #         # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    #         'User-Agent': ua.random,
    #         'cookie': usercookie
    #     }
    headersParmeters = {
        'Host': 'www.wukong.com',
        # 'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;win64;x64;rv:67.0) Gecko / 20100101 Firefox / 67.0',
        'User-Agent': ua.random,
        'Accept':'application / json, text / javascript, * / *; q = 0.01',
        'Accept - Language': 'zh - CN, zh;q = 0.8, zh - TW; q = 0.7, zh - HK;q = 0.5, en - US;q = 0.3, en; q = 0.2',
        'Accept - Encoding': 'gzip, deflate, br',
        'wendacsrftoken': '67ced382d64234d473e539ab3da44706',
        'X - Requested - With': 'XMLHttpRequest',
        'Connection': 'close',
        'Referer': 'https://www.wukong.com/winner/',
        'X - Requested - With': 'XMLHttpRequest',
        'cookie': usercookie,
        'TE':'Trailers'
    }

    # 标签列表最后一个
    tags_default = [
        '5798809181',
        '6216118333234743809',
        '6216118350762740226',
        '6216118345905736194',
        '6215497897312520705',
        '6213187414555363841',
        '6215497897710979586',
        '6213185668705683969',
        '6213178317307120130'
    ]

    # tags_list = get_tags(db)
    #
    # tags_list.extend(tags_default)
    #
    # tags_nonrep = unique(tags_list)
    #
    # index = random.randint(0, len(tags_nonrep)-1)
    #
    # question_list = []
    #
    # while len(question_list) <= 0:
    #     index = random.randint(0, len(tags_nonrep)-1)
    #     time.sleep(3)
    #     question_list = resque(headersParmeters, int(tags_nonrep[index]))

    question_list = resque(headersParmeters, user)

    return question_list




