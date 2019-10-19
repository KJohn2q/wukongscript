#图像处理标准库
from PIL import Image
#web测试
from selenium import webdriver
#鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
#等待时间 产生随机数
import time,random

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
driver.maximize_window()

