import urllib.request

import requests
import re
#宽度优先遍历，也叫广度遍历，遍历完之后才进入下一级别的遍历
from bs4 import BeautifulSoup

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

#抓取起始页面的所有的链接，然后选择其中的一个链接，继续抓取这个链接中的所有页面

url='https://hr.tencent.com/position.php?keywords=python&lid=2218&tid=0'
req = urllib.request.Request(url, headers=headers)
data = urllib.request.urlopen(req).read()
soup = BeautifulSoup(data, 'lxml')
#总页数
a_list=soup.find('a',id="next").previous_sibling
print(a_list.text)
# for item in a_list:
#     a=item.select('a')[1].text
#     # print(a)