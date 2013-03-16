#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from urllib2 import urlopen
import os,sys
#get page form url
def get_page(url):
    try:
        page = urlopen(url).read()
        return page
    except:
        return ""
    
if __name__ == '__main__':
    print "---------test start"
    print get_page('http://www.bistu.edu.cn')
    print "---------test end"
