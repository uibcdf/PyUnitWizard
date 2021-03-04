import simtk.unit as simtk_unit
import pint as pint
from ._private_tools.forms import digest_form, digest_to_form
from ._private_tools.parsers import digest_parser
from .forms import dict_is_form, dict_is_unit, dict_is_quantity, dict_dimensionality, dict_compatibility
from .forms import dict_get_unit, dict_get_value, dict_make_quantity
from .forms import dict_convert, dict_translate, dict_string_to_quantity, dict_string_to_unit, dict_to_string
from ._private_tools import default
import numpy as np

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

    if type(quantity_or_unit)=='str':
        output = string_is_quantity(quantity_or_unit)
    else:
        try:
            form = get_form(quantity_or_unit)
            output = dict_is_quantity[form](quantity_or_unit)
        except:
            output = False

    return output

def is_unit(quantity_or_unit):

    if type(quantity_or_unit)=='str':
        output = string_is_unit(quantity_or_unit)
    else:
        try:
            form = get_form(quantity_or_unit)
            output = dict_is_unit[form](quantity_or_unit)
        except:
            output = False

    return output

def get_value(quantity, in_units=None):

    output = None

    if type(quantity) is str:
        quantity = string_to_quantity(quantity)

    form =get_form(quantity)

    if in_units is not None:
        tmp_quantity = convert(quantity, in_units=in_units)
    else:
        tmp_quantity = quantity

    try:
        output = dict_get_value[form](tmp_quantity)
    except:
        raise NotImplementedError

    return output

def get_unit(quantity, to_form=None):

    output = None

    if type(quantity) is str:
        quantity = string_to_quantity(quantity)

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

def dimensionality(quantity_or_unit, output='dict'):

    dim = None

    if type(quantity_or_unit) is str:
        if string_is_quantity(quantity_or_unit):
            quantity_or_unit = string_to_quantity(quantity_or_unit)
        elif string_is_unit(quantity_or_unit):
            quantity_or_unit = string_to_unit(quantity_or_unit)

    form = get_form(quantity_or_unit)
    dim = dict_dimensionality[form](quantity_or_unit)

    if output is 'array':
        dim = np.array([dim[ii] for ii in default.order_fundamental_units], dtype=float)

    return dim

def compatibility(quantity_or_unit_1, quantity_or_unit_2):

    d1 = dimensionality(quantity_or_unit_1, output='array')
    d2 = dimensionality(quantity_or_unit_2, output='array')

    n_fundamental_units = len(default.order_fundamental_units)

    if (np.sum(np.isclose(d1, 0.0)) == n_fundamental_units) and (np.sum(np.isclose(d2, 0.0)) == n_fundamental_units):

        form1 = get_form(quantity_or_unit_1)
        form2 = get_form(quantity_or_unit_2)

        if form1!=form2:

            try:
                tmp = translate(quantity_or_unit_1, to_form=form2)
                output = dict_compatibility[form2](tmp, quantity_or_unit_2)
            except:
                tmp = translate(quantity_or_unit_2, to_form=form1)
                output = dict_compatibility[form1](tmp, quantity_or_unit_1)

        else:

            output = dict_compatibility[form1](quantity_or_unit_1, quantity_or_unit_2)

    else:

        output = np.all(d1==d2)

    return output

def quantity(value, unit=None, form=None, parser=None):

    output = None

    if type(value) is str:
        if unit is None:
            output = string_to_quantity(value, form=form, parser=parser)
        elif type(unit) is str:
            output = string_to_quantity(value+' '+unit, form=form, parser=parser)
        elif is_unit(unit):
            unit = to_string(unit)
            output = string_to_quantity(value+' '+unit, form=form, parser=parser)
    else:
        if unit is None:
            raise ValueError('The input argument "unit" is required.')
        elif type(unit) is not str:
            unit = to_string(unit)

        form = digest_form(form)

        try:
            output = dict_make_quantity[form](value, unit)
        except:
            raise NotImplementedError

    return output

def unit(unit_name, form=None, parser=None):

    return string_to_unit(unit_name, to_form=form, parser=parser)

def translate(quantity_or_unit, to_form=None):

    output=None

    if type(quantity_or_unit) is str:
        if string_is_quantity(quantity_or_unit):
            quantity_or_unit = string_to_quantity(quantity_or_unit)
        elif string_is_unit(quantity_or_unit):
            quantity_or_unit = string_to_unit(quantity_or_unit)

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

def convert(quantity_or_unit, in_units, to_form=None, parser=None):

    output = None

    if type(quantity_or_unit) is str:
        if string_is_quantity(quantity_or_unit):
            quantity_or_unit = string_to_quantity(quantity_or_unit)
        elif string_is_unit(quantity_or_unit):
            quantity_or_unit = string_to_unit(quantity_or_unit)

    form_in = get_form(quantity_or_unit)
    to_form = digest_to_form(to_form)
    parser = digest_parser(parser)

    if to_form is None:
        to_form = form_in

    try:

        if parser is None:
            parser = form_in

        if parser == form_in:
            output = dict_convert[form_in](quantity_or_unit, in_units)
        else:
            output = dict_translate[form_in](quantity_or_unit, to_form=parser)
            output = dict_convert[parser](output, in_units)

        output = translate(output, to_form=to_form)

    except:

        if parser is None:
            parser = to_form

        if parser == form_in:
            output = dict_convert[form_in](quantity_or_unit, in_units)
        else:
            output = dict_translate[form_in](quantity_or_unit, to_form=parser)
            output = dict_convert[parser](output, in_units)

        output = translate(output, to_form=to_form)

    return output

def get_standard_units(quantity_or_unit):

    dim = dimensionality(quantity_or_unit)
    solution = np.array([dim[ii] for ii in default.order_fundamental_units], dtype=float)
    n_dims_solution = len(default.order_fundamental_units) - np.sum(np.isclose(solution, 0.0))

    output = None

    if n_dims_solution == 0:

        for standard_unit, _ in default.adimensional_standards.items():
            if compatibility(quantity_or_unit, standard_unit):
                output = standard_unit
                break

    elif n_dims_solution == 1:

        for standard_unit, dim_array in default.dimensional_fundamental_standards.items():
            if np.allclose(solution, dim_array):
                output = standard_unit
                break

        if output is None:

            matrix = []
            standard_units = []

            for aux_unit, aux_dim_array in default.tentative_base_standards.items():
                standard_units.append(string_to_unit(aux_unit))
                matrix.append(aux_dim_array)

            matrix = np.array(matrix)

            x, _, _, _ = np.linalg.lstsq(matrix.T, solution, rcond=None)

            x = x.round(4)

            if np.allclose(np.dot(matrix.T, x), solution):
                output = 1
                for u, exponent in zip(standard_units, x):
                    if not np.isclose(0.0, exponent):
                        output *= u**exponent

                output = to_string(get_unit(output))

    else:

        for standard_units, dim_array in default.dimensional_combinations_standards.items():
            if np.allclose(solution, dim_array):
                output = standard_units
                break

        if output is None:

            matrix = []
            standard_units = []

            for aux_unit, aux_dim_array in default.dimensional_fundamental_standards.items():
                standard_units.append(string_to_unit(aux_unit))
                matrix.append(aux_dim_array)

            matrix = np.array(matrix)

            x, _, _, _ = np.linalg.lstsq(matrix.T, solution, rcond=None)

            x = x.round(4)

            if np.allclose(np.dot(matrix.T, x), solution):
                output = 1
                for u, exponent in zip(standard_units, x):
                    if not np.isclose(0.0, exponent):
                        output *= u**exponent

                output = to_string(get_unit(output))

        if output is None:

            matrix = []
            standard_units = []

            for aux_unit, aux_dim_array in default.tentative_base_standards.items():
                standard_units.append(string_to_unit(aux_unit))
                matrix.append(aux_dim_array)

            matrix = np.array(matrix)

            x, _, _, _ = np.linalg.lstsq(matrix.T, solution, rcond=None)

            x = x.round(4)

            if np.allclose(np.dot(matrix.T, x), solution):
                output = 1
                for u, exponent in zip(standard_units, x):
                    if not np.isclose(0.0, exponent):
                        output *= u**exponent

                output = to_string(get_unit(output))


    return output

def standardize(quantity_or_unit, to_form=None):

    to_form = digest_form(to_form)

    try:
        output = translate(quantity_or_unit, to_form=to_form)
        standard = get_standard_units(output)
        if standard is None:
            raise ValueError("The input quantity or unit has no standard.")
        output = convert(output, standard)
    except:
        standard = get_standard_units(quantity_or_unit)
        if standard is None:
            raise ValueError("The input quantity or unit has no standard.")
        output = convert(quantity_or_unit, standard)
        output = translate(output, to_form=to_form)

    return output

def string_is_quantity(string):

    if type(string)!=str:
        raise ValueError("Input argument of string_is_quantity is not string.")

    try:
        quantity = string_to_quantity(string)
        form = get_form(quantity_or_unit)
        output = dict_is_quantity[form](quantity_or_unit)
    except:
        output = False

    return output

def string_is_unit(string):

    if type(string)!=str:
        raise ValueError("Input argument of string_is_quantity is not string.")

    try:
        quantity = string_to_unit(string)
        form = get_form(quantity_or_unit)
        output = dict_is_quantity[form](quantity_or_unit)
    except:
        output = False

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

