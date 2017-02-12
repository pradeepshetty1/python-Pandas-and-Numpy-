import pandas as pd

mydata = {'US':{2012:30,2013:45,2014:33},
          'INDIA':{2012:22,2014:44,2015:55,2013:33}}

mydataFrame = pd.DataFrame(mydata)

#Incomplete data is filled with NaN
print mydataFrame

