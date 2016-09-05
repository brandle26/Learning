import numpy as np
import pandas as pd
from pandas import Series,DataFrame

animals=DataFrame(np.arange(16).reshape(4,4),
                  columns=["W","X","Y","Z"],
                  index=["Dog","Cat","Bird","Mouse"])

print(animals)
print("="*50)


animals.ix[1:2,["W","Y"]]=np.nan

print(animals)
print("="*50)

behavior_map={"W":"good","X":"bad","Y":"good","Z":"bad"}

animal_col=animals.groupby(behavior_map,axis=1)

print(animal_col.sum())
print("="*50)

behave_series=Series(behavior_map)

print(behave_series)
print("="*50)

print(animals.groupby(behave_series,axis=1).count())
print("="*50)

print(animals)
print("="*50)

#grouping by length of animals name
print(animals.groupby(len).sum())
print("="*50)

keys=["A","B","A","B"]
print(animals.groupby([len,keys]).max())
print("="*50)

hier_col=pd.MultiIndex.from_arrays([["NY","NY","NY","SF","SF"],[1,2,3,1,2]],names=["City","sub_value"])

dframe_hr=DataFrame(np.arange(25).reshape(5,5),columns=hier_col)

dframe_hr=dframe_hr*100

print(dframe_hr)

print("="*50)


