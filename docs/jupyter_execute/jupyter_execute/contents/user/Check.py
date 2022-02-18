#!/usr/bin/env python
# coding: utf-8

# # Check

# In[1]:


import pyunitwizard as puw


# In[2]:


puw.configure.load_library('pint')


# In[3]:


aa = puw.quantity(1.0,'nm')


# In[4]:


puw.check(aa, value_type=float)


# In[5]:


puw.check(aa, unit='nm')


# In[6]:


puw.check(aa, dimensionality={'[L]':1})


# In[7]:


puw.check(aa, dimensionality={'[L]':1}, value_type=float, unit='nm')


# In[8]:


puw.check(aa, dimensionality={'[L]':1, '[T]':-1}, value_type=float)


# In[9]:


puw.check(aa, dimensionality={'[L]':1}, value_type=float, unit='mm')


# In[10]:


aa = puw.quantity([0,1,2],'nm')


# In[11]:


puw.check(aa, shape=[3])


# In[12]:


puw.check(aa, dimensionality={'[L]':1}, value_type=list, shape=[3])


# In[ ]:




