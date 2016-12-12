# -*-coding:utf-8 -*-
import handle_data
import math
K=100 #用于采集的最近读者数

#=====================================
#代码说明：
#    使用双重矩阵存储相似度矩阵
#=====================================
class UserCF(object):
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



    def user_cf(self):
        W=dict()    #存相关性的字典
        uList=self.Handle.user_standard()
        for u in uList:
            s = dict()
            for v in uList:
                if u==v:
                    pass   #不用处理
                else:
                    inter=uList[u]& uList[v]   #交集
                    if len(inter)==0:
                        # s[v]=0
                        # W[u]=s
                        pass
                    else:
                        s[v]=1/( math.sqrt( len(uList[u]) * len(uList[v]) ) * math.log(1+ float(len(inter))))   #计算相关性的等式
                        print "ok +%f "%s[v]
            W[u] = s

        return W    #输出为相似度矩阵

    def user_proper(self,ID):
        Wm=self.user_cf()
        #Wm=dict()
        closeUser=dict()

        if Wm.has_key(ID):              #使用UserCF算法进行推荐
            caldict=Wm[ID]
            return caldict

        else:                           #如果此ID没有借过书，无法进行推荐，使用最热算法，推荐最热书籍
            return self.MostPopular()   #使用最热算法



s=UserCF()
w=s.user_proper("0FF3B011CFCCC1CEDB575FD3142942B3")
for item in w:
    print item
    print w[item]
# W=s.user_cf()
# for item in W:
#     print W[item]
# for item in s.user_proper("ss"):
#     print item
