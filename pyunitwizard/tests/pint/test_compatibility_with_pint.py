import pytest
import pyunitwizard as puw

def test_1():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.quantity(2.5, 'nanometers/picoseconds')
    q2 = puw.convert(q, to_unit='angstroms/picoseconds')
    output = puw.compatibility(q,q2)
    assert output == True

