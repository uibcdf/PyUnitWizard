#!/usr/bin/env python
# coding: utf-8

# # Docstrings
# 
# A [docstring](https://www.python.org/dev/peps/pep-0257/#id4) is a string embedded in a piece of code for the purpose of documenting it.
# 
# Docstrings in BiFrEE are written in [NumPy style](). Why? Well, BiFrEE's main developers know there are other docstring styles, but the NumPy's one is clear, easy to be read, and widely extended.
# 
# ```{admonition} Note
# :class: note
# When BiFrEE's web documentation is compiled, [Sphinx](https://www.sphinx-doc.org/en/master/index.html) handles the docstrings with the assistance of [the Napoleon extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html). Have a look to the [sphinx section in this guide](). 
# ```
# 
# ```{admonition} It is suggested...
# :class: tip, dropdown
# Although you can find some guidelines to write BiFrEE's docstrings below, if you are not familiar with the docstrings and the NumPy style you may also check the following webs:
#    - [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
#    - [numpydoc's documentation](https://numpydoc.readthedocs.io/en/latest/format.html)
#    - [Example in numpydoc's documentation](https://numpydoc.readthedocs.io/en/latest/example.html)
#    - [Example in Napoleon's documentation](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html)
# ```

# ## Documenting a class
# 
# ```python
# 
# class ClassName():
#     """The summary line for a class docstring should fit on one line.
#     
#     If the class has public attributes, they may be documented here
#     in an ``Attributes`` section and follow the same formatting as a
#     function's ``Args`` section. Alternatively, attributes may be documented
#     inline with the attribute's declaration (see __init__ method below).
# 
#     Properties created with the ``@property`` decorator should be documented
#     in the property's getter method.
# 
#     Attributes
#     ----------
#     attr1 : str
#         Description of `attr1`.
#     attr2 : :obj:`int`, optional
#         Description of `attr2`.
# 
#     """
# 
#     def __init__(a, b=14):
#          """Example of docstring on the __init__ method.
# 
#         The __init__ method may be documented in either the class level
#         docstring, or as a docstring on the __init__ method itself.
# 
#         Either form is acceptable, but the two should not be mixed. Choose one
#         convention to document the __init__ method and be consistent with it.
# 
#         Note
#         ----
#         Do not include the `self` parameter in the ``Parameters`` section.
# 
#         Parameters
#         ----------
#         a : obj:`list` of :obj:`str`
#             Description of `A`. Multiple
#             lines are supported.
#         b : :obj:`int`, default=14
#             Description of `B`.
# 
#         """
# 
# ```
# 
# 
# ```{admonition} See also
# :class: attention
# Before writting your own docstrings, have a look to [BiFrEE's code](https://github.com/uibcdf/BiFrEE/tree/main/sabueso) and the [API documentation](https://uibcdf.org/BiFrEE/api.html). There you can find useful examples on how the docstrings are written and rendered, and what are the usual conventions adopted in BiFrEE's docstrings.
# ```

# ## Documenting a method
# 
# Some advices need to be followed to write a methods documentation. But first let's see an example of the docstring to document a method in BiFrEE's code:
# 
# ```python
# 
# def method_name(a, b=True):
#     """A short one line description without variable names or the method name
# 
#     Paragraph with detailed explanation.
# 
#     Parameters
#     ----------
#     a : int
#         Description of parameter `a`.
#     b : bool, default=True
#         Description of input argument `b` (the default is True, which implies ...).
# 
#     Returns
#     -------
#     int
#         Description of the output int value.
# 
#     Examples
#     --------
#     First example comment.
#     
#     >>> 2+2
#     4
# 
#     Comment explaining the second example.
# 
#     >>> import numpy as np
#     >>> np.add([[1, 2], [3, 4]],
#     ...        [[5, 6], [7, 8]])
#     array([[ 6,  8],
#            [10, 12]])
# 
#     See Also
#     --------
# 
#     :func:`bifree.get`, :func:`bifree.select`
# 
#     Notes
#     -----
# 
#     Section to include notes.
# 
#     Todo
#     ----
# 
#     Section to include a todo message.
# 
#     Warning
#     -------
# 
#     Section to include a warning message.
#     
#     """
#     
#     pass
# ```
# 
# ### About working with magnitudes
# 
# ...
# 
# ```{admonition} See also
# :class: attention
# Before writting your own docstrings, have a look to [BiFrEE's code](https://github.com/uibcdf/BiFrEE/tree/main/sabueso) and the [API documentation](https://uibcdf.org/BiFrEE/api.html). There you can find useful examples on how the docstrings are written and rendered, and what are the usual conventions adopted in BiFrEE's docstrings.
# ```

# In[ ]:




