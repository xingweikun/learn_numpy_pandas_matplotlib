import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
布 = plt.figure()
plt.subplot(221)
plt.plot(["A","B","C"],[1,2,3],'ro-')
plt.title("图1",c='b')
# 字典=dict(facecolor='yellow', pad=5, alpha=0.2)
plt.xlabel("x轴",bbox={'facecolor':'yellow','pad':5,'alpha':0.2})
plt.subplot(222)
plt.subplot(223)
plt.subplot(224)
# 整个画板的标题
plt.suptitle("画板",fontsize=16,fontweight='bold',color='r')
# wspace子图之间的宽度，hspace子图之间的高度，left代表子图与布的左边距离
plt.subplots_adjust(left=0.2,top=0.8,wspace=0.8,hspace=0.8,bottom=0.1)
plt.show()

#折线的样式
x= ["A","B","C","D","E","F"]
y= [1,10,7,5,11,6]
# drawstyle有steps、steps-pre、steps-mid、steps-post和默认共5种
plt.plot(x,y,"r-",drawstyle='steps-pre')
plt.show()

#线条及填充
# 解决坐标轴负号问题
plt.rcParams['axes.unicode_minus']=False
# 画横线与纵线
plt.axhline(y=0.2,linewidth=8,c='r') # 横线
plt.axvline(x=0.4) # 纵线
# 线段
plt.axhline(y=0.5,xmin=0.2,xmax=0.6,c='g')
# 填充
plt.axhspan(1,1.3,facecolor='y',alpha=0.5)
plt.axvspan(1,1.3,facecolor='b',alpha=0.5)
# 设置坐标轴
plt.axis([-1,2,-1,2])
plt.show()

#交差及填充
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2*np.pi*x)
y2 = 1.2*np.sin(4*np.pi*x)
布, 图 = plt.subplots()
图.plot(x, y1, x, y2, color='black')
图.fill_between(x, y1, y2, where=y2>y1, facecolor='green')
图.fill_between(x, y1, y2, where=y2<=y1, facecolor='red')
plt.show()