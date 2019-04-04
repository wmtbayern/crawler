import requests


headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}


# 首页登陆的Url
url=''


data={}


sessions=requests.session()

response=sessions.post(url,data=data,headers=headers)


print(response.text.decode())
# 个人中心的url
url=''
