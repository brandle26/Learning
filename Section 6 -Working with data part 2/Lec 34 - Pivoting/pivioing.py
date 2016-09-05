import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# Lets create some data to play with:

# Note: It is not necessary to understand how this dataset was made to understand this Lecture.

#import pandas testing utility
import pandas.util.testing as tm; tm.N = 3

#Create a unpivoted function
def unpivot(frame):
    N, K = frame.shape
    
    data = {'value' : frame.values.ravel('F'),
            'variable' : np.asarray(frame.columns).repeat(N),
            'date' : np.tile(np.asarray(frame.index), K)}
    
    # Return the DataFrame
    return DataFrame(data, columns=['date', 'variable', 'value'])

#Set the DataFrame we'll be using
dframe = unpivot(tm.makeTimeDataFrame())

print(dframe)
print("="*50)

#to pivot use dframename.pivot("row","column","fill values")
dframe_piv=dframe.pivot("date","variable","value")
print(dframe_piv)
