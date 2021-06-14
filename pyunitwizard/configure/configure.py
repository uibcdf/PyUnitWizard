from importlib.util import find_spec
from pyunitwizard import forms
from pyunitwizard import default
from pyunitwizard._private_tools.forms import digest_form
from pyunitwizard.main import string_to_unit, dimensionality
import numpy as np

libraries = ['pint', 'simtk.unit']
parsers = ['pint', 'simtk.unit']
found = { ii: find_spec(ii) is not None for ii in libraries}

def get_libraries_loaded():

    return forms.loaded_libraries

def get_libraries_supported():

    return libraries

def get_parsers_loaded():

    return forms.loaded_parsers

def get_parsers_supported():

    return parsers

def libraries_found():

    output = [ii for ii in libraries if found[ii]]

    return output

def load_library(library_names):

    if type(library_names) is str:
        library_names = list(library_names)

    for ii in range(len(library_names)):
        library_names[ii]=digest_form(library_names[ii])

    for library in library_names:
        if found[library] and (library not in forms.loaded_libraries):
            forms.load_library(library)

    if default.form is None:
        default.form = library_names[0]

    pass

def get_default_form():

    return default.form

def set_default_form(form):

    form = digest_form(form)
    default.form = form

    pass

def get_standard_units():

    return default.standards

def set_standard_units(standard_units):

    default.standards={}
    default.dimensional_fundamental_standards={}
    default.dimensional_combinations_standards={}
    default.adimensional_standards={}

    n_dimensions = len(default.order_fundamental_units)

    if type(standard_units) is str:
        standard_units=[standard_units]
    elif type(standard_units) not in [list, tuple]:
        raise ValueError

    for standard_unit in standard_units:


        dim = dimensionality(string_to_unit(standard_unit))
        dim_array = np.array([dim[ii] for ii in default.order_fundamental_units], dtype=float)
        n_dims_array = n_dimensions - np.isclose(dim_array,0.0).sum()

        if n_dims_array == 1:

            default.dimensional_fundamental_standards[standard_unit] = dim_array

        elif n_dims_array == 0:

            default.adimensional_standards[standard_unit] = dim_array

        else:

            default.dimensional_combinations_standards[standard_unit] = dim_array

        default.standards[standard_unit] = dim

    # Tentative base standards

    default.tentative_base_standards=default.dimensional_fundamental_standards.copy()

    already = np.zeros(shape=n_dimensions)
    for unit, array in default.tentative_base_standards.items():
        already += array

    for ii in range(n_dimensions):
        if np.isclose(already[ii],0):
            candidate = None
            candidate_array = None
            candidate_n_dims = np.inf
            candidate_n_ii = np.inf
            for standard_unit, array in default.dimensional_combinations_standards.items():
                if array[ii]>0:
                    if array[ii]<candidate_n_ii:
                        candidate = standard_unit
                        candidate_array = array
                        candidate_n_dis = (n_dimensions - np.isclose(array,0.0).sum())
                        candidate_n_ii = array[ii]
                    elif np.isclose(array[ii],candidate_n_ii):
                        if (n_dimensions - np.isclose(array,0.0).sum()) <candidate_n_dims:
                            candidate = standard_unit
                            candidate_array = array
                            candidate_n_dis = (n_dimensions - np.isclose(array,0.0).sum())
                            candidate_n_ii = array[ii]

            if candidate is not None:
                default.tentative_base_standards[candidate] = candidate_array
                for jj in range(ii, n_dimensions):
                    if candidate_array[jj]>0:
                        already[jj]=1

    pass


