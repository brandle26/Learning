#Standard
import numpy as np
import pandas as pd
from numpy.random import randn

#Stats
from scipy import stats

#Plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
url="http://en.wikipedia.org/wiki/Histogram"

dataset1=randn(100)

#plotting histogram from the  dataset
plt.hist(dataset1)
#by default the hist() function create 10 bins 
plt.show()

dataset2=randn(80)
#changing colour
plt.hist(dataset2,color="indianred")
plt.show()

#having two hisgogram at the same plot
#note since dataset1 and 2 has different number of data
#they nedd to be normalise using narmed=True
#the attribute alpha controls transparency
#bins attribute control s the number of bins

plt.hist(dataset1,normed=True,color="indianred",alpha=0.5,bins=20)
plt.hist(dataset2,normed=True,alpha=0.5,bins=20)


data1=randn(1000)
data2=randn(1000)

#using seaborn
sns.jointplot(data1,data2)
plt.show()

#use hex plot
sns.jointplot(data1,data2,kind="hex")
plt.show()
