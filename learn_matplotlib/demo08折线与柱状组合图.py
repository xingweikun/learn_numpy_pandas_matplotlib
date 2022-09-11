import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
data=pd.read_excel('./课件/09.折线与柱状组合图.xlsx')
#柱图
plt.bar(data.班级,data.销售量,color='r',label='销售量',alpha=0.6)
#显示图例
plt.legend()
#平均线-折线图
平均线=np.mean(data.销售量)
plt.axhline(y=平均线,color="blue",linestyle=':')
#plt.axhline(y=0.0, c="r", ls="--", lw=2)
'''
y：水平参考线的出发点
c：参考线的线条颜色
ls：参考线的线条风格
lw：参考线的线条宽度
'''
plt.savefig('./图片/折线与柱状组合图.jpg')
plt.show()