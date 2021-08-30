import pytest
import pyunitwizard as puw

def test_1():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = puw.unit('kJ/mol')
    q_true = openmm_unit.kilojoule/openmm_unit.mole
    assert q == q_true


