from selenium import webdriver
import sys
chromeOptions = webdriver.ChromeOptions()

# 设置代理
chromeOptions.add_argument("--proxy-server=http://202.20.16.82:10152")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
driver = webdriver.Chrome(chrome_options=chromeOptions)

# 查看本机ip，查看代理是否起作用
driver.get("http://httpbin.org/ip")
sys.exit(0)

driver.get('https://www.wukong.com/')

driver.add_cookie({'name':'_ga','value':'GA1.2.1326949150.1560046550'})
driver.add_cookie({'name':'_gid','value':'GA1.2.870718405.1560246319'})
driver.add_cookie({'name':'cookie_tt_page','value':'ba6eeb6e889b582a82b76c3ffdddcfa2'})
driver.add_cookie({'name':'s_v_web_id','value':'7da744a3c0ab7fb80f1679c6c126130a'})
driver.add_cookie({'name':'sessionid','value':'3e424f9743f8ab7cd6c6a98ff3f44a02'})
driver.add_cookie({'name':'sessionid','value':'3e424f9743f8ab7cd6c6a98ff3f44a02'})
driver.add_cookie({'name':'tt_webid','value':'6700348869827380744'})
driver.add_cookie({'name':'tt_webid','value':'6700348869827380744'})
driver.add_cookie({'name':'uid_tt','value':'e8a4291ca2fa97f8234cc7678deb25648a4d752d633b2fb76f50a1b200527839'})
driver.add_cookie({'name':'uid_tt','value':'e8a4291ca2fa97f8234cc7678deb25648a4d752d633b2fb76f50a1b200527839'})
driver.add_cookie({'name':'wenda_login_status','value':'1'})
driver.add_cookie({'name':'wendacsrftoken','value':'373040cb6c48a8622dbecb873ca0d379'})
