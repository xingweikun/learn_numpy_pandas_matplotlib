import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
data=pd.read_excel('./课件/04.堆叠柱状图.xlsx')
plt.bar(x=0,bottom=data.姓名,height=0.5,width=data.语文,orientation="horizontal",color="red")
plt.bar(data.语文,bottom=data.姓名,height=0.5,width=data.数学,orientation="horizontal",color="green")
plt.bar(data.语文+data.数学,bottom=data.姓名,height=0.5,width=data.英语,orientation="horizontal",color="yellow")

for x1, y1 in enumerate(data['语文']):
    plt.text(y1-10,x1, str(y1), ha='center',va='center', fontsize=20, color='black')
for x2, y2 in enumerate(data['语文']+data['数学']):
    plt.text(y2-10,x2, str(y2), ha='center', va='center',fontsize=20, color='black')
for x3, y3 in enumerate(data['语文']+data['数学']+data['英语']):
    plt.text(y3-10,x3, str(y3), ha='center',va='center', fontsize=20, color='black')
plt.savefig('./图片/叠加条形图.jpg')
plt.show()