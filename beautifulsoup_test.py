
#beautifulsoup   bs4   方便查找内容的的python库

from bs4 import BeautifulSoup

fp = open('index.html',encoding='utf-8')
#实例化对象    ‘lxml’  解析器
soup=BeautifulSoup(fp,'lxml')
#格式化代码
# print(soup.prettify())

#获取标签的子标签
print(soup.head.title)

#返回标签名称
print(soup.head.title.name)

#获取属性
# print(soup.p.attrs)  第一个p标签属性
print(soup.a.attrs)
#查看某个属性
print(soup.a.attrs['class'])

print(soup.a.attrs.get('href'))
#拿到属性的值
print(soup.a['href'])

#拿到标签里面的内容
print(soup.p.string)   #只有一行的才能获取到

#获取节点内部的所有文本内容
print(soup.p.text)
print(soup.p.b.get_text())

#兄弟节点  同一级别的标签才可以用
#下一个节点
print(soup.a.next_sibling)   #要注意换行和空格也都是文本节点 有可能获取到的是这样的标签
print(soup.a.next_sibling.next_sibling)  #可以连用

#上一个文本节点
print(soup.a.previous_sibling)

#find_all
#获取所有的a标签
aa=soup.find_all('a')
for a in aa:
    print(a)

#获取第二个a标签
aas=soup.find_all('a',limit=2)[1]
print(aas)
print('####'*20)
#获取所有的class为sister的a标签   html 中 class=sister
adf=soup.find_all('a',attrs={'class':'sister'})

for i in adf:
    print(i)
#获取id class 都为某个值的标签

List =  soup.find_all('a',id='test',class_='test')  # 两个属性的标签 注意class_的写法
for item in List:
    print(item)
print('fff'*10)



#获取所有a 标签的href属性
aList=soup.find_all('a')
for a in aList:
    href=a.attrs['href']
    print(href)


#获取所有的职位的信息，纯文本格式
trs=soup.find_all('tr')[1:]
tests=[]
for tr in trs:
    test={}
    tds=tr.find_all('td')
    title=tds[0].string
    category=tds[1].string
    nums=tds[2].string
    city=tds[3].string
    pubtime=tds[4].string
    test['title']=title
    test['category']=category
    test['nums']=nums
    test['city']=city
    test['pubtime']=pubtime
    tests.append(test)
    print(tests)
