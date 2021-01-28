import simtk.unit as simtk_unit
from ._private_tools.forms import digest_form
from ._private_tools.unit_names import digest_unit_name

def get_form(quantity):

    output = None

    quantity_type = type(quantity)

    if quantity_type == simtk_unit:
        output = 'simtk.unit'
    else:
        raise NotImplementedError("This quantity form was not implemented yet. Please open an issue to suggest its inclusion.")

    return output

def quantity(value, unit_name, form='simtk.unit'):

    output = None

    form = digest_form(form)
    unit_name = digest_unit_name(unit_name, form)

    if form == 'simtk.unit':
        output = simtk_unit.Quantity(value, unit(unit_name, 'simtk.unit'))
    else:
        raise NotImplementedError

    return output


def unit(unit_name, form='simkt.unit'):

    output = None

    form = digest_form(form)
    unit_name = digest_unit_name(unit_name, form)

    if form == 'simtk.unit':
        output = getattr(simtk_unit, unit_name)
    else:
        raise NotImplementedError

    return output

def translate(quantity, to_form=None):

    output = None

    form_in = get_form(quantity)
    to_form = digest_to_form(to_form)

    if (to_form is None) or (to_form==form_in):
        output = quantity
    else:
        raise NotImplementedError

    return output

def convert(quantity, unit_name, to_form=None):

    output = None

    form_in = get_form(quantity)
    unit_name = digest_unit_name(unit_name, form_in)
    to_form = digest_to_form(to_form)

    try:

        if form_in == 'simtk.unit':
            output = output.in_units_of(unit(unit_name,'simtk.unit'))
        else:
            raise NotImplementedError

        if to_form is not None:
            output = translate(output, to_form=to_form)

    except:

        if to_form is None:
            raise ValueError
        else:
            tmp_quantity = translate(quantity, to_form=to_form)
            output = convert(tmp_quantity, unit_name)

    return output

