import pyunitwizard as puw
import openmm.unit as openmm_unit

def test_convert_from_openmm_to_pint():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit', 'pint'])
    quantity = puw.convert(1*openmm_unit.meter, to_form='pint')
    assert puw.get_form(quantity) == 'pint'

def test_convert_from_openmm_to_openmm():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit', 'pint'])
    puw.configure.set_default_parser('pint')
    
    quantity = puw.convert(1*openmm_unit.meter, to_unit='cm')
    assert quantity == 100.0*openmm_unit.centimeter

    quantity = puw.convert(1*openmm_unit.meter, to_type='unit')
    assert quantity == openmm_unit.meter

    quantity = puw.convert(1*openmm_unit.meter, to_unit=openmm_unit.centimeter, to_type='unit')
    assert quantity == openmm_unit.centimeter

    quantity = puw.convert(1*openmm_unit.meter, to_type='value')
    assert quantity == 1

    quantity = puw.convert(1*openmm_unit.meter, to_unit=openmm_unit.centimeter, to_type='value')
    assert quantity == 100.0

def test_convert_from_openmm_to_string():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])

    quantity = puw.convert(1*openmm_unit.meter, to_unit=openmm_unit.centimeter, to_form='string')
    assert quantity == '100.0 cm'

    quantity = puw.convert(1*openmm_unit.meter, to_unit=openmm_unit.centimeter, to_form='string', to_type='unit')
    assert quantity == 'centimeter'


