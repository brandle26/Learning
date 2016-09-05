import numpy as np
import pandas as pd
from pandas import Series,DataFrame

ser1=Series([2,np.nan,4,np.nan,6,np.nan],
           index=["Q","R","S","T","U","V"])

ser2=Series(np.arange(len(ser1)),dtype=np.float64,
           index=["Q","R","S","T","U","V"])

a=Series(np.where(pd.isnull(ser1),ser2,ser1),index=ser1.index)
print(a)
print("="*50)

ser1.combine_first(ser2)
print(ser1.combine_first(ser2))
print("="*50)

nan=np.nan
dframe_odds=DataFrame({"X":[1.,nan,3.,nan],
                      "Y":[nan,5.,nan,7.],
                      "Z":[nan,9.,nan,11]})

dframe_even=DataFrame({"X":[2.,4.,nan,6.,8.],
                      "Y":[nan,10.,12.,14.,16.]})


print(dframe_odds.combine_first(dframe_even))
print("="*50)


