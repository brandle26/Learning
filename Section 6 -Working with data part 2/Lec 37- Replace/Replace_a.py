import numpy as np
import pandas as pd
from pandas import Series,DataFrame


ser1=Series([1,2,3,4,1,2,3,4])
print(ser1)
print("="*50)


print(ser1.replace(1,np.nan))
print("="*50)

#replacing selected values
ser1.replace([1,4],[100,400])
print(ser1.replace([1,4],[100,400]))
print("="*50)

#replacing by pasing dictionary
ser1.replace({4:np.nan})
print(ser1.replace({4:np.nan}))
print("="*50)
