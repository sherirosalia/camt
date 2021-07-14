import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import datetime


df = pd.read_csv('random_licenses.csv')
# print(df['Effective'])

# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S')

df['Effective'] = df.loc[df['Effective'].notnull(),'Effective'].apply(lambda d: datetime.datetime.strptime(d, '%Y-%m-%dT%H:%M:%S'))
print(df.dtypes)

# print(df.sample(5))
# plt.scatter(df['Effective'], )

#  histogram 
# df['Effective'].hist()
# plt.show()

# df['Effective'].hist(bins=144)
# plt.show()

print(df['Status'].value_counts())

# print(df.loc[df['Effective'].notnull(),'Effective'])

active_df=df.loc[df['Status']=='Active'].copy()

# active_df[(active_df['Effective'] > '2019-4-10') & (active_df['Effective'] <= '2021-4-10')]['Effective'].hist(bins=24)
# plt.show()
inactive_df=df.loc[df['Status']!='Active'].copy()
inactive_df['Effective'].hist(bins=144)
plt.show()