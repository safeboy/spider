#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from urllib2 import urlopen, quote
import os,sys
#从指定URL地址获取页面文件
def get_page(url):
    try:
        page = urlopen(url).read() 
        return page.lower().decode('utf-8')
    except:
        return ""
#测试代码   
if __name__ == '__main__':
    print "---------test start"
    url =  'http://www.baidu.com'
    print get_page(url)
    print "---------test end"
