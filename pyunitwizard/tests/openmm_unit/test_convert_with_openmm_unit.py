import pytest
import pyunitwizard as puw
import openmm.unit as openmm_unit

def test_from_string_1():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit', 'pint'])
    q = puw.convert(1*openmm_unit.meter, to_form='pint')
    q_form = puw.get_form(q)
    assert q_form == 'pint'

def test_from_string_2():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit', 'pint'])
    puw.configure.set_default_parser('pint')
    q = puw.convert(1*openmm_unit.meter, to_unit='cm')
    q_true = 100.0*openmm_unit.centimeter
    assert q == q_true

def test_from_string_3():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    q = puw.convert(1*openmm_unit.meter, to_type='unit')
    q_true = openmm_unit.meter
    assert q == q_true

def test_from_string_4():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    q = puw.convert(1*openmm_unit.meter, to_unit=openmm_unit.centimeter, to_type='unit')
    q_true = openmm_unit.centimeter
    assert q == q_true

def test_from_string_5():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    q = puw.convert(1*openmm_unit.meter, to_unit=openmm_unit.centimeter, to_form='string')
    q_true = '100.0 cm'
    assert q == q_true

def test_from_string_6():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    q = puw.convert(1*openmm_unit.meter, to_unit=openmm_unit.centimeter, to_form='string', to_type='unit')
    q_true = 'centimeter'
    assert q == q_true

def test_from_string_7():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    q = puw.convert(1*openmm_unit.meter, to_type='value')
    q_true = 1
    assert q == q_true

def test_from_string_8():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])
    q = puw.convert(1*openmm_unit.meter, to_unit=openmm_unit.centimeter, to_type='value')
    q_true = 100.0
    assert q == q_true


