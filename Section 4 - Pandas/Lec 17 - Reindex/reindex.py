import numpy as np
from pandas import Series, DataFrame
import pandas as pd

from numpy.random import randn

ser1=Series([1,2,3,4],index=["A","B","C","D"])
print(ser1)
print("="*50)

#to reindex you need to use reindex function as shown below
ser2=ser1.reindex(["A","B","C","D","E","F"])

print(ser2)
print("="*50)

#redindexing ser2
#fill_value attribute can be set to 0 if the new index has no value
ser2.reindex(["A","B","C","D","E","F","G"],fill_value=0)
print(ser2.reindex(["A","B","C","D","E","F","G"],fill_value=0))
print("="*50)

ser3=Series(["USA","Mexice","Canada"],index=[0,5,10])

print(ser3)
print("="*50)


ranger=range(15)
print(ranger)
print("="*50)

#reindexing the third series
print(ser3.reindex(ranger,method="ffill"))
print("="*50)

#working with dfame
dframe=DataFrame(randn(25).reshape((5,5)),index=["A","B","D","E","F"],
                 columns=["col1","col2","col3","col4","col5"])

print(dframe)
print("="*50)
#reindexing the data frame
dframe2=dframe.reindex(["A","B","C","D","E","F"])
print(dframe2)
print("="*50)
new_columns=["col1","col2","col3","col4","col5","col6"]
dframe2.reindex(columns=new_columns)
print(dframe2)
print("="*50)

#reindexing using ix takes two arguments
print(dframe.ix[["A","B","C","D","E","F"],new_columns])
print("="*50)

