# -*- coding: utf-8 -*-
"""Multiple LR (ML-2)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1InFB4RjI0SWd4A2cVzZWpBYhYgtbe-2f

#Multiple Regression
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import sklearn

df=pd.read_csv('/content/50_Startups.csv - 50_Startups.csv.csv')

df.head() #tail(last 5 rows)

df.info()

df.keys()

plt.figure(figsize=(8,8),dpi=60)
sns.barplot('Administration','Profit',data=df)
plt.xticks(rotation=90)

plt.figure(figsize=(6,6),dpi=50)
sns.barplot('State','Profit',data=df)

sns.lineplot(x='R&D Spend',y='Profit',data=df)

sns.scatterplot(x='R&D Spend',y='Profit',data=df)

df.duplicated().sum()

df.isnull().sum()

df.describe()

df1=pd.get_dummies(df['State'])

df1.head()

df.drop('State',inplace=True,axis=1)

df.head()

df2=pd.concat([df1,df],axis=1)

df2.head()

x=df2.iloc[:,:-1]  #independent variable
y=df2.iloc[:,-1]   #dependent variable

x.head()

y.head()

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=5)

print(xtrain.shape)
print(ytrain.shape)
print(xtest.shape)
print(ytest.shape)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(xtrain,ytrain)

lr.coef_

lr.intercept_

print('score on training data:',lr.score(xtrain,ytrain))
print('score on testing data:',lr.score(xtest,ytest))

plt.figure(figsize=(8,8),dpi=50)
plt.plot(ytrain,'o',color='blue',label='y-training data')
plt.plot(ytest,'o',color='green',label='y-testing data')
plt.plot(lr.predict(xtrain),color='red',label='predicted values')
plt.legend()

plt.figure(figsize=(8,8),dpi=50)
plt.plot(xtrain,'o',color='blue',label='x-training data')
plt.plot(xtest,'o',color='green',label='x-testing data')
plt.plot(lr.predict(xtrain),color='red',label='predicted values')
plt.legend()

#plt.plot(xtrain,'o',color='black')
plt.plot(ytrain,color='green')
plt.plot(lr.predict(xtrain),color='blue')

plt.plot(y)
plt.plot(lr.predict(x))

plt.plot(ytrain,'o',color='green')
plt.plot(ytest,'o',color='red')
plt.plot(lr.predict(xtest),'o',color='blue')

data=pd.DataFrame()
data['Actual values']=ytest
data['predicted values']=lr.predict(xtest)
data

df6=lr.predict(xtest)
df6