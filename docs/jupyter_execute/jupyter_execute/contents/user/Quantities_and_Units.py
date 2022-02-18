#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# # Quantities and Units
# *-PyUnitWizard provides with a unique simple API to work with quantities and units with different pythonic forms-*
# 
# Since there are many libraries to work with physical quantities, the same quantity can be stored as different python objects, or in the language of PyUniWizard, with different forms, thanks to the method `pyunitwizard.quantity()`:

# In[2]:


import pyunitwizard as puw
import numpy as np

puw.configure.load_library(['pint', 'openmm.unit'])


# In[3]:


puw.configure.get_default_parser()


# In[4]:


q = puw.quantity(value=3.0, unit='joules', form='openmm.unit')


# The form name of a quantity variable can be obtained with the method `pyunitwizard.get_form()`:

# In[5]:


puw.get_form(q)


# And the value and unit of a quantity can be obtained with `pyunitwizard.get_value()` and `pyunitwizard.get_unit()`:

# In[6]:


puw.get_value(q)


# In[7]:


puw._kernel.default_parser


# In[8]:


puw.get_unit(q)


# Let's see other examples of how to use `pyunitwizard.quantity()` to make quantities:

# In[9]:


q = puw.quantity([0,1,2], 'angstroms', form='pint')
q


# In[10]:


q = puw.quantity(np.zeros(shape=[2,6,3]), 'nm/ps', form='pint')
q


# In[11]:


q = puw.quantity('1.0 nm/ps', form='openmm.unit')
q


# Units can be created in a similar way with `pyunitwizard.unit()`:

# In[12]:


u = puw.unit('kcal/mol', form='pint')
u


# In[13]:


puw.get_form(u)


# In[14]:


u = puw.unit('N/nm**2', form='openmm.unit')
u


# And two auxiliary methods, `pyunitwizard.is_quantity()` and `pyunitwizard.is_unit()`, can be used to check if a variable is a quantity or a unit object no matter their form:

# In[15]:


puw.is_quantity(q)


# In[16]:


puw.is_quantity(u)


# In[17]:


puw.is_unit(u)


# Finnally, quantities and units with different forms can be translated into strings:

# In[18]:


q


# In[19]:


puw.convert(q, to_form='string')


# In[20]:


puw.convert(u, to_form='string')


# Additionally, given that some of the libraries supported by PyUnitWizard, as pint, can parse strings to make quantities, this wizard takes advantage of this great functionality to convert strings to any quantity form (see section ['Working with strings'](Strings.ipynb)):

# In[21]:


puw.convert('10.0 Å -0.5 nm', to_form='openmm.unit')


# In[22]:


puw.convert('1.0 mol/L + 3.5 mol/dL', to_form='pint')


# Or to any unit form:

# In[23]:


puw.convert('1.0 (mol/L)/picosecond', to_form='pint', to_type='unit')

