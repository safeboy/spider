#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
from urlparse import urljoin
#get all links form page
def get_all_link(page, url):
    links = []
    soup = BeautifulSoup(page)
    content = soup.findAll('a')
    for item in content:
        u = urljoin(url, item['href'].encode("utf-8"))
        links.append(u)
    return links

if __name__ == '__main__':
    from  get_Page import * 
    print "---------test start"
    url =  'http://www.bistu.edu.cn'
    links1 = get_all_link(get_page(url), url)
    print "first page", links1
    links2 = get_all_link(get_page(links1[0]), links1[0])
    print "second page", links2
    print "---------test end"