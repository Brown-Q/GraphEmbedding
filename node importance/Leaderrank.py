import networkx  as nx
import pandas as pd
from edge_probability import data4
import csv

def leaderrank(graph, damping_factor, max_iterations, delta):
    # pagerank算法
    # graph: 图
    #  damping_factor: 阻尼系数
    #  max_iterations: 最大迭代次数
    #  delta: 算法终止条件
    nodes = graph.nodes()
    graph_size = graph.number_of_nodes()
    graph.add_node(str(graph_size))
    for node in nodes:
        graph.add_edge(str(graph_size), node)
    # 每个节点赋予初始PR值
    page_rank = dict.fromkeys(nodes, 1.0 / graph_size)
    page_rank[str(graph_size)]=0   #增加一个节点
    # 公式中的(1−α)/N部分
    damping_value = (1.0 - 0.85) / graph_size
    for i in range(max_iterations):
        change = 0
        for node in nodes:
            rank = 0
            # 根据邻居计算PR值
            for neighbor in graph[node]:
                print(node,neighbor)
                print(damping_factor[node][neighbor])
                # rank += damping_factor * (page_rank[neighbor] / len(graph[neighbor]))
                rank += float(damping_factor[node][neighbor]) * page_rank[neighbor]
            rank += damping_value
            change += abs(page_rank[node] - rank)  # 绝对值
            page_rank[node] = rank

        # print("%sth iteration" % (i + 1))
        # print(page_rank)
        if change < delta:
            break
    avg = page_rank[str(graph_size)] / graph_size
    page_rank.pop(str(graph_size))
    for k in page_rank.keys():
        page_rank[k] += avg
    return page_rank

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
Leader_rank=leaderrank(G, data4, 100, 0.00001)
# for key in Leader_rank:
#   Leader_rank[key]=Leader_rank[key]*10000
data2 = pd.DataFrame(Leader_rank.values())
# with open('D://节点数据//email_betweenness.csv', 'w') as f:
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in bc.items()]
# writer = pd.ExcelWriter('D://节点数据//email//email.xlsx')		# 写入Excel文件
# data2.to_excel(writer, 'page_3', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
# writer.save()
# writer.close()