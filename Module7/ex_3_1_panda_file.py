import pandas as pd

mydf = pd.read_csv('sample-supplier.csv')
#print mydf

print mydf.describe()

#SKU is not numerical. so describe doesn't list
print mydf.tail(3)

print mydf.columns

print len(mydf)

print mydf["SKU"]

print mydf[["SKU","LEAD 1","LEAD 2"]]