"""
PyUnitWizard
This must be a short description of the project
"""

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

# Add imports here
from .main import unit, quantity, get_form, get_value, get_unit, is_quantity, is_unit
from .main import convert, translate, string_to_quantity, string_to_unit, to_string
from .main import get_standard_units, standardize, dimensionality, compatibility
from . import configure as configure
from ._private_tools import default as _default

_default.initialize()

