'''

脚本主程序

@author john

@date 2019.6.9


'''

import sys
from builtins import len, isinstance, str

from src.sqldump import Sqldump
from src.question import get_question
from src.know import crawler
from src.answer import answer
from selenium import webdriver
from src.functions import format_usercookie, unique
import configparser
import time

def get_driver(driver_path):

    try:
        # driver = webdriver.Chrome(driver_path)
        driver = webdriver.Firefox(executable_path=driver_path)
        driver.maximize_window()

        return driver
    except:
        print("您输入的路径不正确")
        sys.exit(0)

def set_drivercookie(driver, userinfo):

    driver.get('https://www.wukong.com')

    for key, val in userinfo.items():
        driver.add_cookie({'name': str(key), 'value': str(val)})

def add_tags(db, question_list):
    tags_list = []

    for ques in question_list:
        concern_tags = ques['concern_tags']

        tags_list.extend(concern_tags)

    tags_nonrep = unique(tags_list)

    return db.insert_data(tags_nonrep)


extra_tag = 'answer_get_bonus'
answer_base_url = 'https://www.wukong.com/question/{}/?extra_tag=answer_get_bonus'
# answer_base_url = 'https://www.wukong.com/question/{}/?extra_tag=from_wenda_list'

i = 0

cp = configparser.RawConfigParser()
cp.read("program.ini")

driver_path = cp.get('program_cfg', "driver_path")
usercookie = cp.get('program_cfg', "usercookie")

answer_url = ''
solution = ''

db = Sqldump()

if isinstance(usercookie,str):
    question_list = get_question(db,usercookie)
    userinfo = format_usercookie(usercookie)

    driver = get_driver(driver_path)

    set_drivercookie(driver, userinfo)

    # if len(question_list)<=0:
    #     print("您还没有获得回答问题的资格")
    #     sys.exit(0)

    while 1 == 1:
        #  如果问题列表不为空，则执行后续操作，如果为空，则直接重新获取问题
        if i <= len(question_list) - 1:
            for value in question_list:

                if i == len(question_list) - 1:
                    i = 0
                    time.sleep(3)
                    add_tags(db, question_list)
                    question_list = get_question(db,usercookie)
                    break

                # 如果有人回答过，就跳过
                if value['nice_ans_count'] > 0:
                    i += 1
                    continue
                qid = value['qid']  # 题的编号
                title = value['title']  # 题的题面
                answer_url = answer_base_url.format(qid)  # 格式化url

                # 从百度知道获得答案
                cra = crawler(title)
                solution = cra.run()
                if solution.strip() != '':
                    status = answer(answer_url,solution, driver, userinfo)
                    if status == 1:
                        i += 1
                        continue
                    else:
                        i += 1
                        time.sleep(3)
                        continue
                else:
                    i += 1
                    continue
                # 如果问题全部遍历完，就跳出问题循环  重新获取题目

        else:  # 最后一道题答完
            i = 0
            print(1)
            question_list = get_question(db,usercookie)

else:
    sys.exit()