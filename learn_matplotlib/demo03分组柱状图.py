import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
data=pd.read_excel('./课件/03.分组柱状图.xlsx')
data.sort_values(by="第二年",inplace=True,ascending=False)
# print(data)
# 把dataframe转换为list
x=data['姓名'].values.tolist()
y1=data['第一年'].values.tolist()
y2=data['第二年'].values.tolist()
plt.bar(x=x,height=y1,label="第一年",color="red",width=0.3)
plt.bar(x=np.arange(len(x))+0.3,height=y2,label="第二年",color="blue",width=0.3)
# plt.xticks可以实现旋转角度，但是不能设置旋转点，所以要与轴.set_xticklabels配合使用
plt.xticks(x)
# 对轴进行操作,需要先拿到轴
zhou=plt.gca()
# 对x轴数据进行旋转45度，且以中心为旋转点【同样可以用left或right】
zhou.set_xticklabels(x,rotation=45,ha="center")
# 解决图四周的空白，是对图形操作，需要先拿到图形[也可以用紧凑型布局方案]
tuxing=plt.gcf()
tuxing.subplots_adjust(left=0.1,bottom=0.3)

#添加数据标签
# 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for x, yy in enumerate(y1):
    plt.text(x, yy + 1, str(yy), ha='center', va='bottom', fontsize=20, rotation=0)
for x, yy in enumerate(y2):
    plt.text(x + 0.3, yy + 1, str(yy), ha='center', va='bottom', fontsize=20, rotation=0)
plt.savefig('./图片/分组柱状图.jpg')
plt.show()