import pytest
import pyunitwizard as puw

def test_1():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.unit('kJ/mol')
    q_true = ureg.Unit('kJ/mol')
    assert q == q_true


