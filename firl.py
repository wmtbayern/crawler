import re

import requests


headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}


def get_content(url):
    try:
        res = requests.get(url, headers=headers)
        return res.text
    except:
        return ''

def get_son_url(url):
    contents=get_content(url)   #页面内容
    t='mfsdskjfbnslkfjsvmsknvsknvks'
    href_re='ms.*?'   #想要的字符串
    href_list=re.findall(href_re,t,re.S)
    return href_list  #写成函数的形式都要有返回值

url='http://www.baidu.com/s?wd=岛国教育片'

a=get_son_url(url)

print(a)