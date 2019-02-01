import pandas as pd 
import numpy as np

# one dimensional array pandas

data = [1,2,3,4]
data_pd = pd.Series(data)
print(data_pd.dtype)

# one dimensional array with numpy
data_pd2 = pd.Series(data, dtype=np.float64)
print(data_pd2.dtype)

print(2 * data_pd)

print(data_pd[2])
data_pd[3] = 9
print(data_pd[3])

d1 = { 'one': [1,2,3,4], 'two': [9,8,7,6]}
df1 = pd.DataFrame(d1)
print(df1)
print(df1['one'])
print(df1['one'][2])
print(df1.loc[1][1])

data_dict = {'item1': pd.DataFrame(np.random.randn(4,3)), 'item2': pd.DataFrame(np.random.randn(4,2))}
data_panel = pd.Panel(data_dict)
print(data_panel['item2'])
