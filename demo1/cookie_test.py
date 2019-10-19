from selenium import webdriver
import requests
import json
import time

def get_cookies():
    browser = webdriver.Chrome(executable_path="C:\program_john\webdriver\chromedriver.exe")
    browser.get("https://www.wukong.com/")# xxx 改为qq账号
    input("请登陆后按Enter")
    cookie={}
    for i in browser.get_cookies():
        cookie[i["name"]] = i["value"]
    with open("cookies.txt","w") as f:
        f.write(json.dumps(cookie))

if __name__ == "__main__":
    with open("cookies.txt","r") as f:
        cookie_str = f.read()
    cookie_json = json.loads(cookie_str)
    co_str = ''
    for key,val in cookie_json.items():
        temp_str = key+'='+val+';'
        co_str += temp_str
    print(co_str)