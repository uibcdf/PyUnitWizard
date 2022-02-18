#!/usr/bin/env python
# coding: utf-8

# # Similarity

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# In[2]:


import pyunitwizard as puw


# In[3]:


puw.configure.load_library(['openmm.unit'])


# In[4]:


puw.similarity('1 meter', '1 meter')


# In[5]:


puw.similarity('1 meter', '1 centimeter')


# In[6]:


puw.similarity('1 meter', '1.1 meter')


# In[7]:


puw.configure.reset()
puw.configure.load_library(['pint','openmm.unit'])


# In[8]:


aa = puw.quantity(0.4,'cm')
bb = puw.quantity(0.4,'cm')
puw.similarity(aa,bb)


# In[9]:


aa = puw.quantity(4,'mm')
bb = puw.quantity(0.4,'cm')
puw.similarity(aa,bb)


# In[10]:


aa = puw.quantity(4,'mm', form='pint')
bb = puw.quantity(0.4,'cm', form='openmm.unit')
puw.similarity(aa,bb)


# In[11]:


aa = puw.quantity(4,'mm', form='pint')
bb = puw.quantity(0.41,'cm', form='openmm.unit')
puw.similarity(aa,bb)


# In[ ]:




