import simtk.unit as simtk_unit
from pyunitwizard._private_tools.exceptions import *

form_name = 'simtk.unit'

is_form={
    simtk_unit.Quantity:form_name,
    simtk_unit.Unit:form_name,
    }

try:
    from pint.util import ParserHelper as PintParserHelper
    from .api_pint import string_to_quantity as string_to_pint_quantity
except:
    PintParserHelper=None

def is_quantity(quantity_or_unit):

    output = (type(quantity_or_unit)==simtk_unit.Quantity)

    return output

def is_unit(quantity_or_unit):

    output = (type(quantity_or_unit)==simtk_unit.Unit)

    return output

def make_quantity(value, unit_name):

    unit=string_to_unit(unit_name)
    return simtk_unit.Quantity(value, unit)

def string_to_quantity(string):

    if PintParserHelper is None:
        raise PintNotFoundError()

    pint_quantity = string_to_pint_quantity(string)
    parser = PintParserHelper.from_string(pint_quantity.__str__())
    tmp_quantity = parser.scale
    for unit_name, exponent in parser.items():
        tmp_quantity *= getattr(simtk_unit, unit_name)**exponent

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

def to_Pint(quantity):

    from .api_pint import make_quantity as make_pint_quantity

    value = get_value(quantity)
    unit_name = to_string(get_unit(quantity))

    return make_pint_quantity(value, unit_name)

