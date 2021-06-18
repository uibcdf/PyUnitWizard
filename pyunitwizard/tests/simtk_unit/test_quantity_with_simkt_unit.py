import pytest
import pyunitwizard as puw

def test_1():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    simtk_unit = puw.forms.api_simtk_unit.simtk_unit
    q = puw.quantity(10, 'kJ/mol')
    q_true = 10*simtk_unit.kilojoule/simtk_unit.mole
    assert puw.similarity(q, q_true)


