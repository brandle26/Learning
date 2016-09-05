import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#reading csv uring read_csv() file
dframe=pd.read_csv("Lec25.csv")
print(dframe)
print("="*50)

print(dframe["fruit"])
print("="*50)

#reading csv using read_table()
dframe=pd.read_table("Lec25.csv",sep=",")
print(dframe)
print("="*50)

#reading specified numher of row
dframe2=pd.read_csv("Lec25.csv",nrows=2) #read only two rows
print(dframe2)
print("="*50)

print(dframe)
print("="*50)

#export dataframe to a file
dframe.to_csv("mytextdata_out.csv")

import sys

dframe.to_csv(sys.stdout)
print("="*50)

#differente delimiter or seperator
dframe.to_csv(sys.stdout,sep="?")
print("="*50)

#reading only subset of column
print("dframe.to_csv(sys.stdout,columns=[0,1,2])")

