import csv
import networkx  as nx

with open('D:/node importance/user probability.csv', encoding='gbk', errors='ignore') as f1:
    rander1 = csv.reader(f1)
    # 对数据循环获取
    data1={}
    for i in rander1:
        data1.setdefault(i[0], []).append(i[1])
        data1.setdefault(i[0], []).append(i[2])
        data1.setdefault(i[0], []).append(i[3])

with open('D:/node importance/user_edge probability.csv', encoding='gbk', errors='ignore') as f2:
    rander2 = csv.reader(f2)
    # 对数据循环获取
    data2={}
    for i in rander2:
        data2[i[0]]={}

with open('D:/node importance/user_edge probability.csv', encoding='gbk', errors='ignore') as f2:
    rander2 = csv.reader(f2)
    for i in rander2:
        data2[i[0]].setdefault(i[1], []).append(i[2])
        data2[i[0]].setdefault(i[1], []).append(i[3])
        data2[i[0]].setdefault(i[1], []).append(i[4])

with open('D:/node importance/data.csv', encoding='gbk', errors='ignore') as f3:
    rander3 = csv.reader(f3)
    edge=[]
    for i in rander3:
        data3=[]
        data3.append(i[0])
        data3.append(i[1])
        edge.append(data3)
G = nx.Graph()
G.add_edges_from(edge)
data4={}
for node in G.nodes():
    for neighbor in G[node]:
        data4[node]={}
for node in G.nodes():
    for neighbor in G[node]:
        if node in data2 and neighbor in data2[node]:
           c=0
           for i in range(3):
               a=float(data1[neighbor][i])
               b=float(data2[node][neighbor][i])
               c=c+a*b
           data4[node][neighbor]=0.5/G.degree()[neighbor]+0.5*c
        else:
            data4[node][neighbor]=1/G.degree()[neighbor]


