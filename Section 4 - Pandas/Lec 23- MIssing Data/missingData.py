import numpy as np
from pandas import Series,DataFrame
import pandas as pd

data=Series(["one","two",np.nan,"four"])
print(data)
print("="*50)

#chekcing if there is a null value in the serices
print(data.isnull())
print("="*50)

#dropping null value
print(data.dropna())
print("="*50)

#working with dataframe
dframe=DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])

print(dframe)
print("="*50)

#cleaning dframe
#dropping any row with null value
clean_dframe=dframe.dropna()
print(clean_dframe)
print("="*50)

#dropping row only if all the vlaues in them are null
print(dframe.dropna(how="all"))
print("="*50)

#dropping column
#droppping anly column with null
print(dframe.dropna(axis=1))
print("="*50)

npn=np.nan
dframe2=DataFrame([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])
print(dframe2)
print("="*50)

#dropping using threshold argument allows us to not drop rows with at least
#the specified number of values that is not null
print(dframe2.dropna(thresh=2))
print("="*50)
print(dframe2.dropna(thresh=3))
print("="*50)

print(dframe2)

#filling na values
print(dframe2.fillna(1))
print("="*50)

#filling diffrent valeus to diffrent column
print(dframe2.fillna({0:0,1:1,2:2,3:3}))
print("="*50)

#modifying existing object
dframe2=dframe2.fillna(1)

#or
dframe2.fillna(0,inplace=True)
print(dframe2)



