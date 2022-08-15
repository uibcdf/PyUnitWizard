import pyunitwizard as puw
import openmm.unit as openmm_unit
import unyt

def test_string():
    assert puw.get_form('1 meter')=='string'

def test_pint_quantity():
    
    ureg = puw.forms.api_pint.ureg
    quantity = ureg.Quantity(1.0,'meter')
    assert puw.get_form(quantity)=='pint'

def test_pint_unit():
   
    ureg = puw.forms.api_pint.ureg
    unit = ureg.Unit('meter')
    assert puw.get_form(unit)=='pint'

def test_openmm_unit():
    
    assert puw.get_form(openmm_unit.meter/openmm_unit.second) == "openmm.unit"
    assert puw.get_form(openmm_unit.ampere) == "openmm.unit"

def test_openmm_quantity():

    quantity = 1 * openmm_unit.meter
    assert puw.get_form(quantity) == "openmm.unit"

    quantity = 4.0 * openmm_unit.ampere
    assert puw.get_form(quantity) == "openmm.unit"

    quantity = [2.0, 3.0] * openmm_unit.second
    assert puw.get_form(quantity) == "openmm.unit"

def test_unyt_unit():
    assert puw.get_form(unyt.m/unyt.s) == "unyt"
    assert puw.get_form(unyt.A) == "unyt"

def test_unyt_quantity():

    quantity = 1 * unyt.m
    assert puw.get_form(quantity) == "unyt"

    quantity = 4.0 * unyt.A
    assert puw.get_form(quantity) == "unyt"

    quantity = [2.0, 3.0] * unyt.s
    assert puw.get_form(quantity) == "unyt"
