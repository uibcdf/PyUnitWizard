PyUnitWizard
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/uibcdf/pyunitwizard/workflows/CI/badge.svg)](https://github.com/uibcdf/pyunitwizard/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/uibcdf/PyUnitWizard/branch/master/graph/badge.svg)](https://codecov.io/gh/uibcdf/PyUnitWizard/branch/master)


There are several Python libraries to work with physical quantities in the market, such as pint, unyt or openmm.unit. Imagine that your project or workflow requires the interaction with more than one of these tools, or that you are not sure if you will work with a different quantities library in the future. Wouldn't be having a unique API to work with different forms of physical quantities be a relief? PyUnitWizard just do that. It is the wizard you need in your code to change the form of your quantities with few effort.

## Example

```ipython
In [1]: import pyunitwizard as puw

In [2]: puw.configure.load_libraries(['pint', 'openmm.unit'])
   ...: puw.configure.set_default_form('pint')
   ...: puw.configure.set_standard_units(['nm', 'ps', 'kcal', 'mole'])
   ...: 

In [3]: q = puw.quantity(2.5, 'nanometers/picoseconds')

In [4]: puw.get_form(q)
Out[4]: 'pint'

In [5]: puw.get_value(q)
Out[5]: 2.5

In [6]: puw.get_unit(q)
Out[6]: <Unit('nanometer / picosecond')>

In [7]: puw.dimensionality(q)
Out[7]: {'[L]': 1, '[M]': 0, '[T]': -1, '[K]': 0, '[mol]': 0, '[A]': 0, '[Cd]': 0}

In [8]: q2 = puw.convert(q, to_unit='angstroms/femtoseconds', to_form='openmm.unit')

In [9]: print(q2)
0.025000000000000005 A/fs

In [10]: puw.get_form(q2)
Out[10]: 'openmm.unit'

In [11]: puw.compatibility(q, q2)
Out[11]: True

In [12]: q3 = puw.standardize(q2)

In [13]: print('q3 is now a {} quantity expressed in {}.'.format(puw.get_form(q3), puw.get_unit(q3)))
q3 is now a pint quantity expressed in nanometer / picosecond.
```

## Units Python libraries
- [openmm.unit](https://github.com/openmm/openmm/tree/master/wrappers/python/simtk/unit)
- [Pint](https://pint.readthedocs.io/en/stable/)
- [unyt](https://unyt.readthedocs.io/en/stable/)


### Copyright

Copyright (c) 2021, UIBCDF Lab


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.5.

