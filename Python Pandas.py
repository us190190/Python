# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 18:16:26 2018

@author: Manoj.Prabhakar
"""

import numpy as np
import pandas as pd
from numpy.random import randn
import os

# Series

labels = ['a','b','d','e']
data = [10,30,50,70]
ar = np.array(data)
d={'a':10,'b':30,'c':50,'d':70}

pd.Series(data=data)

pd.Series(data=data,index=labels)

pd.Series(data,labels)

pd.Series(d)

series1 = pd.Series([1,2,3,4],['India','Afghanistan','China','Pakistan'])

series2 = pd.Series([1,2,7,4],['India','Afghanistan','Bangladesh','Pakistan'])

series1['India']

series3 = pd.Series(data=labels)

series3[0]

series2[2]

series1+series2

# DataFrame - Pandas series object with an index

np.random.seed(1000)

df=pd.DataFrame(randn(5,3),['A','B','C','D','E'],['W','X','Y'])

df['W']

type(df['W'])

type(df)

df[['W','X']]

df['new'] = df['W']+df['Y']

df

df.drop('new',axis=1,inplace=True) # axis = 0 means the row and axis = 1 means column, inplace = True - for changes to occur

df.drop('E')

df.shape # 5 denotes the number of rows and 3 denotes the number of columns

# Access rows

df.loc['A'] 

df.iloc[0]

df.loc['A','Y']

df.loc[['A','B'],['W','X']]

# Conditional Selection

df1 = df>0

df[df1>0]

df

# Filtering rows - Selecting only those rows which are Not NA's

df[df['X']>0]

# Multiple Conditions

df[(df['W']>0) & (df['X']<1)] # And Operator

df[(df['W']>0) | (df['X']<1)] # Or Operator

newst = 'CA NA NR OS MA'.split()

df['States'] = newst

df

# Mising Data

d = ({'A':[1,2,np.nan],'B':[6,np.nan,np.nan],'C':[1,4,5]})

df = pd.DataFrame(d)

df

df.dropna() # For Rows

df.dropna(axis=1) # For Columns

df.dropna(thresh=2) # Remove those columns which has atleast 2 missing values

df['A'].fillna(value=df['A'].mean())

# Group BY

data = {'Company':['Goog','MSFT','ABINB','DMART','TCS','TCS'],
        'Person':['Ra','Ma','Ta','Ka','Ga','Fa'],
        'Sales': [200,1000,100001,232,445,567]}


df = pd.DataFrame(data)

df

r=df.groupby('Company')

r.mean()

r.sum()

r.std()

df.groupby('Company').count()

df.groupby('Company').max()

df.groupby('Company').describe()

# Merging and Concatenating

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

# Similar to Rbind in R 

pd.concat([df1,df2,df3])

# Similar to Cbind in R

pd.concat([df1,df2,df3],axis=1)

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})

pd.merge(left,right,how='inner',on='key')

pd.merge(left, right, how='outer', on=['key1', 'key2'])

pd.merge(left, right, how='right', on=['key1', 'key2'])

pd.merge(left, right, how='left', on=['key1', 'key2'])

# Data Input and Output

os.chdir("E:/PRESENTATION")

df = pd.readc_csv('train.csv',encoding='latin1')

df.to_csv('Output.csv')

df = pd.read_excel('Train and Test.xlsx',sheetname='Train')

df = pd.read_excel('Train and Test.xlsx',sheetname='Test')

df.to_excel('Output.xlsx',sheet_name='Sheet1')

df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
