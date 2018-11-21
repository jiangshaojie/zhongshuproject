# -*- coding: utf-8 -*-
import time
import random
import hashlib
import requests
import json
from  datetime import datetime
from dictdiffer import diff
class common(object):
    def prepareHeaders(self,UID, SECURITY_KEY):
        headmap = dict()
        headmap['content-type'] = 'application/json;charset=utf-8'
        timestamp = int(round(time.time() * 1000))
        nonce = round(random.random() * 1000000000)
        headmap['X-Uid'] = UID
        headmap['X-Timestamp'] = str(timestamp) + ""
        headmap['X-Nonce'] = str(nonce)
        sha = hashlib.sha1((str(nonce) + ";" + SECURITY_KEY + ";" + str(timestamp) + ";" + UID + ";").encode("utf-8"))
        signature = sha.hexdigest()
        headmap['X-Signature'] = signature
        return headmap

    def getMsg(self,url,uid,security_key,**kwargs):
        rl=requests.get(url,headers=self.prepareHeaders(uid,security_key),params=kwargs)
        rl=json.loads(rl.text)
        #返回字典结果
        return rl

    def getMsgs(self,envir_des,url,uid,security_key,**kwargs):
        rl=requests.get(url,headers=self.prepareHeaders(uid,security_key),params=kwargs)
        print(rl.url)
        filename=envir_des+"_"+str(datetime.now()).replace(" ","_").replace(":",".")+".json"
        #print(rl.content.decode("utf-8"))
        with open(filename,"a",encoding="utf-8") as a:
            a.write(rl.text)
        return filename
    def postMsg(self,url,uid,security_key,body):
        jsondata=json.dumps(body)
        #传给data的为json,所以目前body传入的为dict 字典数据
        rl = requests.post(url, data=jsondata,headers=self.prepareHeaders(uid, security_key))
        # print(rl.url)
        # filename = envir_des +".txt"
        # print(rl.content.decode("utf-8"))
        data=json.loads(rl.text)
        # print(data)
        #返回字典结果
        return data

    def postMsgs(self,url,uid,security_key,**kwargs):
        jsondata=json.dumps(kwargs)
        rl = requests.post(url, data=jsondata,headers=self.prepareHeaders(uid, security_key))
        # print(rl.url)
        # filename = envir_des +".txt"
        # print(rl.content.decode("utf-8"))

        data=json.loads(rl.text)
        print(data)
        return data


if __name__=='__main__':
    a=common()

    test_uid='IIAYDNQE'
    test_security_key='L22hP6LqNWJPQVoHbGg4TuqlXPEZm5a5eCfe23vgcZQ5E6hebPcrZrYfFMH4uhpy'
    test_url = 'http://192.168.100.202/platform/v3/enterprises/freestyle'


    puid='R01QKDQT'

    psecurity_key='1MzEKaDlCLHNZmzQeO3EokWYB0lDimXIQPc7VvkMwtTNkzIcxIXAmNZd7QGbKMPH'

    purl='https://openapi.bidata.com.cn/enterprises/freestyle'


    tetfilename=a.getMsg("测试环境",test_url,test_uid,test_security_key,key='华夏航空',mask=101001100,enableAggregate='false',page=0,size=20)

    pfilename=a.getMsg("生产环境",purl,puid,psecurity_key,key='华夏航空',mask=101001100,enableAggregate='false',page=0,size=20)

    a.compdiff(tetfilename,pfilename)