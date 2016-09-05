import numpy as np
import pandas as pd
from pandas import Series, DataFrame

arr1=np.arange(9).reshape(3,3)

print(arr1)

#concatenate for columns
print(np.concatenate([arr1,arr1],axis=1))
print("="*50)

#concatenate row
np.concatenate([arr1,arr1],axis=0)
print(np.concatenate([arr1,arr1],axis=0))
print("="*50)

#concatenating in pandas
#Series 
ser1=Series([0,1,2],index=["T","U","V"])
ser2=Series([3,4],index=["X","Y"])

print(ser1)
print("="*50)

print(ser2)
print("="*50)

#concatenating series
pd.concat([ser1,ser2])
print(pd.concat([ser1,ser2]))
print("="*50)

#concatenating for column
pd.concat([ser1,ser2],axis=1)
print(pd.concat([ser1,ser2],axis=1))
print("="*50)

pd.concat([ser1,ser2],keys=["cat1","cat2"])
print(pd.concat([ser1,ser2],keys=["cat1","cat2"]))
print("="*50)

dframe1=DataFrame(np.random.randn(4,3),columns=["X","Y","Z"])
dframe2=DataFrame(np.random.randn(3,3),columns=["Y","Q","X"])

print(dframe1)
print("="*50)

print(dframe2)
print("="*50)

#concatenating row of two data frames
pd.concat([dframe1,dframe2])
print(pd.concat([dframe1,dframe2]))
print("="*50)

#concatenating columns 
print(pd.concat([dframe1,dframe2],axis=1))
print("="*50)

#ignore index
print(pd.concat([dframe1,dframe2],ignore_index=True))
print("="*50)



