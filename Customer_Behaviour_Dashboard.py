#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("customer_shopping_behavior.csv")


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df.describe(include='all')


# In[10]:


df.isnull().sum()


# In[11]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


# In[12]:


df.isnull().sum()


# In[13]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')


# In[14]:


df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})


# In[15]:


#create column
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)


# In[16]:


df[['age', 'age_group']].head(10)


# In[17]:


# create new column purchase_frequency_days

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[18]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[19]:


df[['discount_applied','promo_code_used']].head(10)


# In[20]:


(df['discount_applied'] == df['promo_code_used']).all()


# In[21]:


df = df.drop('promo_code_used', axis=1)


# In[22]:


df.columns


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




