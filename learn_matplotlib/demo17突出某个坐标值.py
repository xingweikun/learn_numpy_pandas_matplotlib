import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_columns=None
plt.rcParams['font.sans-serif']=['SimHei']
data=pd.read_excel('./课件/17.直方图.xlsx')
布,图=plt.subplots(1,1)
图.plot(data.序号,data.身高)
plt.gca().get_xticklabels()[1].set(color='red',fontsize=30)
plt.show()