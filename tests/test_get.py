# This file contains test for get_unit, get_value, and get_dimensionality
import pyunitwizard as puw
import pytest
import unyt

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

@pytest.fixture
def unyt_quantity():
    """Returns a unyt quantity"""
    return 2.5 * unyt.nm/unyt.ps

#### Tests for get value ####

def test_get_value_pint(pint_quantity):
    assert puw.get_value(pint_quantity) == 2.5

def test_get_value_openmm(openmm_quantity):
    assert puw.get_value(openmm_quantity) == 2.5

def test_get_value_unyt(unyt_quantity):
    assert puw.get_value(unyt_quantity) == 2.5

#### Tests for get unit ####

def test_get_unit_pint(pint_unit_registry, pint_quantity):
    unit_true = pint_unit_registry.Unit('nanometers/picoseconds')
    assert puw.get_unit(pint_quantity) == unit_true

def test_get_unit_openmm(openmm_quantity):
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    unit = puw.get_unit(openmm_quantity)
    assert isinstance(unit, openmm_unit.Unit)
    assert str(unit) == "nanometer/picosecond"

def test_get_unit_unyt(unyt_quantity):
    unit = puw.get_unit(unyt_quantity)
    assert isinstance(unit, unyt.Unit)
    assert str(unit) == "nm/ps"

#### Tests for get value and unit ####

def test_get_value_and_unit_pint(pint_unit_registry, pint_quantity):
    unit_true = pint_unit_registry.Unit('nanometers/picoseconds')
    value_true = 2.5
    value, unit = puw.get_value_and_unit(pint_quantity)
    assert value == value_true
    assert unit == unit_true

def test_get_value_and_unit_openmm(openmm_quantity):
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    value, unit = puw.get_value_and_unit(openmm_quantity)
    value_true = 2.5
    assert isinstance(unit, openmm_unit.Unit)
    assert str(unit) == "nanometer/picosecond"
    assert value == value_true

def test_get_value_and_unit_unyt(unyt_quantity):
    value, unit = puw.get_value_and_unit(unyt_quantity)
    value_true = 2.5
    assert isinstance(unit, unyt.Unit)
    assert str(unit) == "nm/ps"
    assert value == value_true

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

def test_get_dimensionality_unyt(unyt_quantity):
    assert puw.get_dimensionality(unyt_quantity) == {'[L]': 1, '[M]': 0, 
                                                    '[T]': -1, '[K]': 0, 
                                                    '[mol]': 0, '[A]': 0, 
                                                    '[Cd]': 0}
