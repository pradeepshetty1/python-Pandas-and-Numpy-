import pandas as pd
import numpy as np

raw_data = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
print df_a

raw_data1 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_n = pd.DataFrame(raw_data1, columns = ['subject_id','test_id'])
print df_n

print '~~~~~~~~~~~~~~~~~~~~~~~~~'

mergeddf = pd.merge(df_a, df_n, on='subject_id')

print '##################'

print mergeddf

print '~~~~~~~~~~~~~~~~~~~~~`'

mergeddfright  = pd.merge(df_a, df_n, on='subject_id',how='right')

print mergeddfright
