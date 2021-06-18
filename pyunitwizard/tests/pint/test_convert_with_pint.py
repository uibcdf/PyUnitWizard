import pytest
import pyunitwizard as puw

## from string

def test_from_string_1():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.convert('1 meter')
    q_true = ureg.Quantity(1, 'meter')
    assert q == q_true

def test_from_string_2():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.convert('1 meter', to_unit='cm')
    q_true = ureg.Quantity(100.0, 'centimeter')
    assert q == q_true

def test_from_string_3():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.convert('1 meter', to_type='unit')
    q_true = ureg.Unit('meter')
    assert q == q_true

def test_from_string_4():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.convert('1 meter', to_unit='cm', to_type='unit')
    q_true = ureg.Unit('centimeter')
    assert q == q_true

def test_from_string_5():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.convert('1 meter', to_unit='cm', to_form='string')
    q_true = '100.0 centimeter'
    assert q == q_true

def test_from_string_6():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.convert('1 meter', to_unit='cm', to_form='string', to_type='unit')
    q_true = 'centimeter'
    assert q == q_true

def test_from_string_7():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.convert('1 meter', to_type='value')
    q_true = 1
    assert q == q_true

def test_from_string_8():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.convert('1 meter', to_unit='cm', to_type='value')
    q_true = 100.0
    assert q == q_true

def test_from_string_9():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.convert('100 angstroms**3', to_form='string', to_type='unit')
    q_true = 'angstrom ** 3'
    assert q == q_true

def test_from_string_10():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = puw.quantity('100 angstroms**3')
    q = puw.convert(q, to_form='string', to_type='unit')
    q_true = 'angstrom ** 3'
    assert q == q_true

## to_pint

def test_to_pint_1():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    q = ureg.Quantity(2.5, 'nanometers/picoseconds')
    q = puw.convert(q, to_unit='angstroms/picoseconds')
    q_true = ureg.Quantity(25.0, 'angstroms/picoseconds')
    assert q == q_true


## to_simtk_unit

def test_to_simtk_unit_1():
    puw.configure.reset()
    puw.configure.load_library(['pint','simtk.unit'])
    ureg = puw.forms.api_pint.ureg
    simtk_unit = puw.forms.api_simtk_unit.simtk_unit
    q = ureg.Quantity(2.5, 'nanometers/picoseconds')
    q = puw.convert(q, to_form='simtk.unit')
    q_true = 2.5 * simtk_unit.nanometer/simtk_unit.picosecond
    assert q == q_true

