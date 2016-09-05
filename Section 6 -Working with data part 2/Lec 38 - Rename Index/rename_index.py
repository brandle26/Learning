import numpy as np
import pandas as pd
from pandas import Series,DataFrame

dframe=DataFrame(np.arange(12).reshape(3,4),
                 index=["NY","LA","SF"],
            columns=["A","B","C","D"])

print(dframe)
print("="*50)

dframe.index.map(str.lower)
print(dframe.index.map(str.lower))
print(dframe)
print("="*50)

dframe.index=dframe.index.map(str.lower)
print(dframe)
print("="*50)

dframe.rename(index=str.title,columns=str.lower)
print(dframe.rename(index=str.title,columns=str.lower))
print("="*50)

dframe.rename(index={"ny":"NEW YORK"},
              columns={"A":"ALPHA"})
print(dframe.rename(index={"ny":"NEW YORK"},
              columns={"A":"ALPHA"}))
print("="*50)

#makeing the change permanent
dframe.rename(index={"ny":"NEW YORK"},
              columns={"A":"ALPHA"},inplace=True)
print(dframe)
