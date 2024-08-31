#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[10]:


df=pd.read_csv("empdata.csv")


# In[11]:


# df.info will display all the data
df.info()


# In[15]:


# df.head will display only the first 5 rows  from start
df.head()


# In[ ]:





# In[16]:


#df.head(2) will display the first two rows in the output
df.head(2)


# In[19]:


#df.tail(2) will display last two rows
df.tail(2)


# In[21]:


df.shape  # it will display the  no of rows and columns


# In[26]:


df1.shape


# In[ ]:





# In[ ]:





# In[22]:


df.columns


# In[25]:


# gnerating all the empid  fromm start
df.Empid


# In[27]:


# the data which was already there ,we are appeding the same data again after row 6th
df1=df.append(df)
print("dimensions of the original frame ",df.shape) # since we have appended 6 more data set thatswhy the no of rows comming are 12
print("dimensions of the frame with duplicates",df1.shape)


# In[29]:


# remove the duplicates
df1=df1.drop_duplicates()  # here we have removed the dupliate  dataset so it is comming as only 6 rows and 4 columns
print("dimensions of the frame after removing the duplicates",df1.shape)

