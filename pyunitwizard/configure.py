from importlib.util import find_spec
from .forms import load_library as load_library
from .forms import loaded_libraries as loaded
from ._private_tools import default
from ._private_tools.forms import digest_form
from .main import string_to_unit, dimensionality

libraries = ['pint', 'simtk.unit', 'unyt']
found = { ii: find_spec(ii) is not None for ii in libraries}

def libraries_loaded():

    return loaded

def libraries_supported():

    return libraries

def libraries_found():

    output = [ii for ii in libraries if found[ii]]

    return output

def load_libraries(library_names):

    if type(library_names) is str:
        library_names = list(library_names)

    for ii in range(len(library_names)):
        library_names[ii]=digest_form(library_names[ii])

    for library in library_names:
        if found[library] and (library not in loaded):
            load_library(library)

    if default.form is None:
        default.form = library_names[0]

    pass

def get_default_form():

    return default.form

def set_default_form(form):

    form = digest_form(form)
    default.form = form

    pass

def get_default_standards():

    return default.standards

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

