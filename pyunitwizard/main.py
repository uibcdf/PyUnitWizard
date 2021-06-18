import simtk.unit as simtk_unit
import pint as pint
from ._private_tools.forms import digest_form, digest_to_form
from ._private_tools.parsers import digest_parser
from .forms import dict_is_form, dict_is_unit, dict_is_quantity, dict_dimensionality, dict_compatibility
from .forms import dict_get_unit, dict_get_value, dict_make_quantity
from .forms import dict_convert, dict_translate, dict_string_to_quantity, dict_string_to_unit, dict_to_string
from .import kernel
import numpy as np

def get_form(quantity_or_unit):

    output = None

    try:
        return dict_is_form[type(quantity_or_unit)]
    except:
        try:
            return dict_is_form[quantity_or_unit]
        except:
            raise NotImplementedError("This quantity form was not implemented yet. Please open an issue to suggest its inclusion.")

    return output

def is_quantity(quantity_or_unit, parser=None):

    if type(quantity_or_unit)=='str':
        try:
            quantity_or_unit = convert(string, to_form=kernel.default_form, parser=parser)
            output = dict_is_quantity[kernel.default_form](quantity_or_unit)
        except:
            output = False
    else:
        try:
            form = get_form(quantity_or_unit)
            output = dict_is_quantity[form](quantity_or_unit)
        except:
            output = False

    return output

def is_unit(quantity_or_unit, parser=None):

    if type(quantity_or_unit)=='str':
        try:
            quantity_or_unit = convert(string, to_type='unit')
            form = get_form(quantity_or_unit)
            output = dict_is_quantity[form](quantity_or_unit)
        except:
            output = False
    else:
        try:
            form = get_form(quantity_or_unit)
            output = dict_is_unit[form](quantity_or_unit)
        except:
            output = False

    return output

def get_value(quantity, to_unit=None, parser=None):

    return convert(quantity, to_unit=to_unit, parser=parser, to_type='value')

def get_unit(quantity, to_form=None, parser=None):

    return convert(quantity, to_form=to_form, parser=parser, to_type='unit')

def similarity(quantity_or_unit_1, quantity_or_unit_2, relative_tolerance=1e-08):

    output = compatibility(quantity_or_unit_1, quantity_or_unit_2)

    if output == True:

        form_1 = get_form(quantity_or_unit_1)
        if form_1 == 'string':
            quantity_or_unit_1 = convert(quantity_or_unit_1)
            form_1 = get_form(quantity_or_unit_1)
        quantity_or_unit_2 = convert(quantity_or_unit_2, to_form=form_1)
        ratio = quantity_or_unit_1/quantity_or_unit_2
        output = (abs(ratio-1.0)<relative_tolerance)

    return output

def dimensionality(quantity_or_unit, output='dict'):

    dim = None

    if type(quantity_or_unit) is str:
        if is_quantity(quantity_or_unit):
            quantity_or_unit = convert(quantity_or_unit, to_type='quantity')
        elif is_unit(quantity_or_unit):
            quantity_or_unit = convert(quantity_or_unit, to_type='unit')

    form = get_form(quantity_or_unit)
    dim = dict_dimensionality[form](quantity_or_unit)

    if output is 'array':
        dim = np.array([dim[ii] for ii in kernel.order_fundamental_units], dtype=float)

    return dim

def compatibility(quantity_or_unit_1, quantity_or_unit_2):

    d1 = dimensionality(quantity_or_unit_1, output='array')
    d2 = dimensionality(quantity_or_unit_2, output='array')

    n_fundamental_units = len(kernel.order_fundamental_units)

    if (np.sum(np.isclose(d1, 0.0)) == n_fundamental_units) and (np.sum(np.isclose(d2, 0.0)) == n_fundamental_units):

        form1 = get_form(quantity_or_unit_1)
        form2 = get_form(quantity_or_unit_2)

        if form1!=form2:

            try:
                tmp = convert(quantity_or_unit_1, to_form=form2)
                output = dict_compatibility[form2](tmp, quantity_or_unit_2)
            except:
                tmp = convert(quantity_or_unit_2, to_form=form1)
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
            output = convert(value, to_form=form, parser=parser)
        elif type(unit) is str:
            output = convert(value+' '+unit, to_form=form, parser=parser)
        elif is_unit(unit):
            unit = convert(unit, to_form='string', parser=parser)
            output = convert(value+' '+unit, to_form=form, parser=parser)
    else:
        if unit is None:
            raise ValueError('The input argument "unit" is required.')
        elif type(unit) is not str:
            unit = convert(unit, to_form=form, parser=parser)

        form = digest_form(form)

        try:
            output = dict_make_quantity[form](value, unit)
        except:
            raise NotImplementedError

    return output

def unit(unit_name, form=None, parser=None):

    return convert(unit_name, to_form=form, parser=parser, to_type='unit')

def convert(quantity_or_unit, to_unit=None, to_form=None, parser=None, to_type='quantity'):

    output = None

    form_in = get_form(quantity_or_unit)
    to_form = digest_to_form(to_form)
    parser = digest_parser(parser)

    if to_form is None:
        if form_in == 'string':
            to_form=kernel.default_form
        else:
            to_form=form_in

    if parser is None:
        if form_in == 'string':
            if to_form == 'string':
                parser = kernel.default_parser
            else:
                parser = to_form
        else:
            if to_form is None:
                parser = kernel.default_parser
            else:
                parser = form_in

    output = quantity_or_unit

    if to_type=='quantity':

        if form_in=='string':
            if parser==to_form:
                output = dict_translate[form_in][to_form](output)
                if to_unit is not None:
                    output = dict_convert[to_form](output, to_unit)
            else:
                output = dict_translate[form_in][parser](output)
                if to_unit is not None:
                    output = dict_convert[parser](output, to_unit)
                output = dict_translate[parser][to_form](output)
        else:
            if form_in==to_form:
                if to_unit is not None:
                    if parser==to_form:
                        output = dict_convert[form_in](output, to_unit)
                    else:
                        output = dict_translate[form_in][parser](output)
                        output = dict_convert[parser](output, to_unit)
                        output = dict_translate[parser][to_form](output)
            elif form_in!=to_form:
                if to_unit is not None:
                    if parser==form_in:
                        output = dict_convert[form_in](output, to_unit)
                        output = dict_translate[form_in][to_form](output)
                    elif parser==to_form:
                        output = dict_translate[form_in][to_form](output)
                        output = dict_convert[to_form](output, to_unit)
                    else:
                        output = dict_translate[form_in][parser](output)
                        output = dict_convert[parser](output, to_unit)
                        output = dict_translate[parser][to_form](output)
                else:
                    output = dict_translate[form_in][to_form](output)

    elif to_type=='unit':

        if form_in=='string':
            if parser==to_form:
                if to_unit is None:
                    output = dict_string_to_unit[to_form](output)
                else:
                    output = dict_string_to_quantity[to_form](output)
                    output = dict_convert[to_form](output, to_unit)
                    output = dict_get_unit[to_form](output)
            else:
                if to_unit is None:
                    output = dict_translate[form_in][parser](output)
                    output = dict_get_unit[parser](output)
                    output = dict_translate[parser][to_form](output)
                else:
                    output = dict_translate[form_in][parser](output)
                    output = dict_convert[parser](output, to_unit)
                    output = dict_get_unit[parser](output)
                    output = dict_translate[parser][to_form](output)
        else:
            if form_in==to_form:
                if to_unit is not None:
                    if parser==to_form:
                        output = dict_convert[form_in](output, to_unit)
                    else:
                        output = dict_translate[form_in][parser](output)
                        output = dict_convert[parser](output, to_unit)
                        output = dict_translate[parser][to_form](output)
            elif form_in!=to_form:
                if to_unit is not None:
                    if parser==form_in:
                        output = dict_convert[form_in](output, to_unit)
                        output = dict_translate[form_in][to_form](output)
                    elif parser==to_form:
                        output = dict_translate[form_in][to_form](output)
                        output = dict_convert[to_form](output, to_unit)
                    else:
                        output = dict_translate[form_in][parser](output)
                        output = dict_convert[parser](output, to_unit)
                        output = dict_translate[parser][to_form](output)
                else:
                    output = dict_translate[form_in][to_form](output)
            output = dict_get_unit[to_form](output)

    elif to_type=='value':

        if form_in=='string':
            if parser==to_form:
                output = dict_string_to_quantity[to_form](output)
                if to_unit is not None:
                    output = dict_convert[to_form](output, to_unit)
                output = dict_get_value[to_form](output)
            else:
                output = dict_translate[form_in][parser](output)
                if to_unit is not None:
                    output = dict_convert[parser](output, to_unit)
                output = dict_get_value[parser](output)
        else:
            if form_in==to_form:
                if to_unit is not None:
                    if parser==to_form:
                        output = dict_convert[form_in](output, to_unit)
                        output = dict_get_value[form_in](output)
                    else:
                        output = dict_translate[form_in][parser](output)
                        output = dict_convert[parser](output, to_unit)
                        output = dict_get_value[parser](output)
                else:
                    output = dict_get_value[form_in](output)
            elif form_in!=to_form:
                if to_unit is not None:
                    if parser==form_in:
                        output = dict_convert[form_in](output, to_unit)
                        output = dict_get_value[form_in](output)
                    elif parser==to_form:
                        output = dict_translate[form_in][to_form](output)
                        output = dict_convert[to_form](output, to_unit)
                        output = dict_get_value[to_form](output)
                    else:
                        output = dict_translate[form_in][parser](output)
                        output = dict_convert[parser](output, to_unit)
                        output = dict_get_value[parser](output)
                else:
                    output = dict_get_value[form_in](output)

    else:

        raise ValueError("Argument 'to_type' must take one of the following values: 'quantity', 'unit' or 'value'.")


    return output

def get_standard_units(quantity_or_unit):

    dim = dimensionality(quantity_or_unit)
    solution = np.array([dim[ii] for ii in kernel.order_fundamental_units], dtype=float)
    n_dims_solution = len(kernel.order_fundamental_units) - np.sum(np.isclose(solution, 0.0))

    output = None

    if n_dims_solution == 0:

        for standard_unit, _ in kernel.adimensional_standards.items():
            if compatibility(quantity_or_unit, standard_unit):
                output = standard_unit
                break

    elif n_dims_solution == 1:

        for standard_unit, dim_array in kernel.dimensional_fundamental_standards.items():
            if np.allclose(solution, dim_array):
                output = standard_unit
                break

        if output is None:

            matrix = []
            standard_units = []

            for aux_unit, aux_dim_array in kernel.tentative_base_standards.items():
                standard_units.append(convert(aux_unit, to_type='unit'))
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

        for standard_units, dim_array in kernel.dimensional_combinations_standards.items():
            if np.allclose(solution, dim_array):
                output = standard_units
                break

        if output is None:

            matrix = []
            standard_units = []

            for aux_unit, aux_dim_array in kernel.dimensional_fundamental_standards.items():
                standard_units.append(convert_to(aux_unit, to_type='unit'))
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

            for aux_unit, aux_dim_array in kernel.tentative_base_standards.items():
                standard_units.append(convert_to(aux_unit, to_type='unit'))
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
        output = convert(quantity_or_unit, to_form=to_form)
        standard = get_standard_units(output)
        if standard is None:
            raise ValueError("The input quantity or unit has no standard.")
        output = convert(output, standard)
    except:
        standard = get_standard_units(quantity_or_unit)
        if standard is None:
            raise ValueError("The input quantity or unit has no standard.")
        output = convert(quantity_or_unit, to_unit=standard, to_form=to_form)

    return output


