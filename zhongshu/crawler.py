# -*- coding: utf-8 -*-
import requests
from lxml import etree
header="""
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-cn
Cookie: security_session_verify=635c631d3b5bbc8ef1c684c993a30203; _ga=GA1.2.782853674.1528988983; _gid=GA1.2.20019521.1528988983
"""
def headers_to_dict(headers):
    #将字符串转换成字典
    headers=headers.split('\n')
    header=dict()
    for i in headers:
        h=i.strip()
        if h:
            k,v=h.split(":",1)
            header[k]=v.strip()
    return header

def parse():

    headers=headers_to_dict(header)
    print(headers)
    url='http://www.fortunechina.com/fortune500/c/2017-07/31/content_287415.htm'
    a=requests.get(url=url,headers=headers)
    a.encoding='utf-8'
    print(a.text)
    html=etree.HTML(a.text)

    html_data=html.xpath('//*[@id="yytable"]/tbody/tr[*]/td[3]/a')
    # for i in range(1,len(html_data)+1):
    #
    #     pass
    # print(len(html_data))
    with open("name.txt","w",encoding="utf-8") as file:

        for i in html_data:
            file.write(i.text)
            file.write("\n")

    # print(html_data)

    # with open(r'C:\Users\ChinaDaas\Desktop\view-source_www.fortunechina.com_fortune500_c_2017-07_31_content_287415.htm','r',encoding='utf-8') as f:
    #     for i in f.readlines():
    #         print(i)
    #         s=i.split('china500')
    #         if len(s)==2:
    #         print(s)

def parsefile(filename):
    file=open(filename,'r',encoding='utf-8')
    text=file.read()
    print(text)
    html=etree.HTML(text)
    print(html)

    # html = etree.HTML(a.text)

    html_data = html.xpath('//tr/td[3]/a')
    print(html_data)
    with open("name.txt", "a", encoding="utf-8") as file:
        for i in html_data:
            file.write(i.text)
            file.write("\n")

parse()
# parsefile(r'C:\Users\jiang\Desktop\hehe.txt')
