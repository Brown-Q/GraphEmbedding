import numpy as np
import csv
import pandas as pd


# 读取数据
def read(a,b,c,d):
        temp1=[]
        temp2=[]
        temp3=[]
        temp4=[]
        answer1=[]
        for key in a:
            temp1.append(float(a[key]))
        answer1.append(temp1)
        for key in b:
            temp2.append(float(b[key]))
        answer1.append(temp2)
        for key in c:
            temp3.append(float(c[key]))
        answer1.append(temp3)
        for key in d:
            temp4.append(float(d[key]))
        answer1.append(temp4)
        return np.array(answer1)


# 正向化矩阵标准化
def biaozhun1(datas):
    K = np.power(np.sum(pow(datas,2),axis=1), 0.5)
    # a=[0.16496488,0.09188105,0.53588778,0.20726629]
    # a=[0.04335934,0.10275346,0.82216995,0.03171724]
    a=[0.41234828,0.02975299,0.01029279,0.54760594]
    # a=[0.18775752,0.12493527,0.20236837,0.48493883]
    for i in range(0, K.size):
        for j in range(0, datas[i].size):
            datas[i,j] = a[i]*float(datas[i,j]) /float(K[i])  # 套用矩阵标准化的公式
    return datas


# 计算得分并归一化
def biaozhun2(answer2):
    list_max = np.array(
        [np.max(answer2[0, :]), np.max(answer2[1, :]), np.max(answer2[2, :]), np.max(answer2[3, :])])  # 获取每一列的最大值
    list_min = np.array(
        [np.min(answer2[0, :]), np.min(answer2[1, :]), np.min(answer2[2, :]), np.min(answer2[3, :])])  # 获取每一列的最小值
    max_list = []  # 存放第i个评价对象与最大值的距离
    min_list = []  # 存放第i个评价对象与最小值的距离
    answer_list = []  # 存放评价对象的未归一化得分
    for k in range(0, np.size(answer2, axis=1)):  # 遍历每一列数据
        max_sum = 0
        min_sum = 0
        for q in range(0, 4):  # 有四个指标
            max_sum += np.power(answer2[q, k] - list_max[q], 2)  # 按每一列计算Di+
            min_sum += np.power(answer2[q, k] - list_min[q], 2)  # 按每一列计算Di-
        max_list.append(pow(max_sum, 0.5))
        min_list.append(pow(min_sum, 0.5))
        answer_list.append(min_list[k] / (min_list[k] + max_list[k]))  # 套用计算得分的公式 Si = (Di-) / ((Di+) +(Di-))
        max_sum = 0
        min_sum = 0
    answer = np.array(answer_list)  # 得分归一化
    return (answer / np.sum(answer))

bc={}
lhindex={}
pagerank={}
pca={}
with open('D:/node importance/data4/data1.csv', encoding='gbk', errors='ignore') as f1:
    rander1 = csv.reader(f1)
    for i in rander1:
        bc[i[0]]=i[1]
        lhindex[i[0]]=i[2]
        pagerank[i[0]]=i[3]
        pca[i[0]]=i[4]

answer1 = read(bc,lhindex,pagerank,pca)  # 读取文件
answer2 = biaozhun1(answer1)  # 数组正向化
answer3 = biaozhun2(answer2)  # 标准化处理去钢
answer3 = (answer3  - answer3.min())/(answer3.max() - answer3.min())
data = pd.DataFrame(answer3)  # 计算得分
# print(answer3)
data2 = pd.DataFrame(data)
print(data2)
# with open('D://节点数据//email_betweenness.csv', 'w') as f:
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in bc.items()]
writer = pd.ExcelWriter('D:/node importance/data4/data2.xlsx')		# 写入Excel文件
data2.to_excel(writer, 'page_3', float_format='%.10f')		# ‘page_1’是写入excel的sheet名
writer.save()
writer.close()
print(1)