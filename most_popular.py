# -*-coding:utf-8 -*-
from Data_analysis import handle_data
class MostPopular(object):
    def __init__(self):
        self.Handle=handle_data.data_standard()

    def MostPopular(self):
        Utimes=dict()
        gList=self.Handle.book_standard()

        for numb in gList:
            Utimes[numb]=len(gList[numb])    #使用dict()存储书及其对应的借阅次数

        #print type(Utimes)
        sortL=sorted(Utimes.iteritems(),key=lambda d:d[1], reverse = True)    #这一步的排序相当于把sortL定义为list类型
        #print type(sortL)

        finalList=list()
        flag=0
        for item in sortL:
            finalList.append(item[0])
            flag+=1
            if flag==10:
                return finalList     #输出为最热的十本书的list()
