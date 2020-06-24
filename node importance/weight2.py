import numpy as np
import pandas as pd

fp="d:/data.xlsx"
epsilon = 1e-5
data=pd.read_excel(fp,index_col=None,header=None,encoding='utf8')
data = (data - data.min())/(data.max() - data.min())
m,n=data.shape
#第一步读取文件，如果未标准化，则标准化
data=data.values
print(m,n)
data2=np.zeros((4983,4))
for i in range(4983):
    for j in range(4):
        if data[i,j]-data[i,5]==0:
            data2[i,j]=0
        else:
            data2[i,j]=1/abs(data[i,j]-data[i,5])
data3=data2.sum(axis=0)
wi=data3/np.sum(data3)
print(wi)