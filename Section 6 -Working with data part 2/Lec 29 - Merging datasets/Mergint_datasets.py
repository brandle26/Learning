import numpy as np
import pandas as pd
from pandas import Series,DataFrame

dframe1=DataFrame({"key":["X","Z","Y","Z","X","X"],"data_set_1":np.arange(6)})
print(dframe1)
print("="*50)

dframe2=DataFrame({"key":["Q","Y","Z"],"data_set_2":[1,2,3]})
print(dframe2)
print("="*50)

#use merge method on the dataframe
#merges overlappinf columns
#or merge columns with the same column values in keys or overlapping values
print(pd.merge(dframe1,dframe2))
print("="*50)

#specitying  the specific columns to match
#use on attribute
print(pd.merge(dframe1,dframe2,on="key"))
print("="*50)

#we can also specity which dataframe's key to use
#note here how="left" tells the method merge to use the
#data frame passed first in the left
print(pd.merge(dframe1,dframe2,on="key",how="left"))
print("="*50)

print(pd.merge(dframe1,dframe2,on="key",how="right"))
print("="*50)

#can use both of them
#to do so you can create union of both keys
print(pd.merge(dframe1,dframe2,on="key",how="outer"))

#many to many merge
dframe3=DataFrame({"key":["X","X","X","Y","Z","Z"],"data_set_3":range(6)})

dframe4=DataFrame({"key":["Y","Y","X","X","Z"],"data_set_4":range(5)})

print(dframe3)
print("="*50)

print(dframe4)
print("="*50)

#merging them
print(pd.merge(dframe3,dframe4))
print("="*50)

#merging with multiple data keys
df_left=DataFrame({"key1":["SF","SF","LA"],"key2":["one","two","one"],"left_data":[10,20,30]})

df_right=DataFrame({"key1":["SF","SF","LA","LA"],"key2":["one","one","one","two"],"right_data":[40,50,60,70]})

print(df_left)
print("="*50)

print(df_right)
print("="*50)

#merging multiple key data
print(pd.merge(df_left,df_right,on=["key1","key2"],how="outer"))
print("="*50)

#panda automatically adds suffix to overlaping key names
#this can happen when merge oly by one key
print(pd.merge(df_left,df_right,on="key1"))
print("="*50)

#you can specify what the suffix was if you do not want it to be automatic
pd.merge(df_left,df_right,on="key1",suffixes=("_lefty","_righty"))
print(pd.merge(df_left,df_right,on="key1",suffixes=("_lefty","_righty")))
print("="*50)


