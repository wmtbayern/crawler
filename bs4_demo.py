from bs4 import BeautifulSoup

html_doc="""

<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49099&keywords=&tid=87&lid=2218">GY0-【国际业务部】Senior Web Developer（Hong Kong）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-03</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49100&keywords=&tid=87&lid=2218">25663-泛互联网业务架构师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-03</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49094&keywords=&tid=87&lid=2218">TME-腾讯音乐质量管理工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-03</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49096&keywords=&tid=87&lid=2218">29777-腾讯云金融行业后台开发高级工程师</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-03</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49097&keywords=&tid=87&lid=2218">29777-金融云区块链高级研发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-03</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49093&keywords=&tid=87&lid=2218">TEG14-社交业务图像处理开发工程师</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-03</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49086&keywords=&tid=87&lid=2218">TME-TME-QQ音乐创新平台iOS开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-03</td>
		    	</tr>
		    	    <tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49083&keywords=&tid=87&lid=2218">30630-腾讯广告数据分析师-销售支持（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-03</td>
		    	</tr>
		    		<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49078&keywords=&tid=87&lid=2218">18427-iOS移动客户端开发高级工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-03</td>
		    	</tr>
		    		<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49080&keywords=&tid=87&lid=2218">PCG14-推荐算法工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-03</td>
		    	</tr>
                </table>
  <p class="story">
   ...
  </p>
 </body>
</html>
"""
soup = BeautifulSoup(html_doc,'lxml')

# trs=soup.select('tr')
# for tr in trs:
#
#     print(type(tr))
#
# trs=soup.select('.l')
# for tr in trs:
#     print(tr)

#选择所需要的class    注意书写的格式
# trs=soup.select("tr[class='odd']")
# for i in trs:
#     print(i)

# trList=soup.select('tr')
# for a in trList:
#     print(a)

#只选择前面的三条数据
# trs=soup.select('.even',limit=3)
# for i in trs:
#     print(i)
trs=soup.select("tr[class='even']")
for i in trs:
    print(i)