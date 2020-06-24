# coding:utf-8
# 将一个图，network转换为邻接矩阵
import networkx  as nx
import xlrd
import pandas as pd
import csv

G = nx.Graph()
edge = []
# with open('D://数据//email-Eu-core.txt', 'r') as f:
#     data = f.readlines()
#     for line in data:
#         line = line.replace('\n', '').split(' ')
#         print(line)
        # line = line.replace('\n', '').replace('\t', ',').split(',')
with open('D:/node importance/data.csv', encoding='gbk', errors='ignore') as f:
    rander = csv.reader(f)
    # 对数据循环获取
    edge=[]
    for i in rander:
         line=[]
         line.append(i[0])   #两个点的编号
         line.append(i[1])
         edge.append(line)
G.add_edges_from(edge)
print(G.degree())
# l1 = sorted(G.nodes())#原始节点 排序
# l2 = range(G.number_of_nodes())#新节点 排序
# ##新老节点一一对应
# nodes={}
# for i in l2:
#     nodes[l1[i]] =i
# edge_list=[]
# like=0
# for u,v in G.edges():
#     like=like+1
#     edge_list.append((nodes[u],nodes[v]))
# print(len(G.nodes()))
# print(like)
# new_G=nx.Graph()
# new_G.add_edges_from(edge_list)
bc = nx.centrality.betweenness_centrality(G, normalized=False)
bc=sorted(bc.items(), key=lambda e: e[0], reverse=False)
print(bc)
data2 = pd.DataFrame(bc)
print(data2)
# with open('D://节点数据//email_betweenness.csv', 'w') as f:
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in bc.items()]
writer = pd.ExcelWriter('D:/node importance/data4/betweenness.xlsx')		# 写入Excel文件
data2.to_excel(writer, 'page_1', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
writer.save()
writer.close()




# print("节点编号及其节点介数最大值为：")
# bc_list = sorted(bc.items(), key=operator.itemgetter(1))
# print(bc_list)


# def savetxt(filename,x):
#     np.float16.savetxt(filename,x,fmt='%s',newline='\n')
#
# fh=open('D://节点数据//soc-Epinions1.txt', 'rb')
# G = nx.read_edgelist(fh)
# fh.close()
# A = nx.to_numpy_matrix(G)
# print(A)
# savetxt('result.txt',A)
