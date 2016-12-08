# -*-coding:utf-8 -*-
import csv

csvfile=file('clean_data.csv', 'rb')
reader = csv.reader(csvfile)
total=0
for line in reader:
    total+=1
    print "%s : %s\n"%(line[0],line[1])
print total
csvfile.close()

# csvfile = file('clean_data.csv', 'a')
# writer = csv.writer(csvfile)
#
# writer.writerows(st)
#
# csvfile.close()
# print "success!"