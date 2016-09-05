import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from scipy import stats

import matplotlib.pyplot as plt
import matplotlib as mlb
import seaborn as sns

flight_dframe=sns.load_dataset("flights")
flight_dframe=flight_dframe.pivot("month","year","passengers")
sns.heatmap(flight_dframe)
plt.show()

fig,(axis1,axis2)=plt.subplots(2,1)
plt.show()
