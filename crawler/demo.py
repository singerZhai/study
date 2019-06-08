# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-06-02 15:38
# @File    : demo.py
# @Software: PyCharm
import random
from urllib import request, parse
import ssl

import requests

import config

ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": random.choice(config.agents),
    # "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

params = parse.urlencode(
    [
        ("username", "admin"),
        ("password", "123")
    ]
)

localhost = "http://127.0.0.1:8000/login/"
demo_url = 'http://httpbin.org/get'
baidu_url = "https://www.baidu.com"
# req = request.Request(url=localhost, headers=headers, data=params)
# # req.add_header("User-Agent", random.choice(config.agents))
# with request.urlopen(req) as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print("\n\n\nData:", data.decode('utf-8'))


import telnetlib

print('------------------------connect---------------------------')
# 连接Telnet服务器
try:
    tn = telnetlib.Telnet('183.129.207.80', port='14512', timeout=20)
except Exception:
    print('该代理IP  无效')
else:
    print('该代理IP  有效')

print('-------------------------end----------------------------')

# proxies = {
#     'http': '47.94.200.124:3128',
#     'https': '47.94.200.124:3128'
# }
#
# r = requests.post("http://127.0.0.1:8000/login/", data=None, proxies=proxies)
# print(r.status_code)
# print(r.text)