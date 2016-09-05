from pandas import DataFrame
import numpy as np

data={"City":["SF","LA","NYC"],"Population":[837000,3880000,8400000]}
city_frame=DataFrame(data)
print(city_frame)

print("="*50)

#printing columns name
print(city_frame.columns) #prints name of index of column
print("="*50)

#printing a index column
print(city_frame["Population"])
print("="*50)

#printing first 3 row
print(city_frame.head(3))
print("="*50)
#printing last two row
print(city_frame.tail(2))
print("="*50)


#printing row of a data frame
print(city_frame.ix[2]) #print third row
print("="*50)

#adding new column
#city_frame["Stadium"]=np.array(["Manchester","Liverpool","Chelsea"])
city_frame["Stadium"]=["Manchester","Liverpool","Chelsea"]
#note both passing list of values and array works
print(city_frame)
print("="*50)

import webbrowser
website="http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html"
webbrowser.open(website)

