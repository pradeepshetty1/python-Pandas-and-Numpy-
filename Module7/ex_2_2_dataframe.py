import pandas as pd

data = {'Country':['US','US','INDIA','INDIA'],
        'Year':[2012,2013,2012,2013],
        'Population':[20,27,30,35]
}

mydataFrame = pd.DataFrame(data)
print mydataFrame
