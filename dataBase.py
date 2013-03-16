#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#add recode into dataBase list
def add_to_dataBase(dataBase, keyword, url):
    for entry in dataBase:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    dataBase.append([keyword, [url]])

#test code
if __name__ == '__main__':
    dataBase = []
    add_to_dataBase(dataBase, "k1", "u1")
    add_to_dataBase(dataBase, "k1", "u2")
    add_to_dataBase(dataBase, "k2", "u3")
    add_to_dataBase(dataBase, "k3", "u4")
    add_to_dataBase(dataBase, None, "u5")
    print dataBase