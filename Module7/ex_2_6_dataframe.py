import pandas as pd


data = {'Country':['US','US','INDIA','INDIA'],
        'Year':[2012,2013,2012,2013],
        'Population':[20,27,30,35]
}

mydataFrame = pd.DataFrame(data)
print mydataFrame

mydataFrame['newColumn']=mydataFrame['Population']*2
print mydataFrame

anotherdf = pd.Series(['Hadoop','Python','NoSQL'],index=[1,3,5])
print '###############################'

print anotherdf

print anotherdf.reindex(range(8))

print anotherdf.reindex(range(8),fill_value='New Course')
print anotherdf.reindex(range(8),method='ffill')
print anotherdf.reindex(range(8),method='bfill')
print anotherdf.reindex(range(8),method='bfill',fill_value='default_course')

