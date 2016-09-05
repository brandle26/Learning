import pandas as pd
import numpy as np
from pandas import Series,DataFrame

dframe1=DataFrame(np.arange(8).reshape(2,4),
                  index=pd.Index(["LA","SF"],name="city"),
                  columns=pd.Index(["A","B","C","D"],name="Letters"))

print(dframe1)
print("="*50)

dframe_st=dframe1.stack()
print(dframe_st)
print("="*50)

#unstack
print(dframe_st.unstack())
print("="*50)

print(dframe_st.unstack("Letters"))
print("="*50)

print(dframe_st.unstack("city"))
print("="*50)

ser1=Series([0,1,2],index=["Q","X","Y"])

ser2=Series([4,5,6],index=["X","Y","Z"])

dframe=pd.concat([ser1,ser2],keys=["Alpha","Beta"])

print(dframe.unstack())
print("="*50)

print(dframe.unstack().stack())
print("="*50)

dframe=dframe.unstack()

print(dframe.stack())
print("="*50)


print(dframe.stack(dropna=False))
print("="*50)
