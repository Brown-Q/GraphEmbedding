import csv
import random
import numpy as np
import matplotlib.pyplot as plt
import networkx  as nx
import pandas as pd
import time

G = nx.Graph()
edge = []
with open('D:/node importance2/data.csv', encoding='gbk', errors='ignore') as f:
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
a=['1.06E+18','1.07E+18','1.12E+18','1.15E+18','1.16E+18','1.04E+18','1.13E+18','1.00E+18','1.14E+18','1.08E+18']
for i in a:
   print(nodes1[i])