import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe=DataFrame({"k1":["X","X","Y","Y","Z"],
                  "k2":["alpha","beta","alpha","beta","alpha"],
                  "dataset1":np.random.randn(5),
                  "dataset2":np.random.randn(5)})

#create a group
group1=dframe["dataset1"].groupby(dframe["k1"])
print(group1)

#finding the mean of teh group just created
print(group1.mean())

cities=np.array(["NY","LA","LA","NY","NY"])

month=np.array(["JAN","FEB","JAN","FEB","JAN"])

dframe["dataset1"].groupby([cities,month]).mean()

print(dframe.groupby("k1").mean())

#can do groupby with multibple keys
print(dframe.groupby(["k1","k2"]).mean())

#asking for size of the groupby
print(dframe.groupby(["k1"]).size())

#can iterate over grupys
for name,group in dframe.groupby("k1"):
    print("This is the %s group"%name)
    print(group)
    print("\n")
    

#iterating for multiple keys]
#iterating for multiple keys]
for (k1,k2), group in dframe.groupby(["k1","k2"]):
    print("Key1 = %s Key2=%s"%(k1,k2))
    print(group)
    print("\n")

group_dict=dict(list(dframe.groupby("k1")))
print(group_dict["X"])

#seperating by datatypes
group_dict_axis1=dict(list(dframe.groupby(dframe.dtypes,axis=1)))
print(group_dict_axis1)

#group by columns
dataset2_group=dframe.groupby(["k1","k2"])[["dataset2"]]
print(dataset2_group.mean())
