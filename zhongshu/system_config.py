# # -*- coding: UTF-8 -*-
# """
# Created on 2015.04.09
# 系统设定模块
#
# """
# #设置系统编码为UTF-8
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
#
# #桩模式
# STUB_MODE = False
#
# SYSTEM_ASI_SWITCH_MAP = \
# {
#     "TST_M": True,
#     "TST_N": False,
#     "TST_Q": False
# }
#
# def get_system_asi_switch():
#     ret = False
#     from wrap.eterm import eterm
#     current_system = eterm.get_instance().get_eterm_info()["system"]["system"]
#     for (system, switch) in SYSTEM_ASI_SWITCH_MAP.items():
#         if system in current_system:
#             ret = switch
#             break
#     return ret