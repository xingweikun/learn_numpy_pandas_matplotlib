import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
data=pd.read_excel('./课件/01.柱状图.xlsx')
data.sort_values(by="分数",inplace=True,ascending=False)
plt.bar(x=0,bottom=data.姓名,height=0.5,width=data.分数,orientation="horizontal",color="red",alpha=0.5)
plt.xlabel("姓名")
plt.ylabel("分数")
plt.tight_layout()
plt.title("三年二班学生成绩",fontsize=16)
plt.savefig('./图片/水平条形图.jpg')
plt.show()