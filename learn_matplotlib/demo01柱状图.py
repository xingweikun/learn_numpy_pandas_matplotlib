import pandas as pd
import matplotlib.pyplot as plt
# 遇到数据中有中文的时候，一定要先设置中文字体
plt.rcParams['font.sans-serif']=['SimHei']# 用黑体显示中文
# 解决坐标轴负号问题
plt.rcParams['axes.unicode_minus']=False
data=pd.read_excel('./课件/01.柱状图.xlsx')
data.sort_values(by="分数",inplace=True,ascending=False)
plt.bar(data.姓名,data.分数,label="成绩",color="red",alpha=0.5)
plt.legend(loc="upper left")
plt.xlabel("姓名")
plt.ylabel("分数")
# 刻度标签及文字旋转
plt.xticks(data.姓名,rotation=45)
plt.ylim([0,100])
#紧凑型的布局
plt.tight_layout()
plt.title("三年二班学生成绩",fontsize=16,fontweight='bold')
plt.savefig('./图片/柱状图.jpg')
plt.show()