
from numpy import *

# print(eye(20))

import numpy as np

# data = np.arange(18)
# print(data)
# re_data = data.reshape(3, 3, 2)
# print(re_data)

x = np.array([[1,  2],  [3,  4],  [5,  6]])
print(x)
print(x.ndim)
y = x[[0, 1, 2],  [0, 1, 0]]
print(y)
