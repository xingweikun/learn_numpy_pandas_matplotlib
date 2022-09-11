import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
data = pd.read_excel('./课件/09.折线与柱状组合图.xlsx')
布=plt.figure()
#add_subplot新增子图
图1=布.add_subplot(221)
图1.bar(data.班级,data.销售量)
图4=布.add_subplot(224)
图4.pie(x=data.销售量,labels=tuple(data.班级))
plt.show()
#add_axes新增子区域
布=plt.figure()
left,bottom,width,height=0.1,0.1,0.8,0.8
图1=布.add_axes([left,bottom,width,height])
图1.bar(data.班级,data.销售量)
图1.set_title("销售量")
left,bottom,width,height=0.65,0.6,0.25,0.25
图2=布.add_axes([left,bottom,width,height])
图2.plot(data.班级,data.毛利率)
图2.set_title("毛利率")
plt.show()