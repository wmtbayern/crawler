import requests
import re
#宽度优先遍历，也叫广度遍历，遍历完之后才进入下一级别的遍历


headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

#抓取起始页面的所有的链接，然后选择其中的一个链接，继续抓取这个链接中的所有页面


def get_content(url):
    try:
        res = requests.get(url, headers=headers)
        return res.text
    except:
        return ''

def get_son_url(url):
    contents=get_content(url)   #页面内容

    href_re='<a.*?href="(.*?)".*?>'   #想要的字符串的人
    href_list=re.findall(href_re,contents,re.S)
    return href_list  #写成函数的形式都要有返回值




def width_crawer(start_url):
    #队列模拟
    #入队列 append() 出队列pop()
    url_quene = []
    url_quene.append(start_url)
    while len(url_quene) > 0:
        url = url_quene.pop(0)
        print("\t" * deep_dict[url], "当前层级:%d" % deep_dict[url])
        if deep_dict[url] <= 2:
            #获取子url列表
            sonurl_list = get_son_url(url)
            for sonurl in sonurl_list:
                #过滤有效的链接
                if sonurl.startswith('http'):
                    #去重 为了不重复爬取
                    if sonurl not in deep_dict:
                        deep_dict[sonurl] = deep_dict[url]+1
                        url_quene.append(sonurl)

if __name__=='__main__':
    url='http://www.baidu.com/s?wd=岛国教育片'
    #将Url作为key  存放url   value 存放层级 1 2  3
    deep_dict={}  #这里面存放所有的列表
    #默认制定等级为1
    deep_dict[url]=1   #不会在第一级爬取数据，第三级爬取完了会返回到第二级
    #执行函数
    width_crawer(url)

