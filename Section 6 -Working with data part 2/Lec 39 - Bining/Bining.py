import numpy as np
from pandas import DataFrame,Series
import pandas as pd

years=[1998,1991,1992,2008,2012,2015,1987,1969,2013,2008,1999]

decade_bins=[1960,1970,1980,1990,2000,2010,2020]

decade_cat=pd.cut(years,decade_bins)
print(decade_cat)

print(decade_cat.categories)
print("="*50)

print(pd.value_counts(decade_cat))
print("="*50)

pd.cut(years,2,precision=1)
print(pd.cut(years,2,precision=1))
