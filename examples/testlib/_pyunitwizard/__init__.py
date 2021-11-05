import pyunitwizard as puw
# In this case Pint and openmm.unit are loaded
puw.load_libraries(['pint', 'openmm.unit'])
# And openmm.unit is defined as default form
puw.set_default_form('openmm.unit')

