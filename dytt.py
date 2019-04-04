from lxml import etree

import requests

BASE_DOMAIN='http://www.ygdy8.net'

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}


def get_detail_urls(url):
    response=requests.get(url,headers=headers)
    text=response.text  #默认使用ISO 给你解码
    # response.content.decode('gbk')
    #requests使用自己猜测的编码方式给你解码 ISO
    #在这里我们仅仅 是抓取url 所以使用 text 就可以了
    html=etree.HTML(text)
    detail_urls=html.xpath('//table[@class="tbspan"]//a/@href')
    detail_urls=list(map(lambda url:BASE_DOMAIN+url,detail_urls))
    #map()  每个元素重复拼接 url
    # def abc(url):
    #     return BASE_DOMAIN +url
    # for detail_url in detail_urls:
    #     detail_url=abc(detail_url)
    # print(detail_urls)



def parse_detail_page(url):
    movie={}
    response=requests.get(url,headers=headers)
    text=response.content.decode('gb2312')
    html=etree.HTML(text)
    title=html.xpath('')
    movie['title']=title
    zoomE=html.xpath('//div[@id="Zoom"]')[0]
    imgs=zoomE.xpath('.//img/@src')
    cover=imgs[0]
    screenshot=imgs[1]

    movie['cover']=cover
    movie['screenshot']=screenshot
    infos=zoomE.xpath('.//text()')
    def parse_info(info,rule):
        return info.replace(rule,'').strip()
    for info in infos:
        if info.startswith('◎年　　代'):
            info=parse_info(info,'◎年　　代')
        elif info.startswith('◎产　　地'):
            info=parse_info(info,'◎产　　地')

def spider():
    base_url='http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    movies=[]
    #拿到每一页,控制爬7个页面
    for X in range(1,8):
        url=base_url.format(X)
        #拿到每个页面的列表
        detail_urls=get_detail_urls(url)
        # for detail_url in detail_urls:
        #     movie=parse_detail_page(detail_url)
        #     movies.append(movie)



if __name__=='__main__':
    spider()