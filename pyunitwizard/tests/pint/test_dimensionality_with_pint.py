import pytest
import pyunitwizard as puw

def test_1():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = ureg.Quantity(2.5, 'nanometers/picoseconds')
    assert puw.get_dimensionality(q)=={'[L]': 1, '[M]': 0, '[T]': -1, '[K]': 0, '[mol]': 0, '[A]': 0, '[Cd]': 0}

