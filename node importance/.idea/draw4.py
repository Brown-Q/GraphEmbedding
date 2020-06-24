import numpy as np
import matplotlib.pyplot as plt
import networkx  as nx
import pandas as pd
import math
from draw3 import b1
from draw3 import d1
a=d1
b=b1
c1=min(a[0][-1],a[1][-1],a[2][-1],a[3][-1],a[4][-1],a[5][-1])
x1=np.array(a[0])
x2=np.array(a[1])
x3=np.array(a[2])
x4=np.array(a[3])
x5=np.array(a[4])
x6=np.array(a[5])
for i in range(6):
    b[i]=[0.3*math.ceil(j) for j in b[i]]
y1=np.array(b[0])
y2=np.array(b[1])
y3=np.array(b[2])
y4=np.array(b[3])
y5=np.array(b[4])
y6=np.array(b[5])
plt.figure()
p1=plt.plot(x1, y1, c='r',lineStyle='--',marker='>',markerSize='5', linewidth=2)
p2=plt.plot(x2, y2, c='#FFA500',lineStyle='--',marker='+',markerSize='5', linewidth=2)
p3=plt.plot(x3, y3, c='#7FFF00',lineStyle='--',marker='*',markerSize='5', linewidth=2)
p4=plt.plot(x4, y4,  c='#FF00FF', lineStyle='--',marker='s',markerSize='5',linewidth=2)
p5=plt.plot(x5, y5, c='#40E0D0', lineStyle='--',marker='H',markerSize='5',linewidth=2)
p6=plt.plot(x6, y6,c='b',lineStyle='--',marker='p',markerSize='5', linewidth=2)
font1 = {'family' : 'Times New Roman','weight' : 'normal','size' : 18,}
font2 = {'family' : 'Times New Roman','weight' : 'normal','size' : 15,}
font3 = {'family' : 'Times New Roman','weight' : 'normal','size' : 13,}
plt.ylim((0,120))
plt.xlim((0,c1))
plt.xlabel('t',font1)
plt.ylabel('Activated nodes',font2)
plt.tick_params(labelsize=11)
plt.legend( labels=['LH', 'BC','AC','DC','K-core','Proposed Method'], loc='lower right', scatterpoints=1,prop=font3)
plt .show()
