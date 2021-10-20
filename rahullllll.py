#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sb
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
from datetime import date


# In[2]:


# Importing data

df = pd.read_csv('/Users/poojithareddy/Library/Containers/com.microsoft.Excel/Data/Downloads/Fraud_Data.csv')
df.head(10)


# In[3]:


df.describe()


# In[4]:


df.dtypes


# In[5]:


# checking for missing values

df.isnull().sum()


# In[ ]:


# So there are no missing values


# In[6]:


# Descriptive analysis

# Fraud cases out of total population

fraud_val = df.is_fraud.value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(fraud_val.values, labels=fraud_val.index, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[7]:


# So less than 10 % are values are fraud
# Creating new column

df['signup_time'] = pd.to_datetime(df['signup_time'])
df['purchase_time'] = pd.to_datetime(df['purchase_time'])
df['timediff']=(df['purchase_time']-df['signup_time']).astype('timedelta64[m]')
df['timediff'].head(10)


# In[8]:


sb.distplot(df[df['is_fraud']==1]['timediff'],bins=50, kde = False)
sb.distplot(df[df['is_fraud']==0]['timediff'],bins=50, kde = False)


# In[9]:


# Clearly, transactions with a small difference between signup time and transaction time are fraud transactions
# Lets look at purchase value now

sb.distplot(df[df['is_fraud']==1]['purchase_value'],bins=50)
sb.distplot(df[df['is_fraud']==0]['purchase_value'],bins=50)


# In[10]:


# Purchase value seems to be very similar for both fraud and non-fraud
# Lets look at age now

sb.distplot(df[df['is_fraud']==1]['age'],bins=50)
sb.distplot(df[df['is_fraud']==0]['age'],bins=50)


# In[11]:


# Age distribution appears to be similar as well with outliers in non-fraud but not in fraud which is weird
# Looking at the data again

df.head(10)


# In[12]:


# Intializing the modeling process

# Dropping unnecessary columns

df2=df.drop(['user_id', 'signup_time','purchase_time','device_id','ip_address'], axis=1)
df2.head(10)


# In[13]:


# Encoding categorical variables

def encoding(df2):
    for column in df2.columns[df2.columns.isin(['source','browser','sex'])]:
        df2[column]=df2[column].factorize()[0]
    return df2

df3 = encoding(df2)


# In[14]:


df3.head(10)


# In[ ]:




