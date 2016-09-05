import numpy as np
import pandas as pd
from pandas import Series,DataFrame

ser1=Series([0,1,2],index=["A","B","C"])
print(ser1)
print("="*50)

ser2=Series([3,4,5,6],index=["A","B","C","D"])
print(ser2)
print("="*50)

print(ser1+ser2)

print("="*50)
dframe1=DataFrame(np.arange(4).reshape((2,2)),columns=list("AB"),index=["NYC","LA"])
print(dframe1)
print("="*50)

dframe2=DataFrame(np.arange(9).reshape((3,3)),columns=list("ADC"),index=["NYC","SF","LA"])
print(dframe2)
print("="*50)

print(dframe1+dframe2)
print("="*50)

#use add function
print(dframe1.add(dframe2,fill_value=0))
print("="*50)

print(dframe2)
print("="*50)

ser3=dframe2.ix[0]
print(ser3)
print("="*50)

#subrractin
print(dframe2-ser3)
"="*50







            
