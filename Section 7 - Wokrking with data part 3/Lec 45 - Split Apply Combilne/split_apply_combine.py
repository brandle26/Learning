import numpy as np
import pandas as pd
from pandas import Series,DataFrame

dframe_wine=pd.read_csv("winequality-red.csv",sep=";")

print(dframe_wine.head())

def ranker(df):
    df["alc_content_rank"]=np.arange(len(df))+1
    return df

dframe_wine.sort("alcohol",ascending=False,inplace=True)

dframe_wine=dframe_wine.groupby("quality").apply(ranker)
print(dframe_wine)


num_of_qual=dframe_wine["quality"].value_counts()

