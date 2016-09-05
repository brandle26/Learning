import numpy as np
from pandas import Series, DataFrame
import pandas as pd

ser1=Series(range(3),index=["C","A","B"])
print(ser1)
print("="*50)

#sorting index using sort_index() function
print(ser1.sort_index())
print("="*50)

#sorting series by its value
print(ser1.sort_values())
print("="*50)

from numpy.random import randn

#ranking and sorting values
ser2=Series(randn(10))

print(ser2)
print("="*50)

print(ser2.sort_values())
print("="*50)

print(ser2.rank())


###
ser3=Series(randn(10))
print(ser3.rank())
print(ser3.sort_values().rank())
print(ser3.sort_values())


