import pandas as pd

mydf = pd.read_csv('sample-supplier.csv')

print mydf.irow(2)

v308531 = mydf[mydf['Vendor Nbr'] == 308531]

print 'dataframe where Vendor Nbr == 308531'

print v308531

print v308531.describe()