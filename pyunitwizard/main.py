import simtk.unit as simtk_unit
import pint as pint
from ._private_tools.forms import digest_form, digest_to_form
from ._private_tools.unit_names import digest_unit_name
from .forms import dict_is_form, dict_is_unit, dict_is_quantity
from .forms import dict_get_unit, dict_get_value, dict_make_quantity
from .forms import dict_convert, dict_translate, dict_string_to_quantity, dict_string_to_unit, dict_to_string

default_form = 'pint'
default_parser = 'pint'

def get_form(quantity_or_unit):

    # quantity_or_unit is quantity or unit

    output = None

    try:
        return dict_is_form[type(quantity_or_unit)]
    except:
        try:
            return dict_is_form[quantity_or_unit]
        except:
            raise NotImplementedError("This quantity form was not implemented yet. Please open an issue to suggest its inclusion.")

    return output

def is_quantity(quantity_or_unit):

    output = None
    form = get_form(quantity_or_unit)

    output = dict_is_quantity[form](quantity_or_unit)

    return output

def is_unit(quantity_or_unit):

    output = None
    form = get_form(quantity_or_unit)

    output = dict_is_unit[form](quantity_or_unit)

    return output

def get_value(quantity):

    output = None
    form =get_form(quantity)

    try:
        output = dict_get_value[form](quantity)
    except:
        raise NotImplementedError

    return output

def get_unit(quantity, to_form=None):

    output = None
    form =get_form(quantity)
    to_form = digest_to_form(to_form)

    try:
        output = dict_get_unit[form](quantity)
        if to_form is not None:
            unit_name = get_unit_name(quantity)
            output = make_unit(unit_name)
    except:
        raise NotImplementedError

    return output

def quantity(value, unit_name, parser=default_parser, form=default_parser):

    output = None

    form = digest_form(form)
    unit_name = digest_unit_name(unit_name, form)

    try:
        output = dict_make_quantity[form](value, unit_name)
    except:
        raise NotImplementedError

    return output

def unit(unit_name, parser=default_parser, form=default_form):

    return string_to_unit(unit_name, parser=parser, to_form=form)

def translate(quantity_or_unit, to_form=default_form):

    output = None

    form_in = get_form(quantity_or_unit)
    to_form = digest_to_form(to_form)

    if (to_form is None) or (to_form==form_in):
        output = quantity_or_unit
    else:
        try:
            output = dict_translate[form_in][to_form](quantity_or_unit)
        except:
            raise NotImplementedError("This translation has not been implemented yet.")

    return output

def convert(quantity_or_unit, unit_name, to_form=None):

    output = None

    form_in = get_form(quantity_or_unit)
    to_form = digest_to_form(to_form)

    try:

        unit_name = digest_unit_name(unit_name, form_in)
        output = dict_convert[form_in](quantity_or_unit, unit_name)

        if to_form is not None:
            output = translate(output, to_form=to_form)

    except:

        if to_form is None:
            raise ValueError
        else:
            tmp_quantity_or_unit = translate(quantity_or_unit, to_form=to_form)
            unit_name = digest_unit_name(unit_name, to_form)
            output = convert(tmp_quantity_or_unit, unit_name)

    return output

def string_to_quantity(string, parser=default_parser, to_form=default_form):

    parser = digest_form(parser)
    to_form = digest_to_form(to_form)

    output = dict_string_to_quantity[parser](string)
    output = translate(output, to_form=to_form)

    return output

def string_to_unit(string, parser=default_parser, to_form=default_form):

    parser = digest_form(parser)
    to_form = digest_to_form(to_form)

    output = dict_string_to_unit[parser](string)
    output = translate(output, to_form=to_form)

    return output

def to_string(quantity_or_unit, parser=None):

    output = None

    if parser is None:
        parser= get_form(quantity_or_unit)

    tmp_quantity_or_unit = translate(quantity_or_unit, to_form=parser)
    output = dict_to_string[parser](tmp_quantity_or_unit)

    return output

