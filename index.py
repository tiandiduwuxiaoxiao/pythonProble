# encoding: utf-8
"""
@version: Python3.6.4
@author: Tim 
@contact: lizeyunqz@163.com
@software: PyCharm
@file: index.py
@time: 2018/2/4 20:47
"""
from urllib import request
from bs4 import BeautifulSoup
response = request.urlopen('http://www.baidu.com')
soup = BeautifulSoup(response.read(), 'html.parser')
print(soup.title)