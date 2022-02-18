#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# # Dimensionality and Compatibility
# 
# The dimensional analysis of a quantity, no matter the form, can be performed invoking the method `pyunitwizard.dimensionality()`:

# In[2]:


import pyunitwizard as puw
puw.configure.load_library(['pint', 'openmm.unit'])


# In[3]:


q = puw.quantity(1.4, 'kJ/mol', form='openmm.unit')
puw.get_dimensionality(q)


# Let's see a second example:

# In[4]:


q = puw.quantity('3.5N/(2.0nm**2)')
puw.get_dimensionality(q)


# Where dimensions correspond to the following fundamental quantities:

# 
# | Fundamental Quantity | Dimension |
# | -------------------- | --------- |
# | Length | [L] |
# | Mass | [M] |
# | Time | [T] |
# | Temperature | [K] |
# | Substance | [mol] |
# | Electric Current | [A] |
# | Luminous Intensity | [Cd] |
# 

# In addition, PyUnitWizard can check the dimensional compatibility between quantities with `pyunitwizard.compatibility()`, again, regardless their pythonic form:

# In[5]:


q1 = puw.quantity(1.0, 'meter', form='openmm.unit')
q2 = puw.quantity(1.0, 'centimeter', form='openmm.unit')

puw.compatibility(q1, q2)


# In[6]:


q1 = puw.quantity(1.0, 'kJ/mol', form='openmm.unit')
q2 = puw.quantity(1.0, 'kcal/mol', form='pint')

puw.compatibility(q1, q2)


# In[7]:


q1 = puw.quantity(1.0, 'nm**3', form='pint')
q2 = puw.quantity(1.0, 'litre', form='pint')

puw.compatibility(q1, q2)


# In[8]:


q1 = puw.quantity(1.0, 'nm**3', form='pint')
q2 = puw.quantity(1.0, 'ps', form='openmm.unit')

puw.compatibility(q1, q2)


# In[9]:


q1 = puw.quantity(1.0, 'degrees', form='pint')
q2 = puw.quantity(1.0, 'radians', form='pint')

puw.compatibility(q1, q2)


# In[10]:


q1 = puw.quantity(1.0, 'degrees', form='openmm.unit')
q2 = puw.quantity(1.0, 'hertzs', form='pint')

puw.compatibility(q1, q2)


# In[ ]:




