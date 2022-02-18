from pyunitwizard._private_tools.exceptions import *

try:
    import openmm.unit as openmm_unit
except:
    raise LibraryNotFoundError('openmm')

form_name = 'openmm.unit'
parser = True

is_form={
    openmm_unit.Quantity:form_name,
    openmm_unit.Unit:form_name,
    }

try:
    from pint.util import ParserHelper as PintParserHelper
    from .api_pint import string_to_quantity as string_to_pint_quantity
except:
    PintParserHelper=None

def is_quantity(quantity_or_unit):

    output = (type(quantity_or_unit)==openmm_unit.Quantity)

    return output

def is_unit(quantity_or_unit):

    output = (type(quantity_or_unit)==openmm_unit.Unit)

    return output

_dimensions_translator={
    'length' : '[L]',
    'mass' : '[M]',
    'time' : '[T]',
    'temperature' : '[K]',
    'amount' : '[mol]',
    'luminous intensity' : '[Cd]'
}

def dimensionality(quantity_or_unit):

    output = {'[L]':0, '[M]':0, '[T]':0, '[K]':0, '[mol]':0, '[A]':0, '[Cd]':0}

    tmp_unit = None

    if is_quantity(quantity_or_unit):
        tmp_unit = quantity_or_unit.unit
    elif is_unit(quantity_or_unit):
        tmp_unit = quantity_or_unit
    else:
        raise ValueError

    for base, exponent in tmp_unit.iter_base_dimensions():
        if base.name == 'charge':
            output['[A]'] += exponent
            output['[T]'] += exponent
        else:
            if base.name in _dimensions_translator:
                output[_dimensions_translator[base.name]]=exponent

    return output

def compatibility(quantity_or_unit_1, quantity_or_unit_2):

    tmp_unit_1 = None
    tmp_unit_2 = None

    if is_quantity(quantity_or_unit_1):
        tmp_unit_1 = get_unit(quantity_or_unit_1)

    if is_quantity(quantity_or_unit_2):
        tmp_unit_2 = get_unit(quantity_or_unit_2)

    return tmp_unit_1.is_compatible(tmp_unit_2)


def make_quantity(value, unit_name):

    unit=string_to_unit(unit_name)
    return openmm_unit.Quantity(value, unit)

def string_to_quantity(string):

    if PintParserHelper is None:
        raise PintNotFoundError()

    pint_quantity = string_to_pint_quantity(string)
    parser = PintParserHelper.from_string(pint_quantity.__str__())
    tmp_quantity = parser.scale
    for unit_name, exponent in parser.items():
        tmp_quantity *= getattr(openmm_unit, unit_name)**exponent
    return tmp_quantity

def string_to_unit(string):

    tmp_quantity = string_to_quantity(string)
    tmp_unit = get_unit(tmp_quantity)
    return tmp_unit

def to_string(quantity_or_unit):

    return quantity_or_unit.__str__()

def convert(quantity, unit_name):

    unit = string_to_unit(unit_name)
    return quantity.in_units_of(unit)

def get_value(quantity):

    return quantity._value

def get_unit(quantity):

    return quantity.unit

def to_pint(quantity):

    from .api_pint import make_quantity as make_pint_quantity

    value = get_value(quantity)
    unit_name = to_string(get_unit(quantity))

    return make_pint_quantity(value, unit_name)

def to_unyt(quantity):

    raise NotImplementedMethodError()

