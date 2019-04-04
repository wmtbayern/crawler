import requests

from  bs4 import BeautifulSoup
ALL_DATA=[]

def parse_page(urls):
    headers = {
        "User-Agent": "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }
    response=requests.get(urls,headers=headers)
    text=response.content.decode('utf-8')
    soup=BeautifulSoup(text,'html5lib')
    conMidtab=soup.find('div',class_='conMidtab')
    tables=conMidtab.find_all('table')
    for table in tables:
        trs=table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds=tr.find_all('td')
            city_td=tds[0]  #获取城市列表数据
            if index==0:
                city_td=tds[1]
            city=list(city_td.stripped_strings)[0]
            temp_ed=tds[-2]
            temp_max=list(temp_ed.stripped_strings)[0]
            ALL_DATA.append({'city':city,'max_temp':int(temp_max)})
            print({'city':city,'max_temp':int(temp_max)})

def main(urls):
    urls =[
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml',
    ]
    for url in urls:
        parse_page(url)
    ALL_DATA.sort(key=lambda data:data['max_temp'])
    data=ALL_DATA[0:20]
    cities = list(map(lambda x: x['city'], data))
    max_temp = list(map(lambda x: x['max_temp'], data))


if __name__=='__main__':

    # main()
    parse_page(urls='http://www.weather.com.cn/textFC/hb.shtml')