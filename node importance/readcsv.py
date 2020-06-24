import csv
import os
import re
import networkx  as nx

# def readCsv():
datacsv={}
content={}
filepath='D:/node importance/data1'
# for root,dirs,files in os.walk(filepath):
# files=['1.csv']
files=['1.csv', '10.csv', '11.csv', '12.csv', '13.csv', '14.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv', '7.csv', '8.csv', '9.csv']
for file in files:
    with open(filepath+'/'+file, encoding='gbk', errors='ignore') as f:
        rander = csv.reader(f)
        # 对数据循环获取
        for i in rander:
            if len(i[10])>1:
                line=i[10]
                cop = re.compile("[^\u4e00-\u9fa5^.0-9！？‘”“，：；。]")
                string = cop.sub("", line)
                datacsv.setdefault(i[0], []).append(i[8])
                datacsv.setdefault(i[0], []).append(string)
                datacsv.setdefault(i[0], []).append(i[6])
                datacsv.setdefault(i[0], []).append(i[7])
print(datacsv)
G = nx.Graph()
edge = []
for i in datacsv:
    for j in range(len(datacsv[i])):
        line = []
        line.append(i)
        if j % 4 == 0:
            line.append(datacsv[i][j])  # 两个点的编号
            edge.append(line)
G.add_edges_from(edge)
remove = [node for node, degree in G.degree() if degree < 4]
add=[node for node, degree in G.degree() if degree >= 4]
f = open('D:/node importance/1.csv','w',encoding='gbk')
G.remove_nodes_from(remove)
print(len(G.edges()))
print(len(G.nodes()))
f1 = open('D:/node importance/add node.txt','w')
for i in add:
    write_str2 = i + '\n'
    f1.write(write_str2)
f1.close()
csv_writer = csv.writer(f)
for i in datacsv:
    for j in range(len(datacsv[i])):
        if j%4==0:
            line=[]
            if i in add and datacsv[i][j] in add:
                line.append(i)
                line.append(datacsv[i][j])
                line.append(datacsv[i][j + 1])
                line.append(datacsv[i][j + 2])
                line.append(datacsv[i][j + 3])
                csv_writer.writerow(line)
f.close()





