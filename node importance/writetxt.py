import csv
import os
import re
# def readCsv():
datacsv={}
filepath='D:/node importance/data1'
# for root,dirs,files in os.walk(filepath):
# files=['1.csv']
files=['1.csv', '10.csv', '11.csv', '12.csv', '13.csv', '14.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv', '7.csv', '8.csv', '9.csv']
for file in files:
    with open(filepath+'/'+file, encoding='gbk', errors='ignore') as f:
        rander = csv.reader(f)
        # 对数据循环获取
        for i in rander:
            if len(i[9])>1:
                line=i[9]
                cop = re.compile("[^\u4e00-\u9fa5^.0-9！？‘”“，：；。]")
                string = cop.sub("", line)
                datacsv.setdefault(i[0], []).append(string)
            if len(i[10])>1:
                line = i[10]
                cop = re.compile("[^\u4e00-\u9fa5^.0-9！？‘”“，：；。]")
                string = cop.sub("", line)
                datacsv.setdefault(i[8], []).append(string)
datacsv.pop('user_id')
datacsv.pop('interact_id')
f=open('D:/node importance/topic.txt','w')
f2=open('D:/node importance/node.txt','w')
with open('D:/node importance/add node.txt', 'r') as f3:
    data = f3.readlines()
    data1 = [x.strip() for x in data if x.strip() != '']
print(data1)
for i in datacsv:
    if i in data1:
        line = str(datacsv[i])
        cop = re.compile("[^\u4e00-\u9fa5^.0-9！？‘”“，：；。]")
        string = cop.sub("", line)
        if len(string)>1:
            write_str = str(string) + '\n'
            write_str2=i+'\n'
            f.write(write_str)
            f2.write(write_str2)
f.close()
f2.close()