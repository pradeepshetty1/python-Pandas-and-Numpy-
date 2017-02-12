import pandas as pd

s = pd.Series(list('abcde'))

print s

ss = pd.Series(list('abcdeio'), index=['v','nv','nv','nv','v','v','v'])

print ss

print ss['v']

print ss['nv']

print ss[2:]

print '$$$$$$$$$$$$$$$$$'
# second value from the values having index as v
print ss['v'][1]

print '~~~~~~~~~~~~~~~~~~~~~~'
sss = pd.Series(range(5),index=list('abcde'))

print sss


ssss = pd.Series({'v':'v','a':'v','r':'nv','u':'v','n':'nv'})

print ssss

print '#################################'

testd1 = {'v':1,'a':2,'r':3,'u':4,'n':5,'a':6}

seriesd1 = pd.Series(testd1,index=list('aeiou'))

print seriesd1

print seriesd1*2


print seriesd1**2
