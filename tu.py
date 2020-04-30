import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.close('all')
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

# df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
# df2.plot.bar()
