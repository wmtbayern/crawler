
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup

headers = {
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding': '',   #编码格式，为空就可以，要不然解码会出错
# 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
# 'Cache-Control': 'max-age=0',
# 'Connection': 'keep-alive',
# 'Cookie': 'PHPSESSID=2gr6022ot3vqqc3eb0qurkmbq5; pgv_pvi=7278042112; pgv_si=s82940928',
# 'Host': 'hr.tencent.com',
# 'Upgrade-Insecure-Requests': '1',
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"

}

url='https://hr.tencent.com/position_detail.php?id=49099&keywords=python&tid=0&lid=2218'


#用到的是 bs4
#请求头构造
req = urllib.request.Request(url, headers=headers)

# data = urllib.request.urlopen(req).read().decode()  解码反而会拿不到所有的页面内容
data = urllib.request.urlopen(req).read()         #不解码就是二进制的内容
                            #解析器
soup = BeautifulSoup(data, 'lxml')
tencent={}
tr_list=soup.find_all('tr',class_="bottomline")   #find_all 返回的是列表的形式
# li_list=soup.find_all('ul')
tencent['title']=soup.select('td',id='sharetitle')[0].text

for tr in tr_list:
     tencent['addr']=tr.select('td')[0].text
     tencent['category']=tr.select('td')[1].text
     tencent['num']=tr.select('td')[2].text


tencent['job']=soup.find_all('td',attrs={'class':'l2','colspan':'3'})[1].text
tencent['jobreq']=soup.find_all('td',attrs={'class':'l2','colspan':'3'})[2].text
# # print(tbody_list)

print(tencent)