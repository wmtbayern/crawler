import urllib.request

import pymysql
import requests
import re

from bs4 import BeautifulSoup

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

#如果一个页面中还有url 要一级一级的深入抓取里面的内容
#这就是模仿百度蜘蛛深度抓取原理    采用递归算法

#获取整个页面的内容，   然后获取页面 url 的子列表，
#然后用正则匹配出 a 标签中的  href

#获取网页内容

# def get_content(url):
#     req = urllib.request.Request(url, headers=headers)
#
#     data = urllib.request.urlopen(req).read()
#     soup = BeautifulSoup(data, 'lxml')
#     data = soup.find_all('table', class_="tablelist")
#     for line in data[0].find_all('tr', class_=["even", "odd"]):
#         for data in line.find_all('td'):
#             print( data.string)


#获取页码的a标签列表

# def get_son_url(url):
# req = urllib.request.Request(url, headers=headers)
#
# data = urllib.request.urlopen(req).read()
# soup = BeautifulSoup(data, 'lxml')
# a_list = soup.find_all('a', class_="pagenav")
# print(a_list)
# href_list = []
# for i in a_list:
#     print(i['href'])
    # href_list.append(soup.i['href'])
    # print(href_list)
# get_son_url(url='https://hr.tencent.com/position.php?keywords=python&lid=2218&tid=0')
#层层调用
# def deep_crawer(url):
#     if deep_dict[url]>3:
#         return
#     print('\t'*deep_dict[url],url,'当前层级：%d' % deep_dict[url])
#     son_list=get_son_url(url)
#     for sonurl in son_list:
#         #http 开头的数据才是我们要的
#         if sonurl.startswith('http'):
#             # 去重
#             if sonurl not in deep_dict:
#
#                 deep_dict[sonurl]=deep_dict[url]+1
#
#                 deep_crawer(sonurl)
# #
def getPageNum(url):
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,'lxml')
    #拿到总页数
    pageNum=soup.select('.pagenav a')[-2].text
    return  int(pageNum)
def getJobList(totalPage,url):
    qq_Job_list=[]
    for i in range(totalPage):
        url=url + '&start=%d' % (i*10)
        response=requests.get(url,headers=headers)
        soup=BeautifulSoup(response.text,'lxml')
        #注意url 的拼接,看详情页的url 比 a标签里面的多了一段
        job_list=soup.select('.tablelist tr')[1:-1]
        for job in job_list:
            job_url=job.td.a['href']
            #拿到 url
            job_url='https://hr.tencent.com/'+job_url
            getJobInfo(job_url,qq_Job_list)

def getJobInfo(url,qq_Job_list):
    qq_job_list=[]
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    # 获取工作的详细信息
    job_name=soup.select('#sharetitle')[0].text
    job_address=soup.select('.bottomline td')[0].span.next_sibling
    job_type=soup.select('.bottomline td')[1].span.next_sibling
    job_num=soup.select('.bottomline td')[2].span.next_sibling
    job_num=re.findall(r'(\d+).*?',job_num)[0]
    job_duty = soup.select('.squareli')[0].text
    job_require = soup.select('.squareli')[1].text
    job_dict = {
        "name": job_name,
        "address": job_address,
        "type": job_type,
        "num": int(job_num),
        "duty": job_duty,
        "require": job_require

    }
    qq_job_list.append(job_dict)
    save(qq_job_list)


def save(qq_job_list):
    db=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='qq_hr',charset='utf8')
    cursor=db.cursor()

    for job in qq_job_list:
        name = job['name']
        address = job['address']
        type = job['type']
        num = job['num']
        duty = job['duty']
        require = job['require']
    sql = """insert into job(name,address,type,num,duty,reqire1) value('%s','%s','%s','%d','%s','%s')"""% (
    name, address, type, num, duty, require)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
if __name__=='__main__':
    startUrl='https://hr.tencent.com/position.php?keywords=python&lid=2218&tid=0'
    #将Url作为key  存放url   value 存放层级 1 2  3
    #先获取总页数
    totalPage=getPageNum(startUrl)
    #再获取每一页的岗位信息   里面调用详情函数和保存函数了
    getJobList(totalPage, startUrl)
    #再获取每个岗位的详情

