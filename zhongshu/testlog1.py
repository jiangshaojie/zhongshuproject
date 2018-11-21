# -*- coding: utf-8 -*-
import logging
import sys

#获取logger实例
logger=logging.getLogger("AppName")

formatter=logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

#文件日志

file_handler=logging.FileHandler("logs/test.log")
file_handler.setFormatter(formatter)

#控制台日志

consle_handler=logging.StreamHandler(sys.stdout)
consle_handler.formatter=formatter

#为Logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(consle_handler)

#指定级别
logger.setLevel(logging.INFO)
#输出级别不同的log

logger.debug('this is debug info')
logger.info('this is information')
logger.warning('this is warning message')
logger.error('this is error message')
logger.fatal('this is fatal message, it is same as logger.critical')
logger.critical('this is critical message')
def test():
    logger.info("heheda")
    pass
test()


