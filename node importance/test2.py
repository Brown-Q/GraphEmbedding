import pandas as pd
import csv
import numpy as np


with open('D:/2.csv', encoding='gbk', errors='ignore') as f:
    rander = csv.reader(f)
    # 对数据循环获取
    a=[]
    b=[]
    for i in rander:
        a.append(float(i[0]))
        b.append(float(i[1]))
# c=0
# for i in a:
#     for j in a:
#         if a.index(j)>=a.index(i) and b.index(j)>=b.index(i):
#             c=c+1
#             print(c)
#         elif a.index(j)<a.index(i) and b.index(j)<b.index(i):
#             c = c + 1
# print(c)
c=sorted(a,reverse=True)
d=sorted(b,reverse=True)
e=[]
f=[]
for i in a:
    print(c.index(i))
    e.append(float(c.index(i)))
for i in b:
    f.append(float(d.index(i)))
g=pd.Series(e)
h=pd.Series(f)
# IC1=IC.dropna()
# b1=b.dropna()
# n=IC1.count()
# b1.index=np.arange(n)
# IC1.index=np.arange(n)
r = g.corr(h,method="spearman")
print(r)

