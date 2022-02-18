#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# # Standardization
# *-If quantities have to be handled in your project with a default set of dimensions, PyUnitWizard can help you defining a set of standard units-*
# 
# Let's suppose we are working with observables and magnitudes encoded as pythonic quantities coming from different tools -with different forms-. PyUnitWizard, in addition to work with a default form defined at any moment, can also standardize quantities to a set of units of the users election:

# In[2]:


import pyunitwizard as puw
puw.configure.load_library(['pint', 'openmm.unit'])
puw.configure.set_default_form('pint')


# With the method `puw.configure.set_standard_units()` the list of units as standards can be set:

# In[3]:


puw.configure.set_standard_units(['nm', 'ps', 'K', 'mole', 'amu', 'e',
                                 'kcal/mol', 'N/nm**2', 'N', 'degrees'])


# In[4]:


puw.configure.get_standard_units()


# Some of these standards are fundamental units, some are combinations, and others can be adimensional:

# In[5]:


puw.kernel.dimensional_fundamental_standards


# In[6]:


puw.kernel.dimensional_combinations_standards


# In[7]:


puw.kernel.adimensional_standards


# This way, the method `pyunitwizard.standardize()` converts any quantity to the default form with the standard units:

# In[8]:


q = puw.quantity(450, 'km/hour', form='openmm.unit')
output = puw.standardize(q)
print('{} as {} quantity'.format(output, puw.get_form(output)))


# In[9]:


q = puw.quantity(1.4, 'kJ/mol')
output = puw.standardize(q)
print('{} as {} quantity'.format(output, puw.get_form(output)))


# In[10]:


q = puw.quantity(0.250, 'kN/nm**2')
output = puw.standardize(q)
print('{} as {} quantity'.format(output, puw.get_form(output)))


# In[11]:


q = puw.quantity(9.8, 'amu*m/s**2')
output = puw.standardize(q)
print('{} as {} quantity'.format(output, puw.get_form(output)))


# In[12]:


puw.configure.set_standard_units(['nm', 'ps', 'K', 'kcal', 'mol', 'radians'])


# In[13]:


puw.kernel.adimensional_standards


# In[14]:


q = puw.quantity(1.4, 'kJ/mol')
output = puw.standardize(q)
print('{} as {} quantity'.format(output, puw.get_form(output)))


# In[15]:


q = puw.quantity(30, 'degrees')
output = puw.standardize(q)
print('{} as {} quantity'.format(output, puw.get_form(output)))


# In[ ]:




