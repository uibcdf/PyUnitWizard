#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# # Quick Guide
# 
# *-Brief tutorial for those in a hurry-*
# 
# There are several python libraries to work with physical quantities such as pint, unyt or openmm.unit. Now imagine that your project requires the interaction with different tools, and those tools don't operate with the same physical quantities objects. Wouldn't having a library with a unique API to work with different forms of physical quantities be a relief?
# 
# PyUnitWizard allows you to work with more than a physical units library in python -such as pint, unyt or openmm.unit- with a unique API. PyUnitWizard works as the man in the middle between your code 

# ## Import PyUnitWizard and choose the libraries you are going to work with.

# In[2]:


import pyunitwizard as puw


# In[3]:


puw.configure.load_library(['pint', 'openmm.unit'])


# In[4]:


puw.configure.get_default_form()


# ## Let's play a bit with quantities and units
# 
# Let's make a quantity from its value and unit name:

# In[5]:


q = puw.quantity(2.5, 'nanometers/picoseconds')


# In[6]:


q


# We can check that **q** is in deed a Pint quantity:

# In[7]:


puw.is_quantity(q)


# In[8]:


puw.get_form(q)


# Let's extract now its value and units:

# In[9]:


puw.get_value(q)


# In[10]:


puw.get_unit(q)


# And let's also check the dimensionality:

# In[11]:


puw.get_dimensionality(q)


# We can now translate **q** from Pint to openmm.unit:

# In[12]:


q2 = puw.convert(q, to_form='openmm.unit')


# In[13]:


puw.get_form(q2)


# In[14]:


q2


# Finally, lets convert `q2` into other units:

# In[15]:


q3 = puw.convert(q2, to_unit='angstroms/picoseconds')
print('{} was converted to angstroms/picoseconds as {}'.format(q2, q3))


# The dimensionality of `q3` did not change:

# In[16]:


puw.get_dimensionality(q3)


# Actually, `q` and `q3` are compatible quantities (they have the same dimensionality):

# In[17]:


puw.compatibility(q, q3)


# Let's make now a unit from its name or symbol:

# In[18]:


u = puw.unit('kJ/mol', form='openmm.unit')


# In[19]:


u


# We can check that `u` is in deed a openmm.unit unit.

# In[20]:


puw.get_form(u)


# In[21]:


puw.is_unit(u)


# And as it was done already with a quantity, we can check the dimensionality:

# In[22]:


puw.get_dimensionality(u)


# Units and quantities can be turned into strings:

# In[23]:


puw.convert(u, to_form='string')


# Quantities and units can also be created from algebraical expressions mixing values and units:

# In[24]:


q = puw.convert('3.5N/(2.0nm**2)', to_form='openmm.unit')


# In[25]:


q


# Involving also lists:

# In[26]:


q = puw.convert('[0.0, 0.0, 0.0] nm', to_form='pint')


# In[27]:


q


# And quantities can be converted to strings:

# In[28]:


puw.convert(q, to_form='string')


# As well as units:

# In[29]:


u = puw.convert('K', to_form='pint', to_type='unit')


# In[30]:


u


# In[31]:


puw.convert(u, to_form='string')


# ## The default quantity form

# PyUnitWizard takes the first unit library loaded as the default quantity form:

# In[32]:


puw.configure.get_libraries_loaded()


# In[33]:


puw.configure.get_default_form()


# The default form is taken when a method is invoked with out specifying the quantity or unit form:

# In[34]:


q1 = puw.convert('3.5N/(2.0nm**2)')
q2 = puw.quantity(300.0, 'kelvin')

print('q1 is a {} quantity'.format(puw.get_form(q1)))
print('q2 is a {} quantity'.format(puw.get_form(q2)))


# The default form can be changed with the following method:

# In[35]:


puw.configure.set_default_form('openmm.unit')


# In[36]:


q1 = puw.convert('3.5N/(2.0nm**2)')
q2 = puw.quantity(300.0, 'kelvin')

print('q1 is a {} quantity'.format(puw.get_form(q1)))
print('q2 is a {} quantity'.format(puw.get_form(q2)))


# ## The standards
# 
# PyUnitWizard includes the possibility to define standard units for you library or python script. 
# Let's suppose your quantities will be always expressed in 'nm', 'ps' and 'kcal/mol' as Pint quantities. This two next lines sets this election as the default standards and form:

# In[37]:


puw.configure.set_standard_units(['nm', 'ps', 'kcal', 'mole'])
puw.configure.set_default_form('pint')


# We can check that these values were indeed stored:

# In[38]:


puw.configure.get_standard_units()


# In[39]:


puw.configure.get_default_form()


# The method `pyunitwizard.get_standard()` shows the standardized compatible units of a quantity:

# In[40]:


q = puw.quantity('2.0 pm', form='openmm.unit')


# In[41]:


puw.get_standard_units(q)
print('The standard of q is:', puw.get_standard_units(q))


# And the method `pyunitwizard.standardize()` converts and translates the input quantity into the defined defined default standard compatible units and form:

# In[42]:


q2 = puw.standardize(q)
print('q2 is now a {} quantity expressed in {}.'.format(puw.get_form(q2), puw.get_unit(q2)))


# Other output forms can be specified with the input argument `to_form`

# In[43]:


q2 = puw.standardize(q, to_form='openmm.unit')
print('q2 is now a {} quantity expressed in {}.'.format(puw.get_form(q2), puw.get_unit(q2)))


# As you noticed, we have mention that `pyunitwizard.get_standard` and `pyunitwizard.standardize` results with the compatible default standard units. This is combination of standard units are also considered:

# In[44]:


q = puw.quantity('100 angstroms**3')


# In[45]:


q = puw.quantity('100 angstroms**3')
print('The standard of q is:', puw.get_standard_units(q))


# In[46]:


q = puw.quantity('3000.0 pm/ns')
print('The standard of q is:', puw.get_standard_units(q))


# In[47]:


q = puw.quantity('1.4 kJ/mol')
print('The standard of q is:', puw.get_standard_units(q))


# Again, and finnally, `pyunitwizard.standardize` can help you to have homogeneous outputs in you library:

# In[48]:


q = puw.quantity(1.4, 'kJ/mol', form='openmm.unit')
output = puw.standardize(q)
print('{} as {} quantity'.format(output, puw.get_form(output)))


# ## Integrate PyUnitWizard in your library
# 
# Finnally, and although its is out of the scope of this tutorial, let's mention that PyUnitWizard can be integrated in your library with your local definition of default quantities library and standards. See the section `xxx` in this documentation for further details.
