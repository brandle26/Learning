import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe=DataFrame(np.arange(16).reshape(4,4))

blender=np.random.permutation(4)

print(blender)
print("="*50)

print(dframe)
print("="*50)

#take dataframe and use blender to put then in that order
#i order to do permuattion using the blender as index order
dframe.take(blender)
print(dframe.take(blender))
print("="*50)

#permutation with replace
box=np.array([1,2,3])

#cam ise ramdint with argument to do permuation with replacment
shaker=np.random.randint(0,len(box),size=10)
print(shaker)

hand_grabs=box.take(shaker)

print(hand_grabs)
