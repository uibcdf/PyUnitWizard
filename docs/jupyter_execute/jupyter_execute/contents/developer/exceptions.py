#!/usr/bin/env python
# coding: utf-8

# (developer:exceptions)=
# # Exceptions

# There is in the directory `pyunitwizard/_private_tools` a module named `exceptions.py` with customized exceptions. Use them timely. And, in case you want to raise a new exception type, please include it here for the others to use it.
# 
# To use a exception you just need to import it and raise it:
# 
# ```python
# from pyunitwizard._private_tools.exceptions import NotImplementedMethodError
# 
# def method_to_be_implemented_in_the_future():
#     
#     raise NotImplementedMethodError
# ```
# 
# Let's see the list of customized exceptions in pyunitwizard.

# (developer:exceptions:NotImplementedMethodError)=
# ## NotImplementedMethodError
# 
# The `NotImplementedMethodError` exception is raised when a method has being already defined but its code was not fully implemented yet. Maybe the method was just included in a developing version to be coded in the future. Or maybe the method works already for certain values of the input arguments, but not for others yet.
# 
# ```{admonition} See also
# :class: attention
# {func}`pyunitwizard._private_tools.exceptions.NotImplementedMethodError`
# ```

# (developer:exceptions:NotImplementedClassError)=
# ## NotImplementedClassError
# 
# The `NotImplementedClassError` exception is raised when a class has being already defined but its code was not fully implemented yet. Maybe the class was just included in a developing version to be coded in the future. Or maybe the class can be instantated already for certain values of the input arguments, but not for others yet.
# 
# ```{admonition} See also
# :class: attention
# {func}`pyunitwizard._private_tools.exceptions.NotImplementedClassError`
# ```

# (developer:exceptions:BadCallError)=
# ## BadCallError
# 
# The `BadCallError` is raised when a method was not properly called.
# 
# This exception has an optional input argument: the name of the probable wrong input argument.
# 
# ```{admonition} See also
# :class: attention
# {func}`pyunitwizard._private_tools.exceptions.BadCallError`
# ```

# (developer:exceptions:NoStandardError)=
# ## NoStandardError
# 
# The `NoStandardError` is raised when a quantity needs to be standardized and there are not enough standards declared.
# 
# ```{admonition} See also
# :class: attention
# {func}`pyunitwizard._private_tools.exceptions.NoStandardError`
# ```

# (developer:exceptions:UnknownFormError)=
# ## UnknownFormError
# 
# The `UnknownFormError` is raised when the quantity has a form not recognized and supported by PyUnitWizard.
# 
# ```{admonition} See also
# :class: attention
# {func}`pyunitwizard._private_tools.exceptions.UnknownFormError`
# ```

# (developer:exceptions:LibraryNotFoundError)=
# ## LibraryNotFoundError
# 
# The `LibraryNotFoundError` is raised when PyUnitWizard fails importing a library not required as dependence.
# 
# This exception has a mandatory input argument: the name of library not found.
# 
# ```{admonition} See also
# :class: attention
# {func}`pyunitwizard._private_tools.exceptions.LibraryNotFoundError`
# ```
