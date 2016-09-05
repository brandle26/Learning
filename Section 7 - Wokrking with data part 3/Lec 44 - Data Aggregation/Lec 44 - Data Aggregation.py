import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

url="http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/"

dframe_wine=pd.read_csv("winequality-red.csv",sep=";")

print(dframe_wine.head())

#calculate average
print("="*50)
print(dframe_wine["alcohol"].mean())

print("="*50)

def max_to_min(arr):
    return arr.max()-arr.min()

wino=dframe_wine.groupby("quality")
print(wino.describe())
print("="*50)

wino.agg(max_to_min)
print(wino.agg(max_to_min))
print("="*50)

print(wino.agg("mean"))
print("="*50)

print(dframe_wine.head())

dframe_wine["qual/alc ratio"]=dframe_wine["quality"]/dframe_wine["alcohol"]
print(dframe_wine.head())
piv=dframe_wine.pivot_table(index=["quality"])
print(piv)

dframe_wine.plot(kind="scatter",x="quality",y="alcohol")
plt.show()
