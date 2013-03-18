#!/usr/bin/env python
# -*- coding: UTF-8 -*-
def initlog(logfile, Level):
     import logging
     logger = logging.getLogger()
     hdlr = hdlr = logging.FileHandler(logfile)
     formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
     hdlr.setFormatter(formatter)
     logger.addHandler(hdlr)
     logger.setLevel(Level)
     return logger

if __name__ == '__main__':
     logfile = 'log.txt'
     logger = initlog(logfile)
     logger.error('messagedebug')
     logger.info('messageinfo')
