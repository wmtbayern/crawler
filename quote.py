import requests
from bs4 import BeautifulSoup


headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url = "http://quote.stockstar.com/fund/stock.shtml"

response=requests.get(url,headers=headers)

soup=BeautifulSoup(response.content.decode('gb2312'),'lxml')

#重点是选择标签，选到正确的标签
tr_list=soup.select('#datalist > tr')

for tr in tr_list:   #拿到每一个tr 标签，每个tr 下面有多个  td 用下标获取
    # id=tr.select('td')[0].a.text  两种写法都可以
    id=tr.select('td')[0].text
    name=tr.select('td')[1].text
    value=tr.select('td')[2].text
    print(id,name,value)

