#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import shelve
#初始化数据库
#dataBaseFileName 数据库文件名
def init_dataBase(dataBaseFileName, openstyle = 'c'):
    dataBase = shelve.open(dataBaseFileName, openstyle)    #默认打开方式'c'
    #print "数据库初始化成功".decode('utf-8') 
    return dataBase


#增加记录到数据库
#dataBase数据库句柄
#keyword关键字
#url待存储网址
def add_to_dataBase(dataBase, keyword, url):
    if keyword not in dataBase:
        dataBase[keyword] = [url]
    else :
        s = dataBase[keyword]
        s.append(url)
        dataBase[keyword] = s
        
#显示数据库
#dataBaseFileName 数据库文件名
def show_dataBase(dataBaseFileName):
    dataBase = shelve.open(dataBaseFileName)
    print dataBase
    #print "所有数据显示完毕".decode('utf-8') 

#关闭数据库
#dataBase数据库句柄
def close_dataBase(dataBase):
    dataBase.close()
    #print "数据库关闭成功".decode('utf-8') 
    

#测试代码
if __name__ == '__main__':
    db_file='spider.db'
    dataBase = init_dataBase(db_file, 'n')
    add_to_dataBase(dataBase, "k1", "u1")
    add_to_dataBase(dataBase, "k1", "u2")
    add_to_dataBase(dataBase, "k2", "u3")
    add_to_dataBase(dataBase, "k3", "u4")
    add_to_dataBase(dataBase, None, "u5")
    add_to_dataBase(dataBase, None, "u6")
    close_dataBase(dataBase)
    print "显示数据库".decode('utf-8') 
    show_dataBase(db_file)