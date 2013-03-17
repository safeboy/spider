#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os,sys
def savePage(page, keyword, url):
    if (keyword != None ):              #关键字为空
        if str(page).find(keyword) != -1:  #在页面中找到关键字
            if os.path.exists(keyword) == False:
                os.mkdir(keyword)
            filedir =  keyword+ '/'+ url.replace('/', '_').replace(':', '_').replace('.', '_') + '.html'
            f = file(filedir, 'w')      #保存页面
            f.write(page)
            f.close()
            return True
    else:                               #关键字为空
        if os.path.exists('download') == False:
            os.mkdir('download')
        filedir =  'download'+ '/'+ url.replace('/', '_').replace(':', '_').replace('.', '_') + '.html'
        f = file(filedir, 'w')          #保存页面
        f.write(page)
        f.close()
        return False