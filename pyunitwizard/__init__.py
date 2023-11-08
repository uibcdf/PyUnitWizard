"""
PyUnitWizard
Quantities and units assistant
"""

# versioningit
from ._version import __version__

# Add imports here
from .constants import constants as _constants
from .constants import constants_synonyms as _constants_synonyms
from .main import unit, quantity, get_form, is_quantity, is_unit
from .main import get_value, get_unit, get_value_and_unit, change_value
from .main import convert
from .main import get_standard_units, standardize, get_dimensionality
from .main import concatenate, stack, hstack, vstack
from .main import are_compatible, are_equal, are_close, check
from .main import get_constant, show_constants
from . import configure
from . import kernel as _kernel

_kernel.initialize()

try:
    import pint
    configure.load_library('pint')
except:
    pass

try:
    import openmm.unit as openmm_unit
    configure.load_library('openmm.unit')
except:
    pass

try:
    import unyt
    configure.load_library('unyt')
except:
    pass

