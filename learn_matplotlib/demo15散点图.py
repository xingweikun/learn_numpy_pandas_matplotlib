import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_columns=None
plt.rcParams['font.sans-serif']=['SimHei']
data=pd.read_excel('./课件/16.散点图.xlsx')
plt.scatter(data.身高,data.体重,s=data.身高,c='b',marker='o',alpha=0.6,linewidths=20)
plt.savefig('./图片/散点图.jpg')
plt.show()

#带颜色的散点图
import numpy as np
k=500
x=np.random.rand(k)
y=np.random.rand(k)
size=np.random.rand(k)*50#生成每个点的大小
#arctan2求反正切值
color=np.arctan2(x,y)#生成每个点的颜色大小
plt.scatter(x,y,s=size,c=color)
plt.colorbar()#添加颜色栏
plt.savefig('./图片/带颜色的散点图.jpg')
plt.show()

# 显示所有列，同理：max_rows
pd.options.display.max_columns=None
plt.scatter(data.身高,data.体重,s=data.身高,c=data.身高)
plt.colorbar() # 添加颜色栏
plt.show()