import numpy as np
import pandas as pd
from pandas import DataFrame,Series

dframe=DataFrame({"city":["ALma","Brian Head","Fox Park"],
              "altitude":[3158,3000,2762]})

print(dframe)
print("="*50)

site_map={"Alma":"Colorade","Brian Head":"Utah","Fox Park":"Wyoming"}

dframe["state"]=dframe["city"].map(site_map)

print(dframe)
