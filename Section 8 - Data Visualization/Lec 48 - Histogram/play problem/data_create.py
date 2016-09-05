import random
import numpy as np

a=list()

for i in range(100):
    a.append(random.randrange(100,201))


filehand=open("raw_data.txt","w")

for num in a:
    data=str(num)+"\n"
    filehand.write(data)

filehand.close()

print("done...")
      
