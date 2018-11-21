# -*- coding: UTF-8 -*-
import logging
import sys
class log(object):
    def deflog(self,level,name=None):
        #获取logger实例
        logger=logging.getLogger(name)

        # formatter=logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
        formatter = logging.Formatter('%(asctime)s %(name)s[line:%(lineno)d] %(levelname)-8s: %(message)s')

        #文件日志

        file_handler=logging.FileHandler("test.log")
        file_handler.setFormatter(formatter)

        #控制台日志

        consle_handler=logging.StreamHandler(sys.stdout)
        consle_handler.formatter=formatter

        #为Logger添加的日志处理器
        logger.addHandler(file_handler)
        logger.addHandler(consle_handler)

        #指定级别
        logger.setLevel(level)
    #输出级别不同的log
        return logger