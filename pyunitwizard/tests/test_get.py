# This file contains test for get_unit, get_value, get_dimensionality and
# get_standard_units.

import pyunitwizard as puw
import pytest

puw.configure.reset()
puw.configure.load_library(['pint', 'openmm.unit'])

@pytest.fixture
def pint_unit_registry():
    """ Returns a pint unit registry"""
    return puw.forms.api_pint.ureg

@pytest.fixture
def pint_quantity(pint_unit_registry):
    """ Returns a pint.Quantity"""
    return pint_unit_registry.Quantity(2.5, 'nanometers/picoseconds')

@pytest.fixture
def openmm_quantity():
    """ Returns an openmm quantity"""
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    return 2.5 * openmm_unit.nanometer/openmm_unit.picoseconds


#### Tests for get value ####

def test_get_value_pint(pint_quantity):
    assert puw.get_value(pint_quantity) == 2.5

def test_get_value_openmm():
    pass

def test_get_value_unyt():
    pass

#### Tests for get unit ####

def test_get_unit_pint(pint_unit_registry, pint_quantity):
    unit_true = pint_unit_registry.Unit('nanometers/picoseconds')
    assert puw.get_unit(pint_quantity) == unit_true

def test_get_unit_openmm():
    pass

def test_get_unit_unyt():
    pass

#### Tests for get dimensionality ####

def test_get_dimensionality_pint(pint_quantity):
    assert puw.get_dimensionality(pint_quantity) == {'[L]': 1, '[M]': 0, 
                                                    '[T]': -1, '[K]': 0, 
                                                    '[mol]': 0, '[A]': 0, 
                                                    '[Cd]': 0}

def test_get_dimensionality_openmm(openmm_quantity):
    assert puw.get_dimensionality(openmm_quantity) == {'[L]': 1, '[M]': 0, 
                                                    '[T]': -1, '[K]': 0, 
                                                    '[mol]': 0, '[A]': 0, 
                                                    '[Cd]': 0}

def test_get_dimensionality_unyt():
    pass

### Tests for get standard units ####

def test_get_standard_units_pint():
    pass

def test_get_standard_units_openmm():
    pass

def test_get_standard_units_unyt():
    pass
