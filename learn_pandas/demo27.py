import pandas as pd

path = './data_files/课件030-031/数据.xlsx'
data = pd.read_excel(path)
# 方法1：使用字典进行映射
data['性别'] = data['性别'].map({'男': '先生', '女': '女士'})
# 方法2：使用函数
data = pd.read_excel(path)


def replace_n(x):
    call_name = '先生' if x == "男" else '女士'
    return call_name


data['性别'] = data['性别'].map(replace_n)
print(data)

data = pd.read_excel(path)


def change_age(x, c_v):
    return x + c_v


data['年龄'] = data['年龄'].apply(change_age, args=(-10,))  # (-10,)表示一个参数
print(data)

data = pd.read_excel(path)
data2 = data[['语文', '数学', '英语']].apply(sum, axis=0)
print(data2)

data = pd.read_excel(path)


def BMI(data):
    身高 = data['身高']
    体重 = data['体重']
    BMI = 体重 / 身高 ** 2
    return BMI


data['BMI'] = data.apply(BMI, axis=1)
print(data)
