# encoding: utf-8
"""
@version: Python3.6.4
@author: Tim 
@contact: lizeyunqz@163.com
@software: PyCharm
@file: problem1.py
@time: 2018/2/4 21:13
"""
from PIL import Image, ImageFont, ImageDraw, ImageColor


def problem1():
    img = Image.open('we_chat.jpg', 'r')
    # 创建一个Draw对象
    draw = ImageDraw.Draw(img)
    # 创建一个 Font
    my_font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = ImageColor.colormap.get('red')
    width, height = img.size
    draw.text((width - 30, 0), '1', font=my_font, fill=fillcolor)
    img.save('result.jpg', 'jpeg')
    return 0


problem1()
