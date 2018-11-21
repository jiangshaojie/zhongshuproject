# -*- coding: utf-8 -*-
import json
from dictdiffer import diff
from readconf import readconf
from readexcels import ReadExcel
from common import common
import time
class verifymethod(object):
    hmethod=common()
    conf=readconf()
    def compdiff(self, file1, file2):
        with open(file1, "r", encoding="utf-8") as f:
            dict1 = json.loads(f.readlines()[0])
        with open(file2, "r", encoding="utf-8")as f:
            dict2 = json.loads(f.readlines()[0])
        result = diff(dict1, dict2)
        print(list(result))
        return list(result)
    def verfiy_test_ok(self):
        pass
    def verify_product_ok(self):
        pass
    def verify_id(self):
        pass
    def diff_prd_test(self):
        pass
    def verfyasyntest(self,casefile):
        readcase=ReadExcel(casefile)
        cases=readcase.readcase()
        uid = 'FLRG5WYH'
        security_key = '8OS6MDvKwLsVWPt8ji7ZXjc584jqREvFsXRAOgGiOuctYsLjq9cZxyZVkf0Dfs1H'
        # uid=self.conf.getConfig('asynt_test_uid','shchtest_uid').strip("'")
        # security_key=self.conf.getConfig('asynt_test_uid','shchtest_security_key').strip("'")
        sutext=open("result/测试环境成功异步接口.txt",'w',encoding='utf-8')
        faltext=open("result/测试环境失败异步接口.txt",'w',encoding='utf-8')
        for case in cases:
            url=self.conf.getConfig('asyn_test',case[2])
            status_url=self.conf.getConfig('asyn_test','order_status')
            print(url)
            if case[3]=='POST':
                print(case[-1].get('body'))
                rl=self.hmethod.postMsg(url,uid,security_key,json.loads(case[-1].get('body')))
                print(rl)
                if rl.get('code')==200:
                    time.sleep(2)
                    order=rl.get('result').get('order')
                    orderstatus=self.hmethod.getMsg(status_url,uid,security_key,order=order)
                    if orderstatus.get('code')==200:
                        if orderstatus.get('result').get('size')>0 and orderstatus.get('result').get('complete') is True and orderstatus.get('result').get('status')==4:
                            sutext.write(case[1]+' 执行成功'+' '+str(rl)+' '+str(orderstatus)+'\n')
                        else:
                            faltext.write(case[1]+' 执行失败'+' ' + str(rl) + ' ' + str(orderstatus)+'\n')
                    else:
                        faltext.write(case[1]+' 执行失败'+ ' ' + str(rl) + ' ' + str(orderstatus)+'\n')
                else:
                    faltext.write(case[1]+' 执行失败'+' ' + str(rl)+'\n')
        sutext.close()
        faltext.close()


    def verfyasynproduct(self, casefile):
        readcase = ReadExcel(casefile)
        cases = readcase.readcase()
        #uid,security_key获取的值带了'',需要去除''
        uid = self.conf.getConfig('asynt_product_uid', 'pd_uid').strip("'")
        security_key = self.conf.getConfig('asynt_product_uid', 'pd_security_key').strip("'")
        # uid = 'R01QKDQT'
        # security_key = '1MzEKaDlCLHNZmzQeO3EokWYB0lDimXIQPc7VvkMwtTNkzIcxIXAmNZd7QGbKMPH'
        sutext = open("result/生产环境成功异步接口.txt", 'w', encoding='utf-8')
        faltext = open("result/生产环境失败异步接口.txt", 'w', encoding='utf-8')
        for case in cases:
            url = self.conf.getConfig('asyn_product', case[2])
            status_url = self.conf.getConfig('asyn_product', 'order_status')
            print(url)
            if case[3] == 'POST':
                print(case[-1].get('body'))
                rl = self.hmethod.postMsg(url, uid, security_key, json.loads(case[-1].get('body')))
                print(rl)
                if rl.get('code') == 200:
                    time.sleep(2)
                    order = rl.get('result').get('order')
                    orderstatus = self.hmethod.getMsg(status_url, uid, security_key, order=order)
                    if orderstatus.get('code') == 200:
                        if orderstatus.get('result').get('size') > 0 and orderstatus.get('result').get(
                                'complete') is True and orderstatus.get('result').get('status') == 4:
                            sutext.write(case[1] + ' 执行成功' + ' ' + str(rl) + ' ' + str(orderstatus)+'\n')
                        else:
                            faltext.write(case[1] + ' 执行失败' + ' ' + str(rl) + ' ' + str(orderstatus)+'\n')
                    else:
                        faltext.write(case[1] + ' 执行失败' + ' ' + str(rl) + ' ' + str(orderstatus)+'\n')
                else:
                    faltext.write(case[1] + ' 执行失败' + ' ' + str(rl)+'\n')

        sutext.close()
        faltext.close()
if __name__=='__main__':
    a=verifymethod()
    a.verfyasyntest(r'C:\Users\ChinaDaas\Desktop\work\test3.xlsx')
    # a.verfyasynproduct(r'C:\Users\ChinaDaas\Desktop\work\test3.xlsx')

