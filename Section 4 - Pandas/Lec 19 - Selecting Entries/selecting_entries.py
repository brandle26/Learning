import numpy as np

import pandas as pd

from pandas import Series,DataFrame

ser1=Series(np.arange(3),index=["A","B","C"])

ser1=2*ser1
print(ser1)
print("="*50)

print(ser1["B"])
print("="*50)

#can also use number as index
print(ser1[1])
print("="*50)

#calling  range
print(ser1[0:3])
print("="*50)

#can also use the index name
print(ser1[["A","B"]])
print("="*50)

#can also use boolean logic to select datas
print(ser1[ser1>3])
print("="*50)

#can also set values using this kind of method
ser1[ser1>3]=10
print(ser1)
print("="*50)

#selecting data from data frames
dframe=DataFrame(np.arange(25).reshape((5,5)),index=["NYC","LA","SF","DC","Chi"],
                 columns=["A","B","C","D","E"])
print(dframe)
print("="*50)

#selecting by column name
print(dframe["B"])
print("="*50)

#getting more than one columns
print(dframe[["B","E"]])
print("="*50)

#using logic
print(dframe[dframe["C"]>8])
print("="*50)

#can show boolean data frame
print(dframe>10)
print("="*50)

#can use ix to label index
print(dframe.ix["LA"])
print("="*50)


