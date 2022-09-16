import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = None
plt.rcParams['font.sans-serif'] = ['SimHei']
data = pd.read_excel('./课件/17.直方图.xlsx')
布, 图 = plt.subplots(1, 1)
图.plot(data.序号, data.身高)
# 第一种方法
# plt.locator_params("x",nbins=5)
# 第二种方法
轴 = plt.gca()  # 获取当前轴
# 轴.locator_params("x",nbins=5)
# x与y都平均分成5份
轴.locator_params(nbins=5)
plt.show()

# 设置X轴的刻度是7的倍数，或改成小数点形式
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as ticker

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False
plt.plot(data.序号, data.身高)
轴 = plt.gca()
轴.xaxis.set_major_locator(ticker.MultipleLocator(7))  # 将x轴设置成7的倍数
# 轴.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f')) 保留一位小数点
plt.show()

# 第二种处理日期轴的方法
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

data = pd.read_excel('./课件/12.日期.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False
plt.plot(data.日期, data.销售)
轴 = plt.gca()
轴.xaxis.set_major_formatter(mpl.dates.DateFormatter("%Y*%m*%d"))
plt.show()
