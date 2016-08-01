#! /usr/local/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import re

qrSourceUrl = 'https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_=1470017530044'
qrSourceReq = request.urlopen(qrSourceUrl).read().decode('utf-8')
qrSource = qrSourceReq.split('"')
qrSource = qrSource[1]

qrUrl = 'http://login.wx.qq.com/qrcode/' + qrSource
qrReq = request.urlopen(qrUrl).read()

filePath = '/Users/daryl/Desktop/wxqr.jpg'
f = open(filePath, 'wb+')
f.write(qrReq)

print('请打开图片' + filePath + '，然后使用手机微信扫描')

loginUrl = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=' + qrSource + '&tip=1&r=-1145234545&_=1470024049411'
login = request.urlopen(loginUrl).read().decode('utf-8')

while not ('window.code=200;' in login) :
    loginUrl = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=' + qrSource + '&tip=1&r=-1145234545&_=1470024049411'
    login = request.urlopen(loginUrl).read().decode('utf-8')

uri = login.split('"')
uri = uri[1]
print(uri)
success = request.urlopen(uri).read();
print(success)