from io import StringIO, BytesIO
import pandas as pd
import numpy as np
# data = ('col1,col2,col3,col5\n'
#         'a,b,1\n'
#         'a,b,2\n'
#         'c,d,3')

# data1 = pd.read_csv(StringIO(data))
# print(data1)
# data2 = pd.read_csv(
#     StringIO(data), usecols=lambda x: x.upper() in ['COL1', 'COL3', 'COL5'])
# print(data2)


# 查找
# dates = pd.date_range("20200501", periods=6)
# # print(dates)
# df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates,
#                   columns=["A", "B", "C", "D"])
# print(df)

# print(df.loc["20200502",["B","C"]])
# print(df.iloc[2,2])

# 图表
import matplotlib.pyplot as plt

# data = pd.Series((np.random.randn(1000)), index=np.arange(1000))
# data=data.cumsum()

# # print(data)
# data.plot()
# plt.show()


data = pd.DataFrame(np.random.randn(1000,4), index=np.arange(1000))
data = data.cumsum()
print(data)
data.plot()
plt.show()

