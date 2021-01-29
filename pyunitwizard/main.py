import simtk.unit as simtk_unit
import pint as pint
from ._private_tools.forms import digest_form, digest_to_form
from ._private_tools.unit_names import digest_unit_name
from .forms import dict_is_form, dict_get_unit, dict_get_unit_name, dict_get_value, dict_make_quantity, dict_make_unit, dict_convert, dict_translate

_default_form = 'Pint'

def get_form(quantity):

    output = None

    try:
        return dict_is_form[type(quantity)]
    except:
        try:
            return dict_is_form[quantity]
        except:
            raise NotImplementedError("This quantity form was not implemented yet. Please open an issue to suggest its inclusion.")

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

def get_unit_name(quantity, to_form=_default_form):

    output = None
    form =get_form(quantity)

    try:
        output = dict_get_unit_name[form](quantity)
    except:
        raise NotImplementedError

    return output

def quantity(value, unit_name, form=_default_form):

    output = None

    form = digest_form(form)
    unit_name = digest_unit_name(unit_name, form)

    try:
        output = dict_make_quantity[form](value, unit_name)
    except:
        raise NotImplementedError

    return output

def unit(unit_name, form=_default_form):

    output = None

    form = digest_form(form)
    unit_name = digest_unit_name(unit_name, form)

    try:
        output = dict_make_unit[form](unit_name)
    except:
        raise NotImplementedError

    return output

def translate(quantity, to_form=None):

    output = None

    form_in = get_form(quantity)
    to_form = digest_to_form(to_form)

    if (to_form is None) or (to_form==form_in):
        output = quantity
    else:
        try:
            output = dict_translate[form_in][to_form](quantity)
        except:
            raise NotImplementedError("This translation has not been implemented yet.")

    return output

def convert(quantity, unit_name, to_form=None):

    output = None

    form_in = get_form(quantity)
    to_form = digest_to_form(to_form)

    try:

        unit_name = digest_unit_name(unit_name, form_in)
        output = dict_convert[form_in](quantity, unit_name)

        if to_form is not None:
            output = translate(output, to_form=to_form)

    except:

        if to_form is None:
            raise ValueError
        else:
            tmp_quantity = translate(quantity, to_form=to_form)
            unit_name = digest_unit_name(unit_name, to_form)
            output = convert(tmp_quantity, unit_name)

    return output

