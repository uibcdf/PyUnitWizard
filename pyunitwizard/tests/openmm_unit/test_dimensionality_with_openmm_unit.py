import pytest
import pyunitwizard as puw

def test_1():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = 2.5*openmm_unit.nanometer/openmm_unit.picoseconds
    assert puw.get_dimensionality(q)=={'[L]': 1, '[M]': 0, '[T]': -1, '[K]': 0, '[mol]': 0, '[A]': 0, '[Cd]': 0}

