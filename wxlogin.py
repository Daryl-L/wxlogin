#! /usr/local/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import re
from http import cookiejar

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

redirect = request.urlopen(loginUrl).read().decode('utf-8')
rea = re.findall(r'^.*ticket=(.*?)&.*$', redirect, re.S);
ticket = rea[0]

uri = login.split('"')
uri = uri[1]

cookie = cookiejar.CookieJar();
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
success = opener.open(uri)

cryptUrl = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=' + ticket + '&uuid=' + qrSource + '&lang=zh_CN&scan=1470809455&fun=new&version=v2&lang=zh_CN'
crypt = request.urlopen(cryptUrl).read().decode('utf-8')

info = re.findall(r'^.*<skey>(.*)</skey><wxsid>(.*)</wxsid><wxuin>(.*)</wxuin><pass_ticket>(.*)</pass_ticket>.*$'， crypt)
skey = info[0]
wxsid = info[1]
wxuin = info[2]
passTicket = info[3]