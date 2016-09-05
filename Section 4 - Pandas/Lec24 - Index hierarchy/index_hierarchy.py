import numpy as np
from pandas import Series,DataFrame
import pandas as pd

from numpy.random import randn

ser=Series(randn(6),index=[[1,1,1,2,2,2],["a","b","c","a","b","c"]])
print(ser)
print("="*50)

#checking multi levels
print(ser.index)
print("="*50)

#chekcing each set
print(ser[1])
print("="*50)
print(ser[2])
print("="*50)

#accesing a in both higher index
print(ser[:,"a"])
print("="*50)

#can use unstack() method on series so that lower index level becomes
#column index and the higher index becomes row idnex

dframe=ser.unstack()
print(dframe)
print("="*50)

#index hierarchy in dataframe
dframe2=DataFrame(np.arange(16).reshape(4,4),index=[["a","a","b","b"],[1,2,1,2]],
                 columns=[["NY","NY","LA","SF"],["cold","hot","hot","cold"]])

print(dframe2)
print("="*50)

#naming the index label
dframe2.index.names=["INDEX_1","iNDEX_2"]
dframe2.columns.names=["Cities","Temp"]
print(dframe2)
print("="*50)

#swapping index level
dframe2.swaplevel("Cities","Temp",axis=1)
print(dframe2)
print("="*50)

#sorting level

#soring the second index (inner) index
print(dframe2.sortlevel(1)) 
print("="*50)

#sorting by outer index note the sortlevel() argment is 0
print(dframe2.sortlevel(0))
print("="*50)

#computing sum in temp level
print(dframe2.sum(level="Temp",axis=1))
print("="*50)

