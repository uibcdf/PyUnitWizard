from pyunitwizard._private_tools.exceptions import *

try:
    import pint as pint
except:
    raise LibraryNotFoundError('pint')

## Create a unit UnitRegistry
## See: https://pint.readthedocs.io/en/stable/tutorial.html#using-pint-in-your-projects

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity
U_ = ureg.Unit

##

form_name = 'pint'
parser = True

is_form={
    pint.Quantity:form_name,
    pint.Unit:form_name,
    Q_:form_name,
    U_:form_name,
    }

def is_quantity(quantity_or_unit):

    tmp_type = type(quantity_or_unit)
    output = (tmp_type==pint.Quantity or tmp_type==Q_)

    return output

def is_unit(quantity_or_unit):

    tmp_type = type(quantity_or_unit)
    output = (tmp_type==pint.Unit or tmp_type==U_)

    return output

_dimensions_translator={
    '[length]' : '[L]',
    '[mass]' : '[M]',
    '[time]' : '[T]',
    '[temperature]' : '[K]',
    '[substance]' : '[mol]',
    '[current]' : '[A]',
    '[luminosity]' : '[Cd]'
}

def dimensionality(quantity_or_unit):

    output = {'[L]':0, '[M]':0, '[T]':0, '[K]':0, '[mol]':0, '[A]':0, '[Cd]':0}

    for dim, exponent in quantity_or_unit.dimensionality.items():
        output[_dimensions_translator[dim]]=exponent

    return output

def compatibility(quantity_or_unit_1, quantity_or_unit_2):

    tmp_unit_1 = None
    tmp_unit_2 = None

    if is_quantity(quantity_or_unit_1):
        tmp_unit_1 = get_unit(quantity_or_unit_1)

    if is_quantity(quantity_or_unit_2):
        tmp_unit_2 = get_unit(quantity_or_unit_2)

    return tmp_unit_1.is_compatible_with(tmp_unit_2)

def make_quantity(value, unit_name):

    return Q_(value, unit_name)

def get_value(quantity):

    return quantity.magnitude

def get_unit(quantity):

    return quantity.units

def string_to_quantity(string):

    return Q_(string)

def to_string(quantity_or_item):

    return quantity_or_item.__str__()

def convert(quantity, unit_name):

    return quantity.to(unit_name)

def to_openmm_unit(quantity):

    from pint.util import ParserHelper as PintParserHelper
    try:
        import openmm.unit as openmm_unit
    except:
        raise LibraryNotFoundError('openmm')

    pint_parser = PintParserHelper.from_string(quantity.__str__())
    tmp_quantity = pint_parser.scale
    for unit_name, exponent in pint_parser.items():
        if unit_name in ['unified_atomic_mass_unit']:
            unit_name = 'amu'
        tmp_quantity *= getattr(openmm_unit, unit_name)**exponent

    return tmp_quantity

def to_unyt(quantity):

    raise NotImplementedMethodError()

