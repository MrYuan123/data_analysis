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

    def user_cf(self,uList,eList):
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

    def user_cfE(self,eList):
        #===========================PART1
        C=dict()
        N=dict()
        for i in eList:
            users=eList[i]
            for u in users:
                if N.has_key(u):
                    N[u]+=1
                else:
                    N[u]=1

                for v in users:
                    if u==v:
                        continue
                    else:
                        if C.has_key(u):
                            pass
                        else:
                            C[u]=dict()

                        if C[u].has_key(v):
                            C[u][v]+=1/math.log(1+len(users))
                        else:
                            C[u][v] = 1/math.log(1 + len(users))

        #==========================================
        W=dict()
        for u, related_users in C.items():
            if W.has_key(u):
                pass
            else:
                W[u] = dict()
            for v,cuv in related_users.items():
                W[u][v] = cuv/math.sqrt(N[u]*N[v])
                #print W[u][v]
        return W
    def user_proper(self, ID,uList,eList):

        Wm=self.user_cfE(eList)
        print '\n\n'

        #ss=Wm[ID]
        #Wm = self.user_cf(uList,eList)
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

            #用于检测是否按顺序排
            # print "========================"
            # for item in sortL:
            #     print item[0]
            #     print item[1]
            # print "========================"

            if len(sortL)==0:
                print "error!"
                return TempData.MostPopular
            else:
                finalList = list()
                for item in sortL:
                    finalList.append(item[0])
                if finalList.__len__()>=10:
                    return finalList[0:10]
                else:
                    finalList.extend(TempData.MostPopular)
                    return finalList[0:10]

        else:  # 如果此ID没有借过书，无法进行推荐，使用最热算法，推荐最热书籍
            return TempData.MostPopular  # 使用最热算法




