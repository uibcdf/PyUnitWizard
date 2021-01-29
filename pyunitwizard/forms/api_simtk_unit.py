import simtk.unit as simtk_unit

form_name = 'simtk.unit'

is_form={
    simtk_unit.Quantity:form_name,
    }

def make_quantity(value, unit_name):

    unit=make_unit(unit_name)
    return simtk_unit.Quantity(value, unit)

def make_unit(unit_name):

    return getattr(simtk_unit, unit_name)

def convert(quantity, unit_name):

    unit = make_unit(unit_name)
    return quantity.in_units_of(unit)

def get_value(quantity):

    return quantity._value

def get_unit_name(quantity):

    return quantity.unit.name

def get_unit(quantity):

    return quantity.unit

def to_Pint(quantity):

    from .api_pint import make_quantity as make_pint_quantity

    value = get_value(quantity)
    unit_name = get_unit_name(quantity)

    return make_pint_quantity(value, unit_name)

