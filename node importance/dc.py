import networkx as nx
import pandas as pd
import csv


G = nx.Graph()
edge = []
with open('D:/node importance/data.csv', encoding='gbk', errors='ignore') as f:
    rander = csv.reader(f)
    # 对数据循环获取
    for i in rander:
         line=[]
         line.append(i[0])   #两个点的编号
         line.append(i[1])
         edge.append(line)
G.add_edges_from(edge)
dc = nx.algorithms.centrality.degree_centrality(G)
dc=sorted(dc.items(), key=lambda e: e[0], reverse=False)
data = pd.DataFrame(dc)
writer = pd.ExcelWriter('D:/node importance/data4/dc.xlsx')		# 写入Excel文件
data.to_excel(writer, 'page_1', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
writer.save()
writer.close()

