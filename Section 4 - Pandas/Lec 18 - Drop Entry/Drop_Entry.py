import numpy as np
from pandas import Series,DataFrame
import pandas as pd

ser1=Series(np.arange(3),index=['a','b','c'])
print(ser1)
print("="*50)

#dropping an index
print(ser1.drop("b"))
print("="*50)

#dropping on dataframe
dframe1=DataFrame(np.arange(9).reshape((3,3)),index=["SF","LA","NY"],columns=["pop","size","year"])
print(dframe1)
print("="*50)


#dropping a row form dataframe
print(dframe1.drop("LA"))
print("="*50)

#note this is not permanent.
dframe2=dframe1.drop("LA")
print(dframe2)
print("="*50)

#dropping column
#axis is 0 for row and 1 for column
print(dframe1.drop("year",axis=1))
print("="*50)
