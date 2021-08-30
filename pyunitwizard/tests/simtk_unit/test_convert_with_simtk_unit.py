import pytest
import pyunitwizard as puw

def test_from_string_1_a():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = puw.convert('1 meter')
    q_true = 1*openmm_unit.meter
    assert q == q_true

def test_from_string_2():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = puw.convert('1 meter', to_unit='cm')
    q_true = 100.0*openmm_unit.centimeter
    assert q == q_true

def test_from_string_3():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = puw.convert('1 meter', to_type='unit')
    q_true = openmm_unit.meter
    assert q == q_true

def test_from_string_4():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = puw.convert('1 meter', to_unit='cm', to_type='unit')
    q_true = openmm_unit.centimeter
    assert q == q_true

def test_from_string_5():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = puw.convert('1 meter', to_unit='cm', to_form='string')
    q_true = '100.0 cm'
    assert q == q_true

def test_from_string_6():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = puw.convert('1 meter', to_unit='cm', to_form='string', to_type='unit')
    q_true = 'centimeter'
    assert q == q_true

def test_from_string_7():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = puw.convert('1 meter', to_type='value')
    q_true = 1
    assert q == q_true

def test_from_string_8():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = puw.convert('1 meter', to_unit='cm', to_type='value')
    q_true = 100.0
    assert q == q_true


