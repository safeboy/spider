#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from urlparse import urljoin
from lxml import etree
#从页面获取所有链接
def get_all_link(page, url):
    links = []                                      #用来存放页面链接
    html = etree.HTML(page)
    hrefs = html.xpath(u"//a")                      #提取超链接节点
    for href in hrefs:                              #提取链接
        newUrl =  urljoin(url,href.attrib['href'])  #整理链接
        links.append(newUrl)                        #添加
    print links
    return links                                    #返回

#测试代码
if __name__ == '__main__':
    from  get_Page import * 
    print "---------test start"
    url =  'http://www.bistu.edu.cn'
    links1 = get_all_link(get_page(url), url)
    print "first page", links1
    links2 = get_all_link(get_page(links1[0]), links1[0])
    print "second page", links2
    print "---------test end"