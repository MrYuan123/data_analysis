# -*-coding:utf-8 -*-
import csv

csvfile=file('library.csv', 'rb')
reader = csv.reader(csvfile)

st=[]

for line in reader:
    m=()
    dataT=(line[0],line[1])
    st.append(dataT)

csvfile.close()

csvfile = file('clean_data.csv', 'a')
writer = csv.writer(csvfile)

writer.writerows(st)

csvfile.close()
print "success!"