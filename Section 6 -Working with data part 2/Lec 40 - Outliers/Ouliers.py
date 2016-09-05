import numpy as np
import pandas as pd
from pandas import Series, DataFrame

np.random.seed(12345)

dframe=DataFrame(np.random.randn(1000,4))
print(dframe.head())

print("="*50)

print(dframe.describe())
print("="*50)

col=dframe[0]

print(col.head())
print("="*50)

#cheking which values in column are greater than 3
print(col[np.abs(col)>3])
print("="*50)

#chekcig for same codition for dataframe
dframe[(np.abs(dframe)>3).any(1)]

print(dframe[(np.abs(dframe)>3).any(1)])
print("="*50)

#capping data at 3
dframe[np.abs(dframe)>3]=np.sign(dframe)*3
print(dframe.describe())
