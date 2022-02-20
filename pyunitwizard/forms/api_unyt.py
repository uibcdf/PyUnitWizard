from pyunitwizard._private_tools.exceptions import *

try:
    import unyt as unyt
except:
    raise LibraryNotFoundError('unyt')

form_name = 'unyt'
parser = False

is_form={
    }

_dimensions_translator={
    'length' : '[L]',
    'mass' : '[M]',
    'time' : '[T]',
    'temperature' : '[K]',
    'amount' : '[mol]',
    'luminous intensity' : '[Cd]'
}

def is_quantity(quantity_or_unit):

    raise NotImplementedMethodError()

def is_unit(quantity_or_unit):

    raise NotImplementedMethodError()

def dimensionality(quantity_or_unit):

    raise NotImplementedMethodError()

def compatibility(quantity_or_unit_1, quantity_or_unit_2):

    raise NotImplementedMethodError()

def make_quantity(value, unit_name):

    raise NotImplementedMethodError()

def string_to_quantity(string):

    raise NotImplementedMethodError()

def to_string(unit):

    raise NotImplementedMethodError()

def convert(quantity, unit_name):

    raise NotImplementedMethodError()

def get_value(quantity):

    raise NotImplementedMethodError()

def get_unit(quantity):

    raise NotImplementedMethodError()

def to_pint(quantity):

    raise NotImplementedMethodError()

def to_openmm_unit(quantity):

    raise NotImplementedMethodError()

