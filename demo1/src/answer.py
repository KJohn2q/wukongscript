'''

模拟请求单个问题页面

答题

@author john

@date 2019.6.9

'''
from telnetlib import EC

from selenium import webdriver
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.know import crawler
from selenium.common.exceptions import NoSuchElementException
import time

def isElementPresent(driver,by,value):
    try:
        # element = driver.find_element_by_class_name('write-content-submit')
        if by == 'id':
            element = driver.find_element_by_id(value)
        elif by == 'class_name':
            element = driver.find_element_by_class_name(value)
    except NoSuchElementException as e:
        return False
    except:
        return False
    else:
        return True


def answer(url, solution, driver, userinfo):

    #本地开发首页地址
    driver.get(url)

    # 红包元素不存在
    if isElementPresent(driver, 'class_name','title-suffix') is False:
        print('没有红包检测')
        return 1

    # driver_cookie = driver.get_cookies()

    # for key,val in userinfo.items():
    #     driver.add_cookie({'name':str(key),'value':str(val)})
    #
    # driver.refresh()

    try:
        driver.find_element_by_id('write-ueditor-inline').send_keys(solution)
        driver.find_element_by_class_name('write-content-submit').click()
    except:
        driver.refresh()

    if isElementPresent(driver, 'id', 'wukung_verify_code') is True:
        time.sleep(60)