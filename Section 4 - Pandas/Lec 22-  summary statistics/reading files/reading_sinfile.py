import csv
import matplotlib.pyplot as plt
import numpy as np

##with open("sine.csv","r") as csvfile:
##    fileobj=csv.reader(csvfile,delimiter=",")
##    x=list()
##    y=list()
##    for row in fileobj:
##        try:
##            x_val=float(row[0])
##            y_val=float(row[1])
##            x.append(x_val)
##            y.append(y_val)
##        except:
##            continue
##
##print(x[:15])
##print(y[:15])
##
##
##plt.plot(x,y,label="sinx")
##plt.legend()
##plt.title("Sin(x)")
##plt.xlabel("x")
##plt.ylabel("y")
##plt.show()
##


x=np.linspace(0,(2*np.pi),1000)
y=np.sin(x)
plt.plot(x,y)
plt.grid()
plt.show()

