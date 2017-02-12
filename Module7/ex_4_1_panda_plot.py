import pandas as pd
from pylab import *

mydf = pd.read_csv('sample-supplier.csv')

mydf['Vendor Nbr'].hist()

show()