# -*-coding:utf-8 -*-
from Data_analysis import handle_data,recommond_alg,TempData,most_popular
class startPro(object):

    def __init__(self):
        self.Handle=handle_data.data_standard()
        self.Rec=recommond_alg.UserCF()
        self.Popular=most_popular.MostPopular()

    def start_pro(self):
        uList = self.Handle.user_standard()
        TempData.MostPopular=self.Popular.MostPopular()

        w =self.Rec.user_proper("0FF3B011CFCCC1CEDB575FD3142942B3",uList)

        for item in w:
            print item




if __name__=='__main__':
    s = startPro()
    s.start_pro()