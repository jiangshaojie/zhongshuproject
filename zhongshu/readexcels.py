# -*- coding: utf-8 -*-
import xlrd


class ReadExcel(object):
    def __init__(self,filename):
        self.book = xlrd.open_workbook(filename)
    def readcase(self):
        sheet1=self.book.sheet_by_index(0)
        cases=list()
        # for i in range(1,)
        # print(self.book.sheet_names())
        rows=sheet1.nrows
        # print(rows)
        caselist=list()
        paramslist=list()
        for i in range(1,rows):
            rowvalues = sheet1.row_values(i)
            #读取float转int
            for value in rowvalues:
                if isinstance(value,float):
                    index=rowvalues.index(value)
                    value=int(value)
                    rowvalues[index]=value
            # rowvalues=sheet1.row_values(i)
            if rowvalues[0]!='':
                caselist.append(dict(paramslist))
                cases.append(caselist)
                caselist=rowvalues[0:4]
                paramslist.clear()
                paramslist.append(rowvalues[-2:])
            else:
                if sheet1.row_values(i)[-1]!='':
                    paramslist.append(rowvalues[-2:])
        caselist.append(dict(paramslist))
        cases.append(caselist)
        cases=cases[1:]
        print(cases)
        print(int(cases[0][0]))
        return cases
    def read_groupname(self):
        sheet1=self.book.sheet_by_index(0)
        data=sheet1.col_values(colx=0,start_rowx=1)
        #返回企业名称列表
        return data

    def read_clone(self,sheetindex,colxindex,startrow):
        sheet1 = self.book.sheet_by_index(sheetindex)
        data = sheet1.col_values(colx=colxindex, start_rowx=startrow)
        # 返回企业名称列表
        return data
if __name__=='__main__':
    # a=ReadExcel('C:/Users/jiang/Desktop/test1.xlsx')
    # a.readcase()
    # a=ReadExcel(r'C:\Users\jiang\Desktop\work\集团派系名称列表.xlsx')
    excel=ReadExcel(r'C:\Users\ChinaDaas\Desktop\work\test2.xlsx')
    names=ReadExcel(r'C:\Users\ChinaDaas\Desktop\江苏银行1000名清单集团派系测试.xlsx')
    # a.read_groupname()
    a=names.read_clone(0,5,1)
    print(a)