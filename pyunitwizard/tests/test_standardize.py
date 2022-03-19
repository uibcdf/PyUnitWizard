# This file contains test for get_standard_units and standardize
import pyunitwizard as puw
from pyunitwizard._private_tools.exceptions import NoStandardError
import openmm.unit as openmm_unit
import pytest
import numpy as np
import unyt

### Tests for get standard units ####

def test_raises_no_standard_error():
    puw.configure.reset()
    puw.configure.load_library(['pint'])

    with pytest.raises(NoStandardError):
        quantity = puw.quantity(value=3.0, unit='radian', form='pint')
        puw.get_standard_units(quantity)
    
    with pytest.raises(NoStandardError):
        quantity = puw.quantity(value=3.0, unit='meter', form='pint')
        puw.get_standard_units(quantity)

def test_get_standard_units_pint_quantity():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    puw.configure.set_standard_units(['nm', 'ps', 'kcal', 'mole'])

    quantity = puw.quantity(value=[3.0, 5.0, 5.0], unit='joules', form='pint')
    standard_unit = puw.get_standard_units(quantity)
    assert standard_unit == "kcal"


def test_get_standard_units_openmm_quantity():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    puw.configure.set_standard_units([openmm_unit.meter, openmm_unit.second, openmm_unit.joule])

    quantity = puw.quantity(value=5.0, unit=openmm_unit.centimeter/openmm_unit.picosecond, form='openmm.unit')
    standard_unit = puw.get_standard_units(quantity)
    assert standard_unit == "meter/second"

def test_get_standard_units_unyt_quantity():
    puw.configure.reset()
    puw.configure.load_library(['unyt'])
    puw.configure.set_standard_units([unyt.m, unyt.s, unyt.J])

    quantity = puw.quantity(value=5.0, unit=unyt.cm/unyt.ps, form='unyt')
    standard_unit = puw.get_standard_units(quantity)
    assert standard_unit == "m/s"


### Tests for standardize ###

def test_standardize_pint_quantity():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    puw.configure.set_standard_units(['nm', 'ps', 'kcal', 'mole'])

    quantity = puw.quantity(1.0, "meter", form="pint")
    quantity = puw.standardize(quantity)
    assert np.allclose(puw.get_value(quantity), 1e9)
    assert quantity.units == "nanometer"

    quantity = puw.quantity([1e-12, 2e-12], "second", form="pint")
    quantity = puw.standardize(quantity)
    assert np.allclose(puw.get_value(quantity), [1.0, 2.0])
    assert quantity.units == "picosecond"

def test_standardize_openmm_quantity():
    puw.configure.reset()
    puw.configure.load_library(['pint', 'openmm.unit'])
    puw.configure.set_standard_units(['nm', 'ps', 'kcal', 'mole'])

    quantity = puw.quantity(1.0, openmm_unit.meter, form="openmm.unit")
    quantity = puw.standardize(quantity)
    assert np.allclose(puw.get_value(quantity), 1e9)
    assert puw.get_unit(quantity) == "nanometer"

    quantity = puw.quantity([1e-12, 2e-12], openmm_unit.second, form="openmm.unit")
    quantity = puw.standardize(quantity)
    assert np.allclose(puw.get_value(quantity), [1.0, 2.0])
    assert puw.get_unit(quantity) == "picosecond"

def test_standardize_unyt_quantity():
    puw.configure.reset()
    puw.configure.load_library(['pint', 'unyt'])
    puw.configure.set_standard_units(['nm', 'ps', 'kcal', 'mole'])

    quantity = puw.quantity(1.0, unyt.m, form="unyt")
    quantity = puw.standardize(quantity)
    assert np.allclose(puw.get_value(quantity), 1e9)
    assert puw.get_unit(quantity) == "nm"

    quantity = puw.quantity([1e-12, 2e-12], unyt.s, form="unyt")
    quantity = puw.standardize(quantity)
    assert np.allclose(puw.get_value(quantity), [1.0, 2.0])
    assert puw.get_unit(quantity) == "ps"