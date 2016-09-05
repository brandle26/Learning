import numpy as np
from pandas import Series, DataFrame

import pandas as pd

arr=np.array([[1,2,np.nan],[np.nan,3,4]])
print(arr)
print("="*50)

dframe1=DataFrame(arr,index=["A","B"],columns=["One","Two","Three"])
print(dframe1)
print("="*50)

#summing each column
print(dframe1.sum())
print("="*50)

#summing each row
print(dframe1.sum(axis=1))

#using min method to find minimum value in each column
print(dframe1.min())
print("="*50)

#finding index of minimum value
print(dframe1)
print("="*50)
print(dframe1.idxmin())
print("="*50)

#can also use max
print(dframe1)
print("="*50)
print(dframe1.max())
print("="*50)

#accumumlation sum
print(dframe1.cumsum())
print("="*50)

#describe method()
print(dframe1.describe())
print("="*50)

#getting info in correlation and covariance
#learning about correlation and covarieance
from IPython.display import YouTubeVideo
##YouTubeVideo("xGbpuFNR1ME")
##
##YouTubeVideo("4EXNedimDMs")

#using panda to get information off the web



