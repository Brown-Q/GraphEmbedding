import pandas as pd
import numpy as np
import csv

lhindex1 =[]
bc1 =[]
ac1=[]
topsis1=[]
dc1=[]
kcore1=[]
ic=[]
with open('D:/node importance/data4/output.csv', encoding='gbk', errors='ignore') as f1:
    rander1 = csv.reader(f1)
    for i in rander1:
        lhindex1.append(float(i[1]))
        # bc1.append(i[2])
        # ac1.append(i[3])
        # dc1.append(i[6])
        # kcore1.append(i[7])
        # topsis1.append(i[5])
        ic.append(float(i[8]))
IC=pd.Series(ic)
a= pd.Series(lhindex1)
print(IC,a)
IC1=IC.dropna()
a1=a.dropna()
n=IC1.count()
a1.index=np.arange(n)
IC1.index=np.arange(n)
# b= pd.Series(bc1)
# c= pd.Series(ac1)
# d= pd.Series(dc1)
# e= pd.Series(kcore1)
# f= pd.Series(topsis1)
r1 = IC1.corr(a1,method="pearson")
# r2 = IC.corr(b,method="pearson")
# r3 = IC.corr(c,method="kendall")
# r4 = IC.corr(d,method="kendall")
# r5 = IC.corr(e,method="kendall")
# r6 = IC.corr(f,method="kendall")
print(r1)