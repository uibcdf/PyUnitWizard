"""
PyUnitWizard
Quantities and units assistant
"""

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

__documentation_web__ = 'https://www.uibcdf.org/PyUnitWizard'
__github_web__ = 'https://github.com/uibcdf/PyUnitWizard'
__github_issues_web__ = __github_web__ + '/issues'

# Add imports here
from .main import unit, quantity, get_form, get_value, get_unit, is_quantity, is_unit
from .main import convert
from .main import get_standard_units, standardize, get_dimensionality, compatibility, similarity, check
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

