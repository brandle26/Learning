import numpy as np

from pandas import Series, DataFrame

import pandas as pd

my_ser=Series([1,2,3,4],index=["A","B","C","D"])

print(my_ser)

#gettin index from the series
print("="*50)
my_index=my_ser.index
print(my_index)

print("="*50)

#getting a inde
print(my_index[2])
print("="*50)
print(my_index[2:])
print("="*50)

#changing index value
print(my_index[0])
print("="*50)
##my_index[0]="Z" #not mutable and will result in error

print(my_ser["A"])
