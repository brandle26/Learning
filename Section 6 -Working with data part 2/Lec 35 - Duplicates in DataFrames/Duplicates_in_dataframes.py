import numpy as np
import pandas as pd
from pandas import Series,DataFrame

dframe=DataFrame({"key1":["A"]*2+["B"]*3,
                 "key2":[2,2,2,3,3]})

print(dframe)

#finding duplicate rows
print("="*50)
print(dframe.duplicated())

#droping duplicates
print("="*50)
print(dframe.drop_duplicates())
print("="*50)

#dropping duplicates from specific keys
dframe.drop_duplicates(["key1"])
print(dframe.drop_duplicates(["key1"]))
print("="*50)

print(dframe)
print("="*50)

#taking last duplicate to drop
print(dframe.drop_duplicates(["key1"],take_last=True))

print(dframe.drop_duplicates(["key1"],keep="last"))
