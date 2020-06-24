import networkx  as nx
import pandas as pd
from edge_probability import data4
import csv

def pagerank(graph, damping_factor, max_iterations, delta):
    # pagerank算法
    # graph: 图
    #  damping_factor: 阻尼系数
    #  max_iterations: 最大迭代次数
    #  delta: 算法终止条件
    nodes = graph.nodes()
    graph_size = graph.number_of_nodes()
    # 每个节点赋予初始PR值
    page_rank = dict.fromkeys(nodes, 1.0 / graph_size)
    # 公式中的(1−α)/N部分
    damping_value = (1.0 - 0.85) / graph_size
    for i in range(max_iterations):
        change = 0
        for node in nodes:
            rank = 0
            # 根据邻居计算PR值
            for neighbor in graph[node]:
                # rank += damping_factor * (page_rank[neighbor] / len(graph[neighbor]))
                rank +=1.15*float(damping_factor[node][neighbor]) * page_rank[neighbor]/ len(graph[neighbor])+0.15
            rank += damping_value
            change += abs(page_rank[node] - rank)  # 绝对值
            page_rank[node] = rank

        # print("%sth iteration" % (i + 1))
        # print(page_rank)
        if change < delta:
            break
    return page_rank

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
page_rank=pagerank(G, data4, 100, 0.00001)
for key in page_rank:
  page_rank[key]=page_rank[key]*100
page_rank=sorted(page_rank.items(), key=lambda e: e[0], reverse=False)
print(page_rank)
data2 = pd.DataFrame(page_rank)
print(data2)
# with open('D://节点数据//email_betweenness.csv', 'w') as f:+
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in bc.items()]
writer = pd.ExcelWriter('D:/node importance/data4/pagerank.xlsx')		# 写入Excel文件
data2.to_excel(writer, 'page_3', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
writer.save()
writer.close()