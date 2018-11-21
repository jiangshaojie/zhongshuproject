# -*- coding: utf-8 -*-
import readexcels
from verifymethod import verifymethod
from common import common
import json
import logging
import sys
import time

#获取logger实例
logger=logging.getLogger("AppName")

formatter=logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

#文件日志

file_handler=logging.FileHandler("logs/test.log",encoding="utf-8")
file_handler.setFormatter(formatter)

#控制台日志

consle_handler=logging.StreamHandler(sys.stdout)
consle_handler.formatter=formatter

#为Logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(consle_handler)

#指定级别
logger.setLevel(logging.INFO)

# 批量识别是否为集团母公司
def super_corporation_discern(filename,sheetindex,colxindex,startrow):
    # filename=r'C:\Users\ChinaDaas\Desktop\work\集团派系名称列表.xlsx'
    companyies=readexcels.ReadExcel(filename).read_clone(sheetindex,colxindex,startrow)
    logger.info('需要识别的公司列表'+str(companyies))
    successfilename='result/成功集团识别.txt'
    falsefilename = 'result/失败集团识别.txt'
    test_uid='IIAYDNQE'
    test_security_key='L22hP6LqNWJPQVoHbGg4TuqlXPEZm5a5eCfe23vgcZQ5E6hebPcrZrYfFMH4uhpy'
    test_url = 'http://192.168.100.202/platform/v3/relation/super_corporation_discern'

    sfile=open(successfilename,"w",encoding="utf-8")
    ffile=open(falsefilename,"w",encoding="utf-8")
    # data=json.loads(rl.text)
    # print(data)
    for i in companyies:
        data=common().postMsgs(test_url,test_uid,test_security_key,entmark=i)
        if data.get('code')==200:
            # with open(successfilename, "w", encoding="utf-8") as a:
            # sfile.write(str(data.get('entinfo').get('entname'))+' '+str(data)+'\n')
            sfile.write(i+' '+str(data.get('entinfo').get('regno'))+' '+str(data.get('entinfo').get('creditcode'))+' '+str(data.get('entinfo').get('entname'))+'\n')
            print('\n')
        else:
            # with open(falsefilename, "w", encoding="utf-8") as a:
            ffile.write(i+' '+str(data)+'\n')
            print('\n')
    sfile.close()
    ffile.close()

    # for i in companyies:
    #     common().postMsgs(successfilename,falsefilename,test_url,test_uid,test_security_key,entmark=i)
def super_corporation_discerns():
    filename=r'name.txt'
    companyies=open(filename,'r',encoding='utf-8')
    successfilename='result/成功集团识别.txt'
    falsefilename = 'result/失败集团识别.txt'
    test_uid='IIAYDNQE'
    test_security_key='L22hP6LqNWJPQVoHbGg4TuqlXPEZm5a5eCfe23vgcZQ5E6hebPcrZrYfFMH4uhpy'
    test_url = 'http://192.168.100.202/platform/v3/relation/super_corporation_discern'

    sfile=open(successfilename,"w",encoding="utf-8")
    ffile=open(falsefilename,"w",encoding="utf-8")
    # data=json.loads(rl.text)
    # print(data)
    for i in companyies.readlines():
        data=common().postMsgs(test_url,test_uid,test_security_key,entmark=i)
        if data.get('code')==200:
            # with open(successfilename, "w", encoding="utf-8") as a:
            sfile.write(i+' '+str(data.get('entinfo').get('regno'))+' '+str(data.get('entinfo').get('creditcode'))+' '+str(data.get('entinfo').get('entname'))+'\n')
            print('\n')
        else:
            # with open(falsefilename, "w", encoding="utf-8") as a:
            ffile.write(i+' '+str(data)+'\n')
            print('\n')
    sfile.close()
    ffile.close()
def superCorporationMembers ():
    #集团成员识别
    test_uid='IIAYDNQE'
    test_security_key='L22hP6LqNWJPQVoHbGg4TuqlXPEZm5a5eCfe23vgcZQ5E6hebPcrZrYfFMH4uhpy'
    test_url = 'http://192.168.100.202/platform/v3/relation/super_corporation_members'
    body="""{
          "entmark": "新湖中宝股份有限公司",
          "layer": 1,
          "relations": [
            "entOutHold",
            "personOutHold",
            "samedom",
            "manager"
          ]
        }"""

    pa=dict(json.loads(body))
    print(pa)
    re=common().postMsg(test_url,test_uid,test_security_key,pa)
    print(re)
    print(json.dumps(re))
# 验证测试环境异步接口
def asyn_test(filename):
    methods=verifymethod()
    methods.verfyasyntest(filename)
    pass
#验证生产环境异步接口
def asyn_product(filename):
    methods = verifymethod()
    methods.verfyasynproduct(filename)
def diffSCM_CP():
    #控制路径里的控股企业是否在集团派系中都查询出来
    test_uid = 'IIAYDNQE'
    test_security_key = 'L22hP6LqNWJPQVoHbGg4TuqlXPEZm5a5eCfe23vgcZQ5E6hebPcrZrYfFMH4uhpy'
    control_path = 'http://192.168.100.202/platform/v3/relation/control_path'
    super_corporation_members='http://192.168.100.202/platform/v3/relation/super_corporation_members'
    control_path_body="""{
              "entmark": "北京中数智汇科技股份有限公司",
              "relations": [
                "entOutInvest",
                "entShareholder",
                "personShareholder"
              ],
              "moreInfo": true
            }"""
    super_corporation_members_body="""
            {
          "entmark": "北京中数智汇科技股份有限公司",
          "layer": 8,
          "relations": [
            "entOutHold",
            "personOutHold",
            "samedom",
            "manager"
          ]
        }
        """
    controlparamers=dict(json.loads(control_path_body))
    superparamers=dict(json.loads(super_corporation_members_body))
    # controlparamers['entmark']='hehe'
    # print(controlparamers)
    mcompanise=set()
    with open('result/成功集团识别.txt','r',encoding="utf-8") as mcompanisefile:
        for i in mcompanisefile.readlines():
            mcompanise.add(i.split(' ')[3].strip('\n'))
    logger.info("集团母公司列表"+": "+str(mcompanise))
    refile=open("result/控制路径与集团成员对比结果.txt",'w',encoding="utf-8")
    for i in mcompanise:
        controlparamers['entmark'] = i
        superparamers['entmark'] = i
        controlre = common().postMsg(control_path, test_uid, test_security_key, controlparamers)
        corporationre=common().postMsg(super_corporation_members, test_uid, test_security_key, superparamers)
        if corporationre['code']==200 and controlre['code']==200:
            # 获取集团成员方法
            logger.info(i+' '+'集团族谱成员识别结果'+'： '+str(corporationre))
            corporationresult = corporationre['result']['nodes']
            memberscompany = list()
            for m in corporationresult:
                if m['type'] == 1:
                    memberscompany.append(m['name'])
            # logger.info(type(memberscompany))
            # print(i)
            # print(memberscompany)
            # print(i+" "+memberscompany)
            logger.info(i + ' ' + '集团族谱内公司结果' + ': ' + str(memberscompany))
            # 通过控制路径获取控股公司方法
            logger.info(i + ' ' + '控制路径识别结果' + '： ' + str(controlre))
            controlresult = controlre['result']['nodes']
            controlcompany = list()
            for n in controlresult:
                if n['type'] == 1 and n['properties'].__contains__("middlenode") is True:
                    controlcompany.append(n['name'])
            logger.info(i + ' ' + '控制路径控股公司识别结果' + '： ' + str(controlcompany))

            # 对比list
            # cc = ['深圳市海思半导体有限公司', '北京华为朗新科技有限责任公司', '深圳慧通商务有限公司', "heheda"]
            relist=list()
            for t in controlcompany:
                if memberscompany.__contains__(t):
                    pass
                else:
                    relist.append(t)
                    # print("不包含" + " " + i)
            # pass
            if len(relist)>0:
                logger.info(i + ' ' + '集团族谱不包含控制路径公司列表' + '： ' + str(relist))
                strs=''
                for entry in relist:
                    strs=strs+entry+','
                refile.write(i + " " + "不包含" + " " + strs + '\n')
            else:
                logger.info(i + ' ' + '集团族谱与控制路径公司列表一致')
        else:
            logger.info(i + ' ' + '集团族谱成员识别结果' + '： ' + str(corporationre))
            logger.info(i + ' ' + '控制路径识别结果' + '： ' + str(controlre))



#验证生产异步
# asyn_product(r'C:\Users\ChinaDaas\Desktop\work\test2.xlsx')
#验证测试异步
# asyn_test(r'C:\Users\ChinaDaas\Desktop\work\test3.xlsx')
# filename=r'C:\Users\ChinaDaas\Desktop\江苏银行1000名清单集团派系测试.xlsx'
# super_corporation_discern(filename,0,5,1)
# super_corporation_discerns()
# superCorporationMembers()
diffSCM_CP()