import pandas as pd
import numpy as np

data = {'Country':['US','US','INDIA','INDIA'],
        'Year':[2012,2013,2012,2013],
        'Population':[20,27,30,35]
}

mydataFrame = pd.DataFrame(data)
print mydataFrame

print mydataFrame['Country']

print '############################'
np.random.seed(5)
mydf = pd.DataFrame(np.random.randint(100, size=(100, 6)), columns = list("ABCDEF"), index = ["R" + str(i) for i in range(100)])
print mydf.head()

print 'describe :',mydf.describe()

print 'only column A :',mydf['A']

print 'ix attribute :',mydf.ix['R10':'R20']

print 'ix attribute :',mydf.ix['R10']

