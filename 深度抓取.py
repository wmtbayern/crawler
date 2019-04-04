import requests
import re

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

#如果一个页面中还有url 要一级一级的深入抓取里面的内容
#这就是模仿百度蜘蛛深度抓取原理    采用递归算法

#获取整个页面的内容，   然后获取页面 url 的子列表，
#然后用正则匹配出 a 标签中的  href

#获取网页内容
def get_content(url):
    try:
        res = requests.get(url, headers=headers)
        return res.text
    except:
        return ''
#获取子url列表
def get_son_url(url):
    contents=get_content(url)   #页面内容

    href_re='<a.*?href="(.*?)".*?>'   #匹配想要的字符串
    href_list=re.findall(href_re,contents,re.S)       #re.S忽略空格
    return href_list  #写成函数的形式都要有返回值

#层层调用
def deep_crawer(url):
    if deep_dict[url]>3:
        return
    print('\t'*deep_dict[url],url,'当前层级：%d' % deep_dict[url])
    son_list=get_son_url(url)
    for sonurl in son_list:
        #http 开头的数据才是我们要的
        if sonurl.startswith('http'):
            # 去重
            if sonurl not in deep_dict:

                deep_dict[sonurl]=deep_dict[url]+1

                deep_crawer(sonurl)

if __name__=='__main__':
    url='http://www.baidu.com/s?wd=岛国教育片'
    #将Url作为key  存放url   value 存放层级 1 2  3
    #开始爬取
    deep_dict={}  #这里面存放所有的列表
    #默认制定等级为1
    deep_dict[url]=1   #不会在第一级爬取数据了，第三级爬取完了会返回到第二级
    #执行函数
    deep_crawer(url)