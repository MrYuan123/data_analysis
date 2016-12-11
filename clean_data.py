# -*-coding:utf-8 -*-
import csv

csvfile=file('dataS.csv', 'rb')
reader = csv.reader(csvfile)
total=0
for line in reader:
    total+=1
    print line
print total
csvfile.close()

# csvfile = file('clean_data.csv', 'a')
# writer = csv.writer(csvfile)
#
# writer.writerows(st)
#
# csvfile.close()
# print "success!"