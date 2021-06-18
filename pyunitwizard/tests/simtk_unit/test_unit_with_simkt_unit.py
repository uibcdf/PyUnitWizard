import pytest
import pyunitwizard as puw

def test_1():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    simtk_unit = puw.forms.api_simtk_unit.simtk_unit
    q = puw.unit('kJ/mol')
    q_true = simtk_unit.kilojoule/simtk_unit.mole
    assert q == q_true


