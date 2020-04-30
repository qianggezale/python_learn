from io import StringIO, BytesIO
import pandas as pd

data = ('col1,col2,col3,col5\n'
        'a,b,1\n'
        'a,b,2\n'
        'c,d,3')

data1 = pd.read_csv(StringIO(data))
print(data1)
data2 = pd.read_csv(
    StringIO(data), usecols=lambda x: x.upper() in ['COL1', 'COL3','COL5'])
print(data2)
