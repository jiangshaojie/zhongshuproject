# -*- coding: utf-8 -*-
import configparser
import os
class readconf():

    def __init__(self):
        config = configparser.ConfigParser()
        # configname = 'config.conf'
        configname=os.path.curdir.join('resource')
        self.readfiles=config.read(configname, encoding="utf-8")

    def getConfig(self,section,key):
        config = configparser.ConfigParser()
        configname = 'resource/config.conf'
        config.read(configname, encoding="utf-8")
        return config.get(section,key)
    def getsections(self,section):
        config = configparser.ConfigParser()
        configname = 'resource/config.conf'
        config.read(configname, encoding="utf-8")
        return dict(config.items(section))

if __name__=='__main__':
    a=readconf()
    # print(a.getConfig('test_url','enterpriseListPro'))
    # print(a.getsections("asynt_test_uid").get('shchtest_uid'))
    # uid = a.getConfig('asynt_test_uid', 'shchtest_uid')
    # print(uid)

    uids=a.getConfig('asynt_test_uid','shchtest_uid')
    security_keys=a.getConfig('asynt_test_uid','shchtest_security_key')
    print(uids.strip("'"))
    print(security_keys)
    uid = 'FLRG5WYH'

    print(uid)
    security_key = '8OS6MDvKwLsVWPt8ji7ZXjc584jqREvFsXRAOgGiOuctYsLjq9cZxyZVkf0Dfs1H'
    print(uid==uids)
    print(type(uids))
    print(type(uid))
    a='b'
    b='b'
    print(a==b)


#print(getConfig('testuid',"test_uid"))
