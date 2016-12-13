# -*-coding:utf-8 -*-
import most_popular,TempData
import math

K = 100  # 用于采集的最近读者数


# =====================================
# 代码说明：
#    使用双重矩阵存储相似度矩阵
# =====================================
class UserCF(object):
    def __init__(self):
        pass

    def user_cf(self,uList):
        W = dict()  # 存相关性的字典
        print "Calculate the W:......................."
        for u in uList:
            s = dict()
            for v in uList:
                if u == v:
                    pass  # 不用处理
                else:
                    inter = uList[u] & uList[v]  # 交集
                    if len(inter) == 0:
                        # s[v]=0
                        # W[u]=s
                        pass
                    else:
                        s[v] = 1 / (
                        math.sqrt(len(uList[u]) * len(uList[v])) * math.log(1 + float(len(inter))))  # 计算相关性的等式
                        print "ok +%f " % s[v]
            W[u] = s
        print "Finish calculate W!"
        return W  # 输出为相似度矩阵

    def user_proper(self, ID,uList):
        Wm = self.user_cf(uList)
        matchBook = dict()  # 用于存储最符合要求的十本书

        if Wm.has_key(ID):  # 使用UserCF算法进行推荐

            Similar = Wm[ID]    #用于存储该id与其他id的相似度

            matchBook=dict()   #用于存储用户对该书籍的兴趣度

            for item in Similar:
                for bookitem in uList[item]:
                    if bookitem in uList[ID]:
                        pass
                    else:
                        if matchBook.has_key(bookitem):
                            matchBook[bookitem]+=Similar[item]
                        else:
                            matchBook[bookitem]=0
                            matchBook[bookitem]+=Similar[item]

            sortL = sorted(matchBook.iteritems(), key=lambda d: d[1], reverse=True)   #此处会将dict()转换成list()
            if len(sortL)==0:
                print "error!"
                return self.Popular.MostPopular()
            else:
                finalList = list()
                for item in sortL:
                    finalList.append(item[0])
                finalList.__add__(TempData.MostPopular)
                return finalList[0:10]

        else:  # 如果此ID没有借过书，无法进行推荐，使用最热算法，推荐最热书籍
            return TempData.MostPopular  # 使用最热算法




