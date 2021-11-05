import pytest
import pyunitwizard as puw

def test_1():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = puw.quantity(10, 'kJ/mol')
    q_true = 10*openmm_unit.kilojoule/openmm_unit.mole
    assert puw.similarity(q, q_true)


