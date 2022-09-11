import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_columns=None
plt.rcParams['font.sans-serif']=['SimHei']
data=pd.read_excel('./课件/17.直方图.xlsx')
plt.hist(data.身高,bins=30,facecolor='b',edgecolor='r',alpha=0.8)
plt.show()

#轴的颜色及隐藏轴边框
布,图=plt.subplots(1,1)
图.spines['left'].set_color('g')
图.spines['bottom'].set_color('r')
图.spines['top'].set_color('none')
图.spines['right'].set_color('none')
plt.xlim([0,10])
plt.ylim([0,5])
#翻转x轴和y轴
plt.gca().invert_yaxis() # 翻转y轴
plt.gca().invert_xaxis() # 翻转x轴
plt.show()
'''
图.xaxis.set_ticks_position('top') # x轴显示在顶部
图.yaxis.set_ticks_position('left') # y轴显示在左侧

图.spines['left'].set_color('none')
图.spines['bottom'].set_color('none')
图.spines['top'].set_color('none')
图.spines['right'].set_color('none')
图.set_xticks([])
图.set_yticks([])
将上下左右全设置成“无”
刻度也设置成“无”
也可以写成：
图.spines['left'].set_visible(False) 
'''