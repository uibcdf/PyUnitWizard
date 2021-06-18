import pytest
import pyunitwizard as puw

def test_from_string_1_a():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    simtk_unit = puw.forms.api_simtk_unit.simtk_unit
    q = puw.convert('1 meter')
    q_true = 1*simtk_unit.meter
    assert q == q_true

def test_from_string_2():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    simtk_unit = puw.forms.api_simtk_unit.simtk_unit
    q = puw.convert('1 meter', to_unit='cm')
    q_true = 100.0*simtk_unit.centimeter
    assert q == q_true

def test_from_string_3():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    simtk_unit = puw.forms.api_simtk_unit.simtk_unit
    q = puw.convert('1 meter', to_type='unit')
    q_true = simtk_unit.meter
    assert q == q_true

def test_from_string_4():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    simtk_unit = puw.forms.api_simtk_unit.simtk_unit
    q = puw.convert('1 meter', to_unit='cm', to_type='unit')
    q_true = simtk_unit.centimeter
    assert q == q_true

def test_from_string_5():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    simtk_unit = puw.forms.api_simtk_unit.simtk_unit
    q = puw.convert('1 meter', to_unit='cm', to_form='string')
    q_true = '100.0 cm'
    assert q == q_true

def test_from_string_6():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    simtk_unit = puw.forms.api_simtk_unit.simtk_unit
    q = puw.convert('1 meter', to_unit='cm', to_form='string', to_type='unit')
    q_true = 'centimeter'
    assert q == q_true

def test_from_string_7():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    simtk_unit = puw.forms.api_simtk_unit.simtk_unit
    q = puw.convert('1 meter', to_type='value')
    q_true = 1
    assert q == q_true

def test_from_string_8():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    simtk_unit = puw.forms.api_simtk_unit.simtk_unit
    q = puw.convert('1 meter', to_unit='cm', to_type='value')
    q_true = 100.0
    assert q == q_true


