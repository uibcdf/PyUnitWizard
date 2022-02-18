#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# # Convert quantities
# *Quantities can be converted into other form and units with PyUnitWizard.*
# 
# To facilitate the conversion of units between different forms, PyUnitWizard includes the method `pyunitwizard.convert()`. This way quantities and units can be converted between different forms and units:

# In[2]:


import pyunitwizard as puw


# In[3]:


puw.configure.load_library(['pint', 'openmm.unit'])


# In[4]:


q = puw.quantity(value=3.0, unit='joules', form='openmm.unit')


# In[5]:


q2 = puw.convert(q, to_unit='kilocalories', to_form='pint')


# In[6]:


q2


# If the output form is not specified with the argument `to_form`, a quantity with the same form is obtained:

# In[7]:


q = puw.quantity(value=1000.0, unit='kN/m**2', form='pint')


# In[8]:


q2 = puw.convert(q, to_unit='atmospheres')


# In[9]:


q2


# In[10]:


puw.get_form(q2)


# In[ ]:




