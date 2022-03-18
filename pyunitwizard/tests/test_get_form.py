import pyunitwizard as puw
import openmm.unit as openmm_unit

puw.configure.reset()
puw.configure.load_library(['pint', 'openmm.unit'])

def test_string():
    assert puw.get_form('1 meter')=='string'

def test_pint_quantity():
    
    ureg = puw.forms.api_pint.ureg
    q = ureg.Quantity(1.0,'meter')
    assert puw.get_form(q)=='pint'

def test_pint_unit():
   
    ureg = puw.forms.api_pint.ureg
    q = puw.forms.api_pint.ureg.Unit('meter')
    assert puw.get_form(q)=='pint'

def test_openmm_unit():
    
    assert puw.get_form(openmm_unit.meter) == "openmm.unit"
    assert puw.get_form(openmm_unit.ampere) == "openmm.unit"

def test_openmm_quantity():

    quantity = 1 * openmm_unit.meter
    assert puw.get_form(quantity) == "openmm.unit"

    quantity = 4.0 * openmm_unit.ampere
    assert puw.get_form(quantity) == "openmm.unit"

    quantity = [2.0, 3.0] * openmm_unit.second
    assert puw.get_form(quantity) == "openmm.unit"
