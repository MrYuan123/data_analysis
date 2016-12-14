# -*-coding:utf-8 -*-
#from Data_analysis
import handle_data,recommond_alg,TempData,most_popular
class startPro(object):

    def __init__(self):
        self.Handle=handle_data.data_standard()
        self.Rec=recommond_alg.UserCF()
        self.Popular=most_popular.MostPopular()

    def start_pro(self):
        uList = self.Handle.user_standard()
        eList=self.Handle.book_standard()
        TempData.MostPopular=self.Popular.MostPopular()

        for users in uList:
            w=self.Rec.user_proper(users,uList,eList)
            if w.__len__()!=10:
                print 'Error!'
                return 

            print "Borrowed books:==========="
            for item in uList[users]:
                print item
            print 'Recommond Book:==========='
            for item in w:
                print item

            title='%s.txt'%users
            F=open(title,'w')
            for item in uList[users]:
                F.write('#%s\n'%item)

            print "\n"

            for item in w:
                F.write('*%s\n'%item)

            F.close()


        #w =self.Rec.user_proper("0FF3B011CFCCC1CEDB575FD3142942B3",uList,eList)

        for item in w:
            print item




if __name__=='__main__':
    s = startPro()
    s.start_pro()