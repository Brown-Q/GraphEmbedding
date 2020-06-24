import jieba
import csv

def jiebafenci(txt, wordslist):
    jieba.load_userdict('D:/node importance/stopwords.txt')
    words = jieba.lcut(txt)
    counts = {}
    a = 0
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    for i in wordslist:
        if i in counts:
             a = a + counts[i]
    return (a)

with open('D:/node importance/data.csv', encoding='gbk', errors='ignore') as f:
    rander = csv.reader(f)
    # 对数据循环获取
    data=[]
    for i in rander:
        data.append(i[2])
    print(data)
with open('D:/node importance/topic1.txt', encoding='utf-8') as f:
    need_words1 = f.readlines()
with open('D:/node importance/topic2.txt', encoding='utf-8') as f:
    need_words2 = f.readlines()
with open('D:/node importance/topic3.txt', encoding='utf-8') as f:
    need_words3 = f.readlines()

find1 = []
find2 = []
find3 = []
for line in need_words1:
    find1.append(line.replace('\n', '').replace('\t', ''))
for line in need_words2:
    find2.append(line.replace('\n', '').replace('\t', ''))
for line in need_words3:
    find3.append(line.replace('\n', '').replace('\t', ''))
probab_assemble = []
for f1 in data:
    f1 = f1.replace('\n', '').replace('\t', '')
    probab = []
    a1 = jiebafenci(f1, find1)
    probab.append(a1)
    a2 = jiebafenci(f1, find2)
    probab.append(a2)
    a3 = jiebafenci(f1, find3)
    probab.append(a3)
    # print(probab)
    probab1=[]
    for i in range(len(probab)):
        if sum(probab)>0:
            probab1.append(probab[i]/sum(probab))
        elif sum(probab)==0:
            probab1.append(0)
    print(probab1)
    probab_assemble.append(probab1)
with open('D:/node importance/edge probability.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in probab_assemble:
        writer.writerow(row)