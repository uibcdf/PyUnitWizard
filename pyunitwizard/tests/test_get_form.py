import pytest
import pyunitwizard as puw

def test_string():
    puw.configure.reset()
    assert puw.get_form('1 meter')=='string'

def test_pint_quantity():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = ureg.Quantity(1.0,'meter')
    assert puw.get_form(q)=='pint'

def test_pint_unit():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.forms.api_pint.ureg.Unit('meter')
    assert puw.get_form(q)=='pint'

