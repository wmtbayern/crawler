import requests


headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}


# 首页登陆的Url
url='http://www.xbiquge.la/login.php'

data={

}

sessions=requests.session()

response=sessions.post(url,headers=headers)

# 登陆后，查看个人中心
url1=''

sessions=requests.session()

response1=sessions.post(url1,headers=headers)

print(response1.text)