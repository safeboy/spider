#coding=GBK
import os,sys
def savePage(page, keyword, url):
    if (keyword != None ):              #the keyword is not none
        if str(page).find(keyword) != -1:  #page be find the keyword
            if os.path.exists(keyword) == False:
                os.mkdir(keyword)
            filedir =  keyword+ '/'+ url.replace('/', '_').replace(':', '_').replace('.', '_') + '.html'
            f = file(filedir, 'w')      #save the page that be find keyword
            f.write(page)
            f.close()
            return True
    else:                               #keyword is none
        if os.path.exists('download') == False:
            os.mkdir('download')
        filedir =  'download'+ '/'+ url.replace('/', '_').replace(':', '_').replace('.', '_') + '.html'
        f = file(filedir, 'w')
        f.write(page)
        f.close()
        return False