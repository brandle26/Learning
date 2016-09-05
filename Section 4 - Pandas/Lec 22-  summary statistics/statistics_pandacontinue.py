import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt

import pandas.io.data as pdweb

import datetime
prices=pdweb.get_data_yahoo(["CVX","XOM","BP"],start=datetime.datetime(2010,1,1),
                            end=datetime.datetime(2013,1,1))["Adj Close"]
print(prices.head())
print("="*50)

volume=pdweb.get_data_yahoo(["CVX","XOM","BP"],start=datetime.datetime(2010,1,1),
                            end=datetime.datetime(2013,1,1))["Volume"]
print(volume.head())
print("="*50)

rets=prices.pct_change() #call percentage change

#get correlation
corr=rets.corr

#plotting it

prices.plot()
plt.show()

import seaborn as sns
sns.corrplot(rets,annot=False,diag_names=False)

plt.show()

ser1=Series("w"."w"."x","y","z","w","x","y","x","a")
print(ser1)
ser1.unique()
ser1.calue_counts()
