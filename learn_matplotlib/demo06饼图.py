import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel('./课件/07.饼图.xlsx')
plt.pie(x=data.第一次, labels=tuple(data.姓名), explode=(0, 0.2, 0), colors=['r', 'g', 'b'], shadow=True,
        autopct='%.2f%%', startangle=90, counterclock=False, labeldistance=0.8, radius=1.3, pctdistance=0.3,
        textprops={'fontsize': 20, 'color': 'black'})
# 将饼图显示为正圆形,plt.axis( )
plt.axis('equal')
# 添加图例，plt.legend( )
# loc = 'upper right' 位于右上角
# bbox_to_anchor=[0.5, 0.5] # 外边距 上边 右边
# ncol=2 分两列
# borderaxespad = 0.3图例的内边距
plt.legend(loc="upper right", fontsize=10, bbox_to_anchor=(1.1, 1.05), borderaxespad=0.3, ncol=3)
plt.savefig('./图片/饼图.jpg', dpi=200, bbox_inches='tight')  # bbox_inches='tight' 忽略不可见的轴
plt.show()
'''
def pie(x, explode=None, labels=None, colors=None, autopct=None,
 pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None,
 radius=None, counterclock=True, wedgeprops=None, textprops=None,
 center=(0, 0), frame=False, rotatelabels=False, hold=None, data=None)
x :(每一块)的比例，如果sum(x) > 1会使用sum(x)归一化；
labels :(每一块)饼图外侧显示的说明文字；
explode :(每一块)离开中心距离；
startangle :起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起；
shadow :在饼图下面画一个阴影。默认值：False，即不画阴影；
labeldistance :label标记的绘制位置,相对于半径的比例，默认值为1.1, 如<1则绘制在饼图内侧；
autopct :控制饼图内百分比设置,可以使用format字符串或者format function '%1.1f'指小数点前后位数(没有用空格补齐)；
pctdistance :类似于labeldistance,指定autopct的位置刻度,默认值为0.6；
radius :控制饼图半径，默认值为1；counterclock ：指定指针方向；布尔值，可选参数，默认为：True，即逆时针。将值改为False即可改为顺时
针。wedgeprops ：字典类型，可选参数，默认值：None。参数字典传递给wedge对象用来画一个饼图。例如：wedgeprops={'linewidth':3}设置
wedge线宽为3。
textprops ：设置标签（labels）和比例文字的格式；字典类型，可选参数，默认值为：None。传递给text对象的字典参数。
center ：浮点类型的列表，可选参数，默认值：(0,0)。图标中心位置。
frame ：布尔类型，可选参数，默认值：False。如果是true，绘制带有表的轴框架。
rotatelabels ：布尔类型，可选参数，默认为：False。如果为True，旋转每个label到指定的角度。
'''
