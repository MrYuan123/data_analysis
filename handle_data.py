# -*-coding:utf-8 -*-
import csv

#代码说明：
#    此段代码用于将存储在文件中的数据转换成字典的形式，在字典中存储学生借阅的对应图书;
#为了便于计算相似程度，因此采取set()的形式存储;
#书库：12516
#读者库：6134

class data_standard(object):
    def __init__(self):
        pass

    def user_standard(self):
        userMode=dict()
        csvfile = file('clean_data.csv', 'rb')
        reader = csv.reader(csvfile)

        for line in reader:
            if userMode.has_key(line[0]):
                userMode[line[0]].add(line[1])
            else:
                item=set()
                item.add(line[1])
                userMode[line[0]]=item

        # print userMode.__len__()
        # for k in userMode:
        #     s=userMode[k]
        #     print k+":"
        #     for m in s:
        #         print m
        #     print "\n"
        return userMode



    def book_standard(self):
        bookMode = dict()
        csvfile = file('clean_data.csv', 'rb')
        reader = csv.reader(csvfile)

        for line in reader:
            if bookMode.has_key(line[1]):
                bookMode[line[1]].add(line[0])
            else:
                item=set()
                item.add(line[0])
                bookMode[line[1]]=item

        #print bookMode.__len__()
        # for k in bookMode:
        #     s=bookMode[k]
        #     print k+" :"
        #     for m in s:
        #         print m
        #     print "\n"

        return bookMode

s=data_standard()
s.user_standard()