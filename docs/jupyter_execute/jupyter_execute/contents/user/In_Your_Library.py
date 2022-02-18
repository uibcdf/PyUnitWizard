#!/usr/bin/env python
# coding: utf-8

# # PyUnitWizard in your library
# *-Instructions to work with PyUnitWizard inside your own library-*
# 
# Here you can find the instructions to include PyUnitWizard in your projects. Following this indications, you don't need to worry about the requirements of the libraries supported by PyUnitWizard.
# 
# To illustrate how to include PyUnitWizard let's see a very simple library you can find in [github repository (examples directory)](https://github.com/uibcdf/PyUnitWizard/tree/main/examples): `testlib`. This is its structure:

# ```bash
# tree --dirsfirst --charset=markdown testlib
# ```

# ```
# testlib
# |-- box
# |   |-- __init__.py
# |   |-- methods_a.py
# |   |-- methods_b.py
# |   `-- methods_c.py
# |-- _pyunitwizard
# |   `-- __init__.py
# |-- __init__.py
# ```

# Make a directory named `_pyunitwizard` in your project top directory. And include in `_pyunitwizard` a `__init__.py` file such as:

# ```python
# ### testlib/_pyunitwizard/__init__.py ###
# import pyunitwizard as puw
# 
# # In this case Pint and openmm.unit are loaded:
# puw.load_libraries(['pint', 'openmm.unit'])
# 
# # And openmm.unit is defined as default form
# puw.set_default_form('openmm.unit')
# ```

# Now, let's define some methods using your `_pyunitwizard` module. The first ones in the file `main.py`:

# ```python
# ### testlib/main.py ###
# from ._pyunitwizard import puw
# 
# def sum_quantities(a, b, form=None):
# 
#     aa = puw.string_to_quantity(a, to_form=form)
#     bb = puw.string_to_quantity(b, to_form=form)
#     output = aa+bb
# 
#     return output
# 
# def get_form(quantity):
# 
#     return puw.get_form(quantity)
# 
# def libraries_loaded():
# 
#     return puw.libraries_loaded()
# ```

# And in a directory named `box` let's include two methods to test your `_pyunitwizard` module:

# ```python
# ### testlib/box/methods_a.py
# from .._pyunitwizard import puw
# 
# def get_default_form():
# 
#     return puw.get_default_form()
# ```
# 
# ```python
# ### testlib/box/methods_b.py
# from .._pyunitwizard import puw
# 
# def set_default_form(form):
# 
#     return puw.set_default_form(form)
# ```
# 

# Finnally, let's writte the `__init__.py` files in the top directory and in `box`:

# ```python
# # testlib/box/__init__.py
# from .methods_a import get_default_form
# from .methods_b import set_default_form
# ```
# 
# ```python
# # testlib/__init__.py
# from .main import sum_quantities, get_form, libraries_loaded
# from . import box
# ```

# This way we already have a simple library using PyUnitWizard. You can check how `testlib` works:

# ```ipython
# In [1]: import testlib
# 
# In [2]: testlib.libraries_loaded()
# Out[2]: ['pint', 'openmm.unit']
# 
# In [3]: q = testlib.sum_quantities('2cm','3cm')
# 
# In [4]: testlib.get_form(q)
# Out[4]: 'openmm.unit'
# 
# In [5]: testlib.box.get_default_form()
# Out[5]: 'openmm.unit'
# 
# In [6]: testlib.box.set_default_form('pint')
# 
# In [7]: q = testlib.sum_quantities('2cm','3cm')
# 
# In [8]: testlib.get_form(q)
# Out[8]: 'pint'
# ```

# <div class="alert alert-block alert-info">
# <b>Tip:</b> Together with testlib, in the github repository, you can find testlib2
# where pyunitwizard is included using only absolut import paths -as suggested by <a href="https://www.python.org/dev/peps/pep-0008/#imports">PEP8</a>-</div>
