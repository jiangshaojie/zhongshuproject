# # -*- coding: UTF-8 -*-
# """
# Created on 2014.08.06
# 日志模块
#
# """
# from common.system_config import *
# import json
# if not STUB_MODE:
#     from robot.api.logger import *
#
# from decorator import *
#
# #日志输出级别定义
# LOG_MASK_FAT = 0x01
# LOG_MASK_ERR = 0x02
# LOG_MASK_WAR = 0x04
# LOG_MASK_INF = 0x08
# LOG_MASK_TRC = 0x10
# LOG_MASK_DBG = 0x20
#
# #日志输入级别标识辞典
# LOG_PMT_DICT = {LOG_MASK_DBG: 'DEBUG',
#                 LOG_MASK_TRC: 'TRACE',
#                 LOG_MASK_INF: 'INFO',
#                 LOG_MASK_WAR: 'WARN',
#                 LOG_MASK_ERR: 'ERROR',
#                 LOG_MASK_FAT: 'ERROR'}
#
# #日志级别
# LOG_LEVEL = 0x00 \
#     | LOG_MASK_FAT\
#     | LOG_MASK_ERR\
#     | LOG_MASK_WAR\
#     | LOG_MASK_INF\
#     | LOG_MASK_DBG\
#     | LOG_MASK_TRC
#
#
# @decorator
# def traced(func, *args, **kwargs):
#     TRC(func.__module__ + '.' + func.__name__ + " IN")
#     ret = func(*args, **kwargs)
#     TRC(func.__module__ + '.' + func.__name__ + " OUT")
#     return ret
#
#
# def _log_out(log_type, msg):
#     if dict == type(msg):
#         try:
#             msg = json.dumps(msg, indent=4)
#         except TypeError:
#             pass
#     if STUB_MODE:
#         print "%s %s" % (LOG_PMT_DICT[log_type], msg)
#     else:
#         write(msg, LOG_PMT_DICT[log_type])
#
#
# def _log_filter(log_type, msg):
#     if log_type & LOG_LEVEL == log_type:
#         _log_out(log_type, msg)
#
#
# def DBG(msg):
#     _log_filter(LOG_MASK_DBG, msg)
#
#
# def TRC(msg):
#     _log_filter(LOG_MASK_TRC, msg)
#
#
# def INF(msg):
#     _log_filter(LOG_MASK_INF, msg)
#
#
# def WAR(msg):
#     _log_filter(LOG_MASK_WAR, msg)
#
#
# def ERR(msg):
#     _log_filter(LOG_MASK_ERR, msg)
#
#
# def FAT(msg):
#     _log_filter(LOG_MASK_FAT, msg)
#
#
# def test():
#     #__log_out(0x01, 'message')
#     DBG('Debug')
#     INF('Information')
#     WAR('Warning')
#     ERR('Error')
#     FAT('Fatal error')
# #test()