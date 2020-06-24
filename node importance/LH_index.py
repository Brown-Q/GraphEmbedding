import networkx  as nx
import pandas as pd
import csv

def Hindex(indexList):
    indexSet = sorted(list(set(indexList)), reverse=True)
    for index in indexSet:
        # clist为大于等于指定引用次数index的文章列表
        clist = [i for i in indexList if i >= index]
        # 由于引用次数index逆序排列，当index<=文章数量len(clist)时，得到H指数
        if index <= len(clist):
            break
    return index


def LHindex(graph):
    node = {}  # 每个节点的度数
    H_index = {}  # 每个节点的H-index
    LHindex1 = {}  # 每个节点的LH-index
    for i in graph.nodes():
        node[i] = graph.degree(i)
    for i in graph.nodes():
        test = [node[j] for j in graph[i]]
        H_index[i] = Hindex(test)
    for i in graph.nodes():
        LHindex1[i] = sum(H_index[j] for j in graph[i])
    return LHindex1

G = nx.Graph()
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
lhindex = LHindex(G)
lhindex=sorted(lhindex.items(), key=lambda e: e[0], reverse=False)
print(len(G.nodes()))
print(G.size())
print(lhindex)
data2 = pd.DataFrame(lhindex)
# with open('D://节点数据//email_betweenness.csv', 'w') as f:
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in bc.items()]
writer = pd.ExcelWriter('D:/node importance/data4/lhindex.xlsx')		# 写入Excel文件
data2.to_excel(writer, 'page_3', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
writer.save()
writer.close()
