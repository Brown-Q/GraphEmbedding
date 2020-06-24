import networkx  as nx
import pandas as pd
import csv
from sklearn.decomposition import PCA
import numpy as np

with open('D:/node importance/data.csv', encoding='gbk', errors='ignore') as f1:
    rander1 = csv.reader(f1)
    edge=[]
    for i in rander1:
        data1=[]
        data1.append(i[0])
        data1.append(i[1])
        edge.append(data1)
G = nx.Graph()
G.add_edges_from(edge)

with open('D:/node importance/data.csv', encoding='gbk', errors='ignore') as f2:
    rander2 = csv.reader(f2)
    data2={}
    for i in rander2:
        data2.setdefault(i[0], []).append(int(i[3]))
        data2.setdefault(i[0], []).append(int(i[4]))
        data2.setdefault(i[0], []).append(G.degree()[i[0]])

data3={}
for node in G.nodes():
    if node in data2:
        data3.setdefault(node, []).append(data2[node][0])
        data3.setdefault(node, []).append(data2[node][1])
        data3.setdefault(node, []).append(data2[node][2])
        data3.setdefault(node, []).append(len(data2[node]))
    else:
        data3.setdefault(node, []).append(0)
        data3.setdefault(node, []).append(0)
        data3.setdefault(node, []).append(G.degree()[node])
        data3.setdefault(node, []).append(G.degree()[node])

data4=[]
for i in data3:
    data4.append(data3[i])

X=np.array(data4)
pca=PCA(n_components=4)
pca.fit(X)
component=pca.components_
variance_ratio=pca.explained_variance_ratio_
component=abs(component.T)
for i in range(0,4):
    component[:,i]=variance_ratio[i]*component[:,i]
a=pd.DataFrame(component)
b=a.sum(axis=1)
c=b/b.sum(axis=0)

data5={}
for i in data3:
    data5[i]=sum(np.multiply(np.array(c),np.array(data3[i])))
print(data5)
data5=sorted(data5.items(), key=lambda e: e[0], reverse=False)
data6 = pd.DataFrame(data5)
print(data6)
writer = pd.ExcelWriter('D:/node importance/data4/pca.xlsx')		# 写入Excel文件
data6.to_excel(writer, 'page_3', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
writer.save()
writer.close()