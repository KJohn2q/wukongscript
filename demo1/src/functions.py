import time
import datetime

"""
    获取精确毫秒数时间戳、   
"""
def get_seconds():
    datetime_object = datetime.datetime.now()
    now_timetuple = datetime_object.timetuple()
    now_second = time.mktime(now_timetuple)  # 返回当前时间的秒数
    mow_millisecond = now_second * 1000 + datetime_object.microsecond / 1000  # 毫秒
    return mow_millisecond

'''
    
    格式化cookie
    cookie字符串转字典对象
'''
def format_usercookie(str):
    # str = 'tt_webid=6700348869827380744; tt_webid=6700348869827380744; answer_enterFrom=; cookie_tt_page=70a7fd4ac4224b35f54cf51a460377ee; _ga=GA1.2.1326949150.1560046550; _gid=GA1.2.1491219071.1560046550; s_v_web_id=86b0e8e1533d4ea43da96c7775860de4; sessionid=8dbcccba17eeec708c508c8dea02ab96; sessionid=8dbcccba17eeec708c508c8dea02ab96; uid_tt=8cc88a2e32df5448b6da94ee01306fa29f72ffccd1c08c4033b58033ff132ee8; uid_tt=8cc88a2e32df5448b6da94ee01306fa29f72ffccd1c08c4033b58033ff132ee8; wenda_login_status=1; wendacsrftoken=0db8c93dd08289843702b4e344d3a5ea; answer_finalFrom=; _gat=1'

    arr = str.split(';')
    userinfo = {}  # 用户信息cookie数组

    for item in arr:
        item_str = item.replace(' ','')
        arr2 = item_str.split('=')
        userinfo[arr2[0]] = arr2[1]
    return userinfo

"""
    数组去重
"""
def unique(old_list):
    newList = []
    for x in old_list:
        if x not in newList :
            newList.append(x)
    return newList