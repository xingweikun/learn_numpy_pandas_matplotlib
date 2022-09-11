'''
subplot(nrows,ncols,sharex,sharey,subplot_kw,**fig_kw)
参数 说明
nrows 行数
ncols 列数
sharex 使用相同的x轴刻度
sharey 使用相同的y轴刻度
subplot_kw 创建关键字字典
**fig_kw 使用其它关键字
'''
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
data = pd.read_excel('./课件/09.折线与柱状组合图.xlsx')
布=plt.figure()
plt.subplot(221)
plt.bar(data.班级,data.销售量)
plt.subplot(223)
plt.pie(x=data.销售量,labels=tuple(data.班级))
plt.subplot(224)
plt.plot(data.班级,data.毛利率)
plt.savefig('./图片/subplot创建单个子图.jpg')
plt.show()

#subplots创建多个子图
布,图=plt.subplots(2,2)
图1=图[0,0]
图2=图[0,1]
图3=图[1,0]
图4=图[1,1]
图1.bar(data.班级,data.销售量)
图4.pie(x=data.销售量,labels=tuple(data.班级))
plt.savefig('./图片/subplots创建多个子图.jpg')
plt.show()
