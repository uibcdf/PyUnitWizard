#!/usr/bin/env python
# coding: utf-8

# # Import and configure PyUnitWizard
# 
# *-The list of unit libraries used by PyUnitWizard needs to be loaded at the beginning-*
# 
# PyUnitWizard detects, in the very moment it is imported, the list of supported libraries available in you environment.

# In[1]:


import pyunitwizard as puw


# In[2]:


puw.configure.get_libraries_supported()


# In[3]:


puw.configure.get_libraries_found()


# For PyUnitWizard to work with some of them -or all-, a list of available libraries need to be loaded:

# In[4]:


puw.configure.load_library(['pint', 'openmm.unit'])


# You can check the quantities libraries the wizard is going to work with:

# In[5]:


puw.configure.get_libraries_loaded()


# Finnally, PyUnitWizard always defines the first library loaded as the default one. But this can be changed as follows:

# In[6]:


puw.configure.get_default_form()


# In[7]:


puw.configure.set_default_form('openmm.unit')


# In[8]:


puw.configure.get_default_form()


# This way, if no library name -or quantity form name- is specified, PyUnitWizard assumes that the default one is applied:

# In[9]:


q = puw.quantity(1.0,'s')


# In[10]:


puw.get_form(q)

