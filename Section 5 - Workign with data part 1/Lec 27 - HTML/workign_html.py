import pandas as pd
from pandas import Series,DataFrame

from pandas import read_html

url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'

dframe_list=pd.io.html.read_html(url)
dframe=dframe_list[0]
print(dframe)
print("="*50)

#just knowing columns
print(dframe.columns.values)
print("="*50)

print(dframe.index.values)
print("="*50)
