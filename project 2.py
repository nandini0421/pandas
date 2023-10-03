#!/usr/bin/env python
# coding: utf-8

# # Creating Data Frame

# In[2]:


import pandas as pd


# In[3]:


list1 = ["Kunal", "Nandini","Vanshika","Nitya"]
df = pd.DataFrame(list1)

age = [25, 23 , 22, 8]

location = ["Jabalpur", "Jabalpur", "Sagar", "Jabalpur"]
#create a new column in existing dataframe
df['Age'] = age 
df['Location'] = location

#to rename the column name
df.rename(columns = {"Location": "Home-town"}, inplace = True)

df


# In[4]:


df = pd.read_csv("drug200.csv")
#print first 5 rows
df.head()


# In[5]:


#print last 5 rows
df.tail()


# In[6]:


#print number of columns

df.shape


# In[7]:


#print name of columns
df.columns


# In[8]:


#only numerical column
df.describe()


# In[ ]:




