# 常用方法
# datas.head( 5 ) #查看前5行
# datas.tail( 3 ) #查看后3行
# datas.values #查看数值
# datasshape #查看行数、列数
# datas.fillna(0) #将空值填充0
# datas.replace( 1, -1) #将1替换成-1
# datas.isnull() #查找datas中出现的空值
# datas.notnull() #非空值
# datas.dropna() #删除空值
# datas.unique() #查看唯一值
# datas.reset_index() #修改、删除，原有索引，详见例1
# datas.columns #查看datas的列名
# datas.index #查看索引
# datas.sort_index() #索引排序
# datas.sort_values() #值排序
# pd.merge(data1,data1) #合并
# pd.concat([data1,data2]) #合并，与merge的区别，自查
# pd.pivot_table( datas ) #用df做datas透视表（类似于Excel的数透）
# print(datas.reset_index(drop=True)) # 索引被直接删除
# print(datas.reset_index(drop=False)) # 索引列会被还原为普通列