'''
#以下是格式定义
代码 说明
%Y 4位数的年
%y 2位数的年
%m 2位数的月[01,12]
%d 2位数的日[01，31]
%H 时（24小时制）[00,23]
%l 时（12小时制）[01,12]
%M 2位数的分[00,59]
%S 秒[00,61]有闰秒的存在
%w 用整数表示的星期几[0（星期天），6]
%F %Y-%m-%d简写形式例如，2017-06-27
%D %m/%d/%y简写形式
'''
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
data = pd.read_excel('./课件/12.日期.xlsx')
date=[d.strftime('%Y-%m-%d')for d in data.日期]
plt.plot(date,data.销售)
#文字旋转
plt.xticks(date,rotation=45)
plt.show()

#网格线
data = pd.read_excel('./课件/12.日期.xlsx')
plt.grid(axis='x',color='r',linestyle=':',linewidth=3)
plt.show()