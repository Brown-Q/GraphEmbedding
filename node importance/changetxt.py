import re
arr=[]
f = open('D://1.txt',encoding='utf-8')
for line in f:
    line=line.strip().replace("\n","").replace("\t","")
    cop=re.compile("[^\u4e00-\u9fa5^.0-9！？‘”“，：；。]")
    string=cop.sub("",line)
    arr.append(string)
f.close()
file_write_obj = open("D:/2.txt", 'w')
for var in arr:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()

