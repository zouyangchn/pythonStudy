import json

import requests

r = requests.get('https://www.baidu.com/' )  # 百度首页   ,timeout=0.005
print(r.status_code)
print(r.text)
print(r.content)
print(r.url)
print(r.headers)
print(r.headers['Cache-Control'])
print(r.cookies)
print(r.cookies['BDORZ'])


r = requests.get('https://www.baidu.com/s', params={'wd': 'python'})
print(r.url) # 实际请求的URL
print(r.encoding)

r = requests.get(
    'http://www.kuaidi100.com/query?type=yuantong&postid=11111111111')
print(r.json())


r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r.content)
