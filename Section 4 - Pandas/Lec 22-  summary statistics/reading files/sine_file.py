import numpy as np

x=[i for i in range(1001) if i%2!=0]

y=np.sin(x)



filehand=open("sine.txt","w")
header="x\tsin(x)\n"
filehand.write(header)
for row in range(len(x)):
    data=str(x[row])+"\t"+str(y[row])+"\n"
    filehand.write(data)

filehand.close()
print("done...")
