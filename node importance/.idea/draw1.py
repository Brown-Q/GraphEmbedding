import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt

def countlist(mylist):
    list=[]
    mylist.sort(reverse=True)
    myset = set(mylist)
    for item in myset:
        list.append(mylist.count(item))
    return list

lhindex1 =[]
bc1 =[]
ac1=[]
topsis1=[]
dc1=[]
kcore1=[]
with open('D:/node importance/data4/output.csv', encoding='gbk', errors='ignore') as f1:
    rander1 = csv.reader(f1)
    for i in rander1:
        lhindex1.append(i[1])
        bc1.append(i[2])
        ac1.append(i[3])
        dc1.append(i[6])
        kcore1.append(i[7])
        topsis1.append(i[5])
lhindex2=countlist(lhindex1)
bc2=countlist(bc1)
ac2=countlist(ac1)
dc2=countlist(dc1)
kcore2=countlist(kcore1)
topsis2=countlist(topsis1)
y1=np.array(lhindex2)
y2=np.array(bc2)
y3=np.array(ac2)
y4=np.array(dc2)
y5=np.array(kcore2)
y6=np.array(topsis2)
x1=np.array(range(len(lhindex2)))
x2=range(len(bc2))
x3=range(len(ac2))
x4=range(len(dc2))
x5=range(len(kcore2))
x6=range(len(topsis2))
font1 = {'family' : 'Times New Roman','weight' : 'normal','size' : 15,}
font2 = {'family' : 'Times New Roman','weight' : 'normal','size' : 15,}
plt.xlabel('Ranking',font1)
plt.ylabel('Frequency',font1)
plt.xlim(xmax=3250,xmin=0)
plt.ylim(ymax=80,ymin=0)
plt.tick_params(labelsize=13)
area = np.pi * 3**2  # 点面积
#  画散点图
p1=plt.scatter(x1, y1, marker='>',s=30, c='r', alpha=0.4)
p2=plt.scatter(x2, y2, marker='+',s=60,c='#FFA500', alpha=0.4)
p3=plt.scatter(x3, y3, marker='*',s=60, c='#7FFF00', alpha=0.4)
p4=plt.scatter(x4, y4, marker='s', s=25,c='#FF00FF', alpha=0.4)
p5=plt.scatter(x5, y5, marker='H',s=35, c='#40E0D0', alpha=0.4)
p6=plt.scatter(x6, y6, s=area, c='b', alpha=0.4)
plt.legend([p1,p2,p3,p4,p5,p6], ['LH', 'BC','AC','DC','K-core','Proposed Method'], loc='upper right', scatterpoints=1,prop=font2)

plt.show()