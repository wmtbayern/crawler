import requests
from bs4 import BeautifulSoup

import re
import urllib.request

#准备请求头,必须的  http://tools.jb51.net/table/useragent  找到模拟的请求头
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
# 步骤:
#打开网页的源代码 看源代码中的链接 找到我们要的数据的请求url,在url地址栏也能看到

#获取前程无忧的接口

url = "https://search.51job.com/list/040000%252C010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
#创建请求对象,
req=urllib.request.Request(url,headers=headers)
#获取响应体
response=urllib.request.urlopen(req)

#获取数据才是工作的开始,后续数据的处理才是重点

html=response.read().decode('gbk')
#查看源代码查看所要的数据所在的位置



soup=BeautifulSoup(html,'lxml')

jobnum=soup.select('.rt')[0].text
print(jobnum)



# strs=coms.findall(html) #列表的形式
# strs=coms.findall(html)[0]  #获取第一个元素
# print(strs)
#贪婪模式  非贪婪模式
#贪婪模式加上 ？ 变成了非贪婪模式
#取出纯数字
num_re = '.*?(\d+).*'
num = re.findall(num_re,jobnum)
# print(num)
print(int(num[0]))

