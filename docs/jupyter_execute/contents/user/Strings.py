#!/usr/bin/env python
# coding: utf-8

# # Working with strings
# *A quantity can be created from a string expression, but not all libraries understand the same syntaxis and vocabulary*
# 
# Some python libraries to work with physical quantities, as pint, are very efficient parsing strings. And some other probably not. And in addition, it is probable that not all of them use the samy syntaxis. With PyUnitWizard a unique parser and syntaxis can be used not matter the desired form of the quantity. Let's show how the methods `pyunitwizard.string_to_quantity()` and `pyunitwizard.string_to_unit()` work:

# In[1]:


import pyunitwizard as puw
puw.configure.load_library(['pint', 'openmm.unit'])
puw.configure.set_default_form('openmm.unit')


# In[2]:


puw.quantity('2 litres + 20 dL')


# In[3]:


puw.convert('2 newtons per square meter', parser='pint')


# In[4]:


puw.quantity('1.5 kcal / mole', parser='pint', form='pint')


# In[5]:


puw.convert('kelvin**(-1)', parser='pint', to_form='pint')


# And the inverse translation can be performed:

# In[6]:


q = puw.convert('2 newtons per square meter', parser='pint', to_form='openmm.unit')


# In[7]:


puw.convert(q, to_form='string')


# In[8]:


u = puw.convert('kelvin**(-1)', to_type='unit')


# In[9]:


u


# In[10]:


puw.convert(u, to_form='string')


# In[ ]:




