
form_name = 'string'
paser = False

is_form={
    str:form_name,
    }

def is_quantity(quantity_or_unit):

    from pyunitwizard.kernel import default_form, default_parser
    from pyunitwizard import convert as _convert, is_quantity as _is_quantity

    tmp_quantity_or_unit = _convert(quantity_or_unit, to_form=default_form, parser=default_parser)
    output = _is_quantity(tmp_quantity_or_unit)

    return output

def is_unit(quantity_or_unit):

    from pyunitwizard.kernel import default_form, default_parser
    from pyunitwizard import convert as _convert, is_unit as _is_unit

    tmp_quantity_or_unit = _convert(quantity_or_unit, to_form=default_form, parser=default_parser)
    output = _is_unit(tmp_quantity_or_unit)

    return output

def dimensionality(quantity_or_unit):

    from pyunitwizard.kernel import default_form, default_parser
    from pyunitwizard import convert as _convert, get_dimensionality as _get_dimensionality

    tmp_quantity_or_unit = _convert(quantity_or_unit, to_form=default_form, parser=default_parser)
    output = _get_dimensionality(tmp_quantity_or_unit)

    return output

def compatibility(quantity_or_unit_1, quantity_or_unit_2):

    from pyunitwizard.kernel import default_form, default_parser
    from pyunitwizard import convert as _convert, compatibility as _compatibility

    tmp_quantity_or_unit_1 = _convert(quantity_or_unit_1, to_form=default_form, parser=default_parser)
    tmp_quantity_or_unit_2 = _convert(quantity_or_unit_2, to_form=default_form, parser=default_parser)
    output = _compatibility(tmp_quantity_or_unit_1, tmp_quantity_or_unit_2)

    return output

def make_quantity(value, unit_name):

    from pyunitwizard.kernel import default_form, default_parser
    from pyunitwizard import convert as _convert, quantity as _quantity

    tmp_quantity_or_unit = _quantity(value, unit=unit_name, form=default_form, parser=default_parser)
    tmp_quantity_or_unit = _convert(tmp_quantity_or_unit, to_form='string', parser=default_parser)

    return tmp_quantity_or_unit

def get_value(quantity):

    from pyunitwizard.kernel import default_form, default_parser
    from pyunitwizard import convert as _convert, get_value as _get_value

    tmp_quantity_or_unit = _convert(quantity, to_form=default_form, parser=default_parser)
    tmp_value = _get_value(tmp_quantity_or_unit)
    tmp_value = str(tmp_value)

    return tmp_value

def get_unit(quantity):

    from pyunitwizard.kernel import default_parser
    from pyunitwizard import convert as _convert, get_unit as _get_unit

    tmp_quantity_or_unit = _convert(quantity, to_form=default_parser)
    tmp_unit = _get_unit(tmp_quantity_or_unit)
    tmp_unit = _convert(tmp_unit, to_form='string')

    return tmp_unit

def string_to_quantity(string):

    return string

def to_string(quantity_or_item):

    return quantity_or_item

def convert(quantity, unit_name):

    from pyunitwizard.kernel import default_form, default_parser
    from pyunitwizard import convert as _convert, get_unit as _get_unit

    tmp_quantity_or_unit = _convert(quantity, to_form=default_form, parser=default_parser)
    tmp_quantity_or_unit = _convert(tmp_quantity_or_unit, to_unit=unit_name, parser=default_parser)
    tmp_quantity_or_unit = _convert(tmp_quantity_or_unit, to_form='string')

    return tmp_quantity_or_unit

def to_openmm_unit(quantity):

    from .api_openmm_unit import string_to_quantity as _string_to_quantity

    tmp_quantity_or_unit = _string_to_quantity(quantity)

    return tmp_quantity_or_unit

def to_pint(quantity):

    from .api_pint import string_to_quantity as _string_to_quantity

    tmp_quantity_or_unit = _string_to_quantity(quantity)

    return tmp_quantity_or_unit

