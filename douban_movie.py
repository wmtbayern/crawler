import json
import os
import urllib.request

import requests
from lxml import etree
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url='https://movie.douban.com/cinema/nowplaying/shenzhen/'
response=requests.get(url,headers=headers)

text=response.text  #解码后的字符串,str类型  content  是字节

html=etree.HTML(text)

ul=html.xpath('//ul[@class="lists"]')[0]   #返回的是列表
lis=ul.xpath('./li')
dir = 'dir'
os.chdir(dir)
movies=[]
for li in lis:
    title=li.xpath('@data-title')[0]
    score=li.xpath('@data-score')[0]
    star=li.xpath('@data-star')[0]
    duration=li.xpath('@data-duration')[0]
    region=li.xpath('@data-region')[0]
    director=li.xpath('@data-director')[0]
    actors=li.xpath('@data-actors')[0]
    thumbnail=li.xpath('.//img/@src')[0]
    movie={
        'title':title,
        'score':score,
        'star':star,
        'duration':duration,
        'region':region,
        'director':director,
        'actors':actors,
        'thumbnail':thumbnail,
    }

    movies.append(movie)
    # 要下载文件都用 urlretrieve
    urllib.request.urlretrieve(movie['thumbnail'], movie['title'] + 'jpg')


print(movies)
