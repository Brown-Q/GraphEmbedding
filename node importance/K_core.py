import networkx as nx
import pandas as pd
import csv

def k_shell(graph):
    importance_dict = {}
    level = 1
    while len(graph.degree):
        importance_dict[level] = []
        while True:
            level_node_list = []
            for item in graph.degree:
                if item[1] <= level:
                    level_node_list.append(item[0])
            graph.remove_nodes_from(level_node_list)
            importance_dict[level].extend(level_node_list)
            if not len(graph.degree):
                return importance_dict
            if min(graph.degree, key=lambda x: x[1])[1] > level:
                break
        level = min(graph.degree, key=lambda x: x[1])[1]

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
result = k_shell(G)
kshell = {}
for key in result:
    for value in result[key]:
        kshell[value] = key
print(kshell)
Kshell=sorted(kshell.items(), key=lambda e: e[0], reverse=False)
data = pd.DataFrame(Kshell)
print(Kshell)
print(data)
# writer = pd.ExcelWriter('D:/node importance/data4/k-core.xlsx')		# 写入Excel文件
# data.to_excel(writer, 'page_3', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
# writer.save()
# writer.close()