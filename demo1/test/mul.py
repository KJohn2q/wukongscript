from selenium import webdriver
import sys,time
import configparser
sys.path.append("..")
from src.functions import format_usercookie

cp = configparser.RawConfigParser()
cp.read("../program.cfg")

usercookie1 = cp.get('program_cfg', "usercookie1")
usercookie2 = cp.get('program_cfg', "usercookie2")

profile_path1 = r'C:\Users\zlmnh\AppData\Roaming\Mozilla\Firefox\Profiles\2ymud5qu.default'
profile_path2 = r'C:\Users\zlmnh\AppData\Roaming\Mozilla\Firefox\Profiles\jx4bv6f8.john'

driver_path = 'D:\program\driver\geckodriver.exe'

profile1 = webdriver.FirefoxProfile(profile_path1)
driver1 = webdriver.Firefox(firefox_profile=profile1, executable_path=driver_path)
driver1.maximize_window()
driver1.get('https://www.wukong.com/')

driver1.implicitly_wait(30)

userinfo1 = format_usercookie(usercookie1)

for key, val in userinfo1.items():
    driver1.add_cookie({'name': str(key), 'value': str(val)})


profile2 = webdriver.FirefoxProfile(profile_path2)
driver2 = webdriver.Firefox(firefox_profile=profile2, executable_path=driver_path)
driver2.maximize_window()
driver2.get('https://www.wukong.com/')

userinfo2 = format_usercookie(usercookie2)

driver2.implicitly_wait(30)

for key, val in userinfo2.items():
    driver2.add_cookie({'name': str(key), 'value': str(val)})