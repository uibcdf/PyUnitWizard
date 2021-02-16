import simtk.unit as simtk_unit
import pint as pint
from ._private_tools.forms import digest_form, digest_to_form
from ._private_tools.parsers import digest_parser
from .forms import dict_is_form, dict_is_unit, dict_is_quantity, dict_dimensionality
from .forms import dict_get_unit, dict_get_value, dict_make_quantity
from .forms import dict_convert, dict_translate, dict_string_to_quantity, dict_string_to_unit, dict_to_string
from ._private_tools import default

def get_default_standards():

    return default.standards

def get_standard(quantity_or_unit):

    dim = dimensionality(quantity_or_unit)
    dim = default.hashabledict(dim)

    try:
        output = default.standards[dim]
    except:
        output = None

    return output

def set_default_standards(standards):

    if type(standards) is str:
        standards=[standards]
    elif type(standards) not in [list, tuple]:
        raise ValueError

    for standard in standards:
        dim = dimensionality(string_to_unit(standard))
        dim = default.hashabledict(dim)
        default.standards[dim] = standard

    pass

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

def dimensionality(quantity_or_unit):

    output = None
    form = get_form(quantity_or_unit)
    output = dict_dimensionality[form](quantity_or_unit)

    return output

def compatibility(quantity_or_unit_1, quantity_or_unit_2):

    d1 = dimensionality(quantity_or_unit_1)
    d2 = dimensionality(quantity_or_unit_2)
    output = (d1==d2)

    return output

def quantity(value, unit_name, form=None, parser=None):

    output = None

    form = digest_form(form)

    try:
        output = dict_make_quantity[form](value, unit_name)
    except:
        raise NotImplementedError

    return output

def unit(unit_name, form=None, parser=None):

    return string_to_unit(unit_name, to_form=form, parser=parser)

def translate(quantity_or_unit, to_form=None):

    form_in = get_form(quantity_or_unit)
    to_form = digest_form(to_form)

    if (to_form is None) or (to_form==form_in):
        output = quantity_or_unit
    else:
        try:
            output = dict_translate[form_in][to_form](quantity_or_unit)
        except:
            raise NotImplementedError("This translation has not been implemented yet.")

    return output

def convert(quantity_or_unit, unit_name, to_form=None, parser=None):

    output = None

    form_in = get_form(quantity_or_unit)
    to_form = digest_to_form(to_form)
    parser = digest_parser(parser)

    if to_form is None:
        to_form = form_in

    try:

        if parser is None:
            parser = form_in

        if parser == form_in:
            output = dict_convert[form_in](quantity_or_unit, unit_name)
        else:
            output = dict_translate[form_in](quantity_or_unit, to_form=parser)
            output = dict_convert[parser](output, unit_name)

        output = translate(output, to_form=to_form)

    except:

        if parser is None:
            parser = to_form

        if parser == form_in:
            output = dict_convert[form_in](quantity_or_unit, unit_name)
        else:
            output = dict_translate[form_in](quantity_or_unit, to_form=parser)
            output = dict_convert[parser](output, unit_name)

        output = translate(output, to_form=to_form)

    return output

def standardize(quantity_or_unit, to_form=None):

    to_form = digest_form(to_form)

    try:
        output = translate(quantity_or_unit, to_form=to_form)
        standard = get_standard(output)
        if standard is None:
            raise ValueError("The input quantity or unit has no standard.")
        output = convert(output, standard)
    except:
        standard = get_standard(quantity_or_unit)
        if standard is None:
            raise ValueError("The input quantity or unit has no standard.")
        output = convert(quantity_or_unit, standard)
        output = translate(output, to_form=to_form)

    return output

def string_to_quantity(string, to_form=None, parser=None):

    parser = digest_parser(parser)
    to_form = digest_form(to_form)

    if parser is None:
        parser = to_form

    output = dict_string_to_quantity[parser](string)

    if parser != to_form:
        output = translate(output, to_form=to_form)

    return output

def string_to_unit(string, to_form=None, parser=None):

    parser = digest_parser(parser)
    to_form = digest_form(to_form)

    if parser is None:
        parser = to_form

    output = dict_string_to_unit[parser](string)

    if parser != to_form:
        output = translate(output, to_form=to_form)

    return output

def to_string(quantity_or_unit, parser=None):

    output = None

    if parser is None:
        parser= get_form(quantity_or_unit)

    tmp_quantity_or_unit = translate(quantity_or_unit, to_form=parser)
    output = dict_to_string[parser](tmp_quantity_or_unit)

    return output

