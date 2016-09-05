import numpy as np
from pandas import Series,DataFrame
import pandas as pd

json_obj = """
{   "zoo_animal": "Lion",
    "food": ["Meat", "Veggies", "Honey"],
    "fur": "Golden",
    "clothes": null, 
    "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
}
"""

import json

#loading json data
data=json.loads(json_obj)
print(data)


print("="*50)


#converting back to json object
back=json.dumps(data)
print(back)
print("="*50)

#open up json data after opening with data Frame
dframe=DataFrame(data["diet"])
print(dframe)
print("="*50)
