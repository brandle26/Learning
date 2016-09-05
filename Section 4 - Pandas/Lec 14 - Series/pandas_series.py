import numpy as np

import pandas as pd

from pandas import Series, DataFrame

obj=Series([3,6,9,12])

print(obj)
#see only values or index
print("="*50)
print(obj.values)
print("="*50)
print(obj.index)

ww2_cas=Series([8700000,4300000,3000000,2100000,400000],index=["USSR","Germany","China","Japan","USA"])
print(ww2_cas)
#now we can use the country name as index to see the casulaties of the country
#as follows
print("="*50)
print(ww2_cas["USA"])
print("="*50)
#check which countries has casulaties greater than 4 million
morethan=ww2_cas[ww2_cas>4000000]
print(morethan)
print("="*50)
#checking if the index is in the series
print("USSR" in ww2_cas)
print("="*50)

#Series behaves like a dictionary and can be converted to dictionary
ww2_dict=ww2_cas.to_dict()

print(ww2_dict)
print("="*50)
#can also convert dictionary to series
ww2_series=Series(ww2_dict)
print(ww2_series)
print("="*50)

countries=["China","Germany","Japan","USA","USSR","Argentina"]
obj2=Series(ww2_dict,index=countries)
print(obj2)
print("="*50)

#panda has method to find null
#they are isnull() and notnull()
#is null returns true if the value of the index is null and not null returns
#true if the value of the index is not null
print(pd.isnull(obj2))
print("="*50)
print(pd.notnull(obj2))
print("="*50)

print(obj2)
print(ww2_series)
print(obj2+ww2_series)
print("="*50)

#naming the series
obj2.name="World War 2 Casualties"
print(obj2)

#can alsow name the index
obj2.index.name="Countries"
print(obj2)
print("="*50)
