import pandas as pd
import numpy as np
from pandas import Series,DataFrame

from io import StringIO

data="""\
Sample Animal Intelligence
1 Dog Smart
2 Dog Smart
3 Cat Dumb
4 Cat Dumb
5 Dog Dumb
6 Cat Smart"""

dframe=pd.read_table(StringIO(data),sep="\s+")

print(dframe)
print("="*50)


pd.crosstab(dframe.Animal,dframe.Intelligence,margins=True)
