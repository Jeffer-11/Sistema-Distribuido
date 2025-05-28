#!/usr/bin/env python3
import pandas as pd

ser = pd.Series(data=[1, 2, 3, 4, 5], index=['tom', 'bob', 'rob', 'ed', 'vik'])

print(ser.index)


print('fabian' in ser)
print('before')
print(ser)
print('after')
print(ser*2)
print('power into 2')
print(ser**2)


ser = pd.Series(data=[100, 200, 300, 400, 500], index=['tom', 'bob', 'rob', 'ed', 'vik'])

print(ser[[2,4]])
print(ser[['tom']])

# PANDAS DATAFRAME
print('PANDAS DATAFRAME')

df = pd.DataFrame({
    'one': pd.Series(data=[100, 200, 300], index=['apple', 'ball', 'clock']),
    'two': pd.Series(data=[100, 200, 300], index=['apple', 'ball', 'clock'])
})
print('----------------------------------------------')
df1=pd.DataFrame(df)
print(df)
print('Index : {}',format(df1.index))
print('----------------------------------------------')
print(df.columns)
df1['three']=df1['one']*df1['two']
print(df1)
print('----------------------------------------------')
df1['flag']=df1['one']>100
print(df1)
print('----------------------------------------------')
aux=df1.pop('three')
print(df1)
print('----------------------------------------------')
del df1['one']
print(df1)
print('----------------------------------------------')
df1.insert(2,'copia de dos',df1['two'])
print(df1)
print('----------------------------------------------')
df1['flag two']=df1['copia de dos']>200
aux2=df1.pop('copia de dos')
print(df1)
print('----------------------------------------------')
df1['twoupperhalf']=df1['two'][:2]
print(df1)
print('----------------------------------------------')
df1['twodonwhalf']=df1['two'][2:]
print(df1)


import pandas as pd

print('Reading CSV file into DataFrame')
movies = pd.read_csv('movies.csv')
print(movies.head())