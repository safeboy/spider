# -*- coding: UTF-8 -*-
import threadpool
from get_Page import *
from get_Link import *
from dataBase import *
from save_Page import *
from optionParse import *
from logger import *

options = optionParse()                       #处理命令行参数
seedUrl = options.url                         #种子url
deep = options.deep                           #深度
threadPoolSize = options.threadnumber         #线程池大小
db_file= options.dbfile                       #数据库文件
keyword = options.keyword                     #关键字
go = [seedUrl]                                #待抓取网址列表
done = []                                     #已抓取网址列表
logfile = options.logfile                     #日志文件
Level = options.loglevel * 10                 #日志级别
logger = initlog(logfile, Level)              #初始化日志对象

#爬虫驱动函数
#url起始网址
#k关键字
def spider(url=None, keyword=None):
    if url != None:
        if url not in done:
            done.append(url)
        page = get_page(url)                #获取页面
        flag = savePage(page, keyword, url) #存储页面
        if keyword == None:                 #指定关键字
            all_links = get_all_link(page, url)  #从页面获取所有链接
            for item in all_links:  
                if item not in done:        #如果曾近没有抓取
                    go.append(item)         #添加到go[]
            return url                      #返回url
        else:                               #没有指定关键字
            all_links = get_all_link(page, url)  
            for item in all_links:  
                if item not in done: 
                    go.append(item)     
            if flag == True:            
                return url
            else:                   
                return False

#线程池回调函数
#request任务
#result任务返回值
def data_processing(request, result):
    if result == False:     
        pass
    else:
        add_to_dataBase(dataBase, keyword, result)
        print result.decode('utf-8') , '导入成功\n'.decode('utf-8') 
        print '当前深度'.decode('utf-8') , nowdeep
        logger.info(result.decode('utf-8') + '导入成功\n'.decode('utf-8') )
        
       
def main():
    pool = threadpool.ThreadPool(threadPoolSize)
    requests = threadpool.makeRequests(spider, go, data_processing)
    go[:]= done[:]      #done[]赋值给go[]
    done[:] = []        #done[]置空
    [pool.putRequest(req) for req in requests]  # 将任务放入线程池
    pool.wait()         #等待所有任务完成

#测试代码
if __name__ == '__main__':
    dataBase = init_dataBase(db_file, 'n')
    nowdeep = 0
    while nowdeep <= deep:      
        nowdeep = nowdeep + 1
        main()   
    close_dataBase(dataBase)
    show_dataBase(db_file)    
