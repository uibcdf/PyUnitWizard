from pyunitwizard.parse import _parse_with_pint, parse
import numpy as np
import pyunitwizard as puw

def test_parse_with_pint_scalar():

    quantity = _parse_with_pint("5 meters")
    assert quantity.magnitude == 5
    assert str(quantity.units) == "meter"

def test_parse_with_pint_array():

    quantity = _parse_with_pint("[2] mole")
    assert np.allclose(quantity.magnitude, np.array([2]))
    assert str(quantity.units) == "mole"

    quantity = _parse_with_pint("[2, 5, 7] joules")
    assert np.allclose(quantity.magnitude, np.array([2, 5, 7]))
    assert str(quantity.units) == "joule"

    quantity = _parse_with_pint("(3, 2, 1) meters")
    assert np.allclose(quantity.magnitude, np.array([3, 2, 1]))
    assert str(quantity.units) == "meter"

    quantity = _parse_with_pint("[[2, 5, 7], [7, 8, 9]] kilojoules/(mol*nanometer)")
    assert np.allclose(quantity.magnitude, np.array([[2, 5, 7], [7, 8, 9]]))
    assert str(quantity.units) == "kilojoule / mole / nanometer"

def test_parse_to_pint():
    
    quantity = parse("[2, 5, 7] joules", to_form="pint")
    assert np.allclose(quantity.magnitude, np.array([2, 5, 7]))
    assert str(quantity.units) == "joule"

def test_parse_to_string():

    quantity = _parse_with_pint("5 meters")
    assert quantity.magnitude == 5
    assert str(quantity.units) == "meter"

    quantity = parse("5 meter", to_form="string")
    assert isinstance(quantity, str)
    assert quantity == "5 meter"

    quantity = parse("[2, 5, 7] joules", to_form="string")
    assert isinstance(quantity, str)
    assert quantity == "[2 5 7] joule"

def test_parse_to_openmm_scalar():

    quantity = parse("5 meters", to_form="openmm.unit")
    assert quantity._value == 5
    assert str(quantity.unit) == "meter"

def test_parse_to_openmm_array():

    quantity = parse("[2, 5, 7] joules", to_form="openmm.unit")
    assert np.allclose(quantity._value, np.array([2, 5, 7]))
    assert str(quantity.unit) == "joule"

    quantity = parse("(3, 2, 1) meters", to_form="openmm.unit")
    assert np.allclose(quantity._value, np.array([3, 2, 1]))
    assert str(quantity.unit) == "meter"

    quantity = parse("[[2, 5, 7], [7, 8, 9]] joules", to_form="openmm.unit")
    assert np.allclose(quantity._value, np.array([[2, 5, 7], [7, 8, 9]]))
    assert str(quantity.unit) == "joule"


def test_parse_to_unyt():

    quantity = parse("5 meters", to_form="unyt")
    assert quantity.value == 5
    assert str(quantity.units) == "m"

    quantity = parse("[2, 5, 7] joules", to_form="unyt")
    assert np.allclose(quantity.value, np.array([2, 5, 7]))
    assert str(quantity.units) == "J"

    quantity = parse("(3, 2, 1) meters", to_form="unyt")
    assert np.allclose(quantity.value, np.array([3, 2, 1]))
    assert str(quantity.units) == "m"

    quantity = parse("[[2, 5, 7], [7, 8, 9]] joules", to_form="unyt")
    assert np.allclose(quantity.value, np.array([[2, 5, 7], [7, 8, 9]]))
    assert str(quantity.units) == "J"
