#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from optparse import OptionParser


def optionParse():
    #创建对象
    parser = OptionParser(usage="%prog [-u] [-d] [-f] [-l] [-t] [-db] [-k] [-test]",
                          version="%prog 0.1")  
    
    #参数设置
    parser.add_option("-u", "--url", dest="url",
                      default="http://www.baidu.com", 
                      help="种子网址".decode('utf-8') ,
                      metavar="URL")
    parser.add_option("-d", "--deep", dest="deep",
                      default=0, 
                      help="深度".decode('utf-8') ,
                      metavar="DEEP")
    parser.add_option("-f", "--file",
                      dest="logfile",
                      default="spider.log",
                      help="日志文件".decode('utf-8') ,
                      metavar="LOGFILE")
    parser.add_option("-l", "--loglevel",
                      dest="loglevel",
                      default=1, 
                      help="日志详细程度(1-5)".decode('utf-8') ,
                      metavar="LOGLEVEL")
    parser.add_option("-t", "--thread",
                      dest="threadnumber",
                      default=1, 
                      help="线程数(1-10)".decode('utf-8') ,
                      metavar="THREADNUMBER")
    parser.add_option("--dbfile",
                      dest="dbfile",
                      default="spider.db", 
                      help="数据库文件".decode('utf-8') ,
                      metavar="DBFILE")
    parser.add_option("-k", "--keyword",
                      dest="keyword",
                      default=None, 
                      help="关键字".decode('utf-8') ,
                      metavar="KEYWORD")
    parser.add_option("--testself",
                      dest="testself",
                      default=False, 
                      help="程序自检".decode('utf-8') ,
                      metavar="LOGLEVEL",
                      action="store_true")
    
    (options, args) = parser.parse_args()

    if options.testself:
        print "程序正在自检".decode('utf-8')
    
    if options.threadnumber not in range(1, 10):
        parser.error("-th threadnumber 错误，修正范围1-10".decode('utf-8') )
    if options.loglevel not in range(1, 5):
        parser.error("-l loglevel 错误，修正范围1-5".decode('utf-8') )
    
    return options
#测试代码
if __name__ == '__main__':
    optionParse()