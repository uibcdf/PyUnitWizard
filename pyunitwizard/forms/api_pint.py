import pint as pint

form_name = 'Pint'

is_form={
    pint.Quantity:form_name,
    pint.Unit:form_name,
    type(1.0*pint.Unit('nanometer')):form_name
    }


def make_quantity(value, unit_name):

    return pint.Quantity(value, unit_name)

def make_unit(unit_name):

    return pint.Unit(unit_name)

def convert(quantity, unit_name):

    return quantity.to(unit_name)

def get_value(quantity):

    return quantity.magnitude

def get_unit_name(quantity):

    return str(quantity.units)

def get_unit(quantity):

    return quantity.units

def to_simtk_unit(quantity):

    from .api_simtk_unit import make_quantity as make_simtk_unit_quantity

    value = get_value(quantity)
    unit_name = get_unit_name(quantity)

    return make_simtk_unit_quantity(value, unit_name)

