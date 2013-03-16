#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
#get all links form page
def get_all_link(page):
    links = []
    soup = BeautifulSoup(page)
    content = soup.findAll('a')
    for item in content:
        links.append(item['href'].encode("utf-8"))
    return links

if __name__ == '__main__':
    from  get_Page import * 
    print "---------test start"
    links1 = get_all_link(get_page('http://www.baidu.com'))
    print "first page", links1
    links2 = get_all_link(get_page(links1[0]))
    print "second page", links2
    print "---------test end"