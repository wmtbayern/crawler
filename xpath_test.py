from lxml import etree



def parse_lagou_file():
    parser=etree.HTMLParser(encoding='utf-8')
    html=etree.parse('index.html',parser=parser)   #转成html
    print(etree.tostring(html,encoding='utf-8').decode('utf-8'))

# if __name__=='__main__':
    # parse_lagou_file()


parser=etree.HTMLParser(encoding='utf-8')

html = etree.parse('index.html', parser=parser)
#获取所有的  tr 标签
# xpath返回的是所有的列表,
#
# trs=html.xpath('//tr')
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))
#获取第二个 tr
# tr=html.xpath('//tr[2]')[0]
#
# print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# trs=html.xpath('//tr[@class="even"]')
# for  tr in trs :
#     pass

#获取所有的a标签的href属性,获取属性的值
# aList=html.xpath('//a/@href')
# for a in aList:
#      print(a)

#获取所有职位的信息   position 是从一开始,而不是0 开始
trs=html.xpath('//tr[position()>1]')
#tr标签下面再获取子孙元素
positions=[]
for tr in trs:
    href=tr.xpath('.//a/@href')[0]
    fullurl='https://hr.tencent.com/'+href
    title=tr.xpath('./td[1]//text()')[0]
    category=tr.xpath('./td[2]//text()')[0]
    nums=tr.xpath('./td[3]//text()')[0]
    address=tr.xpath('./td[4]//text()')[0]
    position={
        'url':fullurl,
        'title':title,
        'category':category,
        'nums':nums,
        'address':address,
    }

    positions.append(position)
print(positions)