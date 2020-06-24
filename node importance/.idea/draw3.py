import csv
import random
import numpy as np
import matplotlib.pyplot as plt
import networkx  as nx
import pandas as pd
import time

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
l1 = sorted(G.nodes())#原始节点 排序
l2 = range(G.number_of_nodes())#新节点 排序
##新老节点一一对应
nodes1={}
nodes2={}
for i in l2:
    nodes1[l1[i]] =i
    nodes2[i]=l1[i]

N = 4983
K = 6  # 循环次数
M = 24  # 每一循环的遍历次数
# 读取数据
print("读取数据")
with open('D:/node importance/data4/links3.csv', encoding='utf-8') as f:
    data = csv.reader(f)
    network = np.zeros((24935, 2), dtype=np.int64)  # int64是numpy中引入的一个类，即 numpy.int64
    for i, line in enumerate(data):  # enumerate 将对象转为索引序列，可以同时获得索引和值。
        # print(line[0])  matlab中节点标号1~769，python中节点标号0~768.
        network[i][0] = int(line[0]) - 1
        network[i][1] = int(line[1]) - 1
        # print(network)
# 存储为邻接矩阵
new_network = np.zeros((N, N), dtype=np.int64)
for i in range(24935):
    a = network[i][0]
    b = network[i][1]
    new_network[a][b] = 1
# 定义初始状态
# print("定义初始状态")
state = np.zeros((N), dtype=np.int64)  # 初始化节点，1代表激活，0代表未激活
sentiment = np.zeros((N))
# print(sentiment .shape)#(769,)
for n in range(N):
    sentiment[n] = random.random()  # 定义社交网络中节点对某一新闻的情感指数，随机独立
# print(state.shape )#(769,)

start1=['1111681197','1293066843','1293066843','1110840514','1293066843','1111681197']
b1=[]
d1=[]
for start2 in start1:
    start=nodes1[start2]
    print(start)
    state[start] = 1  # 使一个节点成为最初的传播节点
    # 起点备份，保证每次起点相同
    old_state = state.copy()
    old_sentiment = sentiment.copy()
    # 初始化循环10次传播30步遍历769节点的张量
    c = np.zeros((K, M, N))
    # print(c.shape)
    # 开始循环
    a2=[0 for i in range(23)]
    c2=[0 for i in range(23)]
    t2=0
    for i in range(K):
        time_start = time.time()
        a1 = []
        c1=[]
        c[i][0] = old_state.copy()
        # print(old_state)
        state = old_state.copy()
        new_state = state.copy()
        sentiment = old_sentiment.copy()
        activated = [start]
        activated_num = 0
        # print("开始循环")
        # 开始传播
        number=0
        for j in range(M - 1):  # 29步后到达第30个状态
            time_start1=time.time()
            new_activated = []
            # print("开始第"+str(j)+"次传播")
            # 遍历已激活节点
            for m in range(len(activated)):
                # print("开始遍历激活节点")
                # 遍历所有节点
                for n in range(N):
                    # print("开始遍历")
                    # 判断该节点与已激活节点是否邻接
                    if (new_network[activated[m]][n] == 1):
                        # 判断是否已经激活，如果激活则跳过
                        if (new_state[n] == 0):
                            # 判断是否被激活
                            if (random.random() < 0.5 * sentiment[n]):
                                new_state[n] = 1
                                new_activated.append(n)

                        else:
                            continue

            c[i][j + 1] = new_state.copy()
            activated = new_activated.copy()
            activated_num += len(new_activated)
            a1.append(activated_num)
            time_end = time.time()
            t = time_end - time_start
            time_end1=time.time()
            t1=time_end1-time_start1
            if t1>0.2 :
                c1.append(t)
                t2=t
                number=number+1
            elif t1<= 0.2 and number>3:
                number=number+1
                t2=t2+1.5
                c1.append(t2)
            elif t1 <= 0.2 and number <= 3:
                number=number+1
                c1.append(0)
        c2=[i + j for i, j in zip(c1, c2)]
        a2=[i + j for i, j in zip(a1, a2)]
    a2=[i/20 for i in a2]
    c2=[i/20 for i in c2]
    c2[0]=0
    a2[0]=0
    print(c2)
    b1.append(a2)
    d1.append(c2)
print(b1)
print(d1)
# x_zhou=np.array(range (M))
#
# plt.figure()
# for i in range(K):
#     plt.plot(x_zhou,s[i])
# plt.ylim((0,1))
# plt.xlim((0,10))
# plt.xticks(np.linspace(0, 10, 11))#构建等差数列
# plt.yticks(np.linspace(0, 1, 11))
# plt.legend(labels = ['activated1','activated2','activated3'], loc = 'best')
# plt.xlabel('Time/step')
# plt.ylabel('Node density')
#
# plt .show()