import os
import zipfile
import pymongo

client = pymongo.MongoClient('localhost', 27017)
law_data1 = client.法院
sheet1 = law_data1.数据

def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')


filepath1 = 'D:\\法院数据\\2018'
newpath1 = 'D:\\数据\\2018\\'
a = -1
for i1, j1, k1 in os.walk(filepath1):
    a = a + 1
    if len(i1) == 19:
        filename1 = str(a) + '月'
        newpath1_1 = newpath1 + filename1
        os.mkdir(newpath1_1)
        b = 0
        for j in k1:
            if len(j) == 12:
                b = b + 1
                filename1_1 = str(a) + '月' + str(b) + '日'
                newpath1_2 = newpath1_1 + '\\' + filename1_1
                os.mkdir(newpath1_2)
                unzip_file(i1 + '\\' + j, newpath1_2)
dir = 'D:\\数据\\2018'
for root, dirs, files in os.walk(dir):
    for file in files:
        c = os.path.join(root, file)
        d = c.split("\\")
        f = open(c, 'r')
        e = list(f)
        f.close()
        dict = {
            '年份': d[2],
            '日期': d[4],
            '省份': d[5],
            '法院名称': d[6],
            '案件类别': d[7],
            '案件数据': e
        }
        sheet1.insert_one(dict)

