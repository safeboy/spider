#coding=GBK
import threadpool
from get_Page import *
from get_Link import *
from dataBase import *
from save_Page import * 

seedUrl = "http://www.bistu.edu.cn"     #start url
deepth = 3                              #deep
threadPoolSize = 10                     #threadPool size
dataBase = []                           #dataBase
keyword = None                          #keyWord
go = [seedUrl]                          #the list will to be crawl
done = []                               #the list have been crawl

def spider(url=None, k=None):
    if url != None:
        if url not in done:
            done.append(url)
        page = get_page(url)    #get page
        flag = savePage(page, keyword, url)  #if find the keyword ,flag is true
        if keyword == None:                 #keyword is none
            all_links = get_all_link(page)  #get all links in the page
            for item in all_links:  
                if item not in done:        #if the link not be crawl
                    go.append(item)         # add to go[]
            return url                      #return url
        else:                               #keyword is not none
            all_links = get_all_link(page)  
            for item in all_links:  
                if item not in done: 
                    go.append(item)     
            if flag == True:            
                return url
            else:                   
                return False
            
def data_processing(request, result):
    if result == False:     
        pass
    else:
        add_to_dataBase(dataBase, keyword, result)
        print result, '导入成功\n'
        print '当前深度', deepth + 1
        
        
def main():
    pool = threadpool.ThreadPool(threadPoolSize)
    requests = threadpool.makeRequests(spider, go, data_processing)
    go[:]= done[:]      #go = done
    done[:] = []        #done = []
    [pool.putRequest(req) for req in requests]  # put the requests into threadpool
    pool.wait()         #wait all requests(job) end

if __name__ == '__main__':
    while deepth >= 0:      
        deepth = deepth - 1
        main()
    print dataBase