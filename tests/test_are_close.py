from pyunitwizard._private.exceptions import LibraryWithoutParserError
import pyunitwizard as puw
import pytest
import openmm.unit as openmm_unit
import unyt

def test_are_close_parsing_error():
    
    with pytest.raises(LibraryWithoutParserError):
        puw.configure.reset()
        puw.configure.load_library(['openmm.unit'])
        puw.are_close('1 meter', '1 meter')

def test_are_close_string_quantity():
    puw.configure.reset()
    puw.configure.load_library(['pint', 'openmm.unit'])

    close = puw.are_close('1 meter', '1 kilometer')
    assert not close

    close = puw.are_close('1 meter', '1 cm')
    assert not close

    close = puw.are_close('1 meter', '100 cm')
    assert close

def test_are_close_pint_quantity():
    puw.configure.reset()
    puw.configure.load_library(['pint'])

    quantity_1 = puw.quantity(0.4,'cm', form="pint")
    quantity_2 = puw.quantity(0.4,'cm', form="pint")
    close = puw.are_close(quantity_1, quantity_2)
    assert close

    quantity_1 = puw.quantity(4,'mm', form="pint")
    quantity_2 = puw.quantity(0.4,'cm', form="pint")
    close = puw.are_close(quantity_1, quantity_2)
    assert close

    quantity_1 = puw.quantity(4,'mm', form="pint")
    quantity_2 = puw.quantity(0.41,'cm', form="pint")
    close = puw.are_close(quantity_1, quantity_2)
    assert not close

    quantity_1 = puw.quantity(4,'m', form="pint")
    quantity_2 = puw.quantity(4,'cm', form="pint")
    close = puw.are_close(quantity_1, quantity_2)
    assert not close

def test_are_close_openmm_quantity():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])

    quantity_1 = puw.quantity(0.4, openmm_unit.centimeter, form="openmm.unit")
    quantity_2 = puw.quantity(0.4, openmm_unit.centimeter, form="openmm.unit")
    close = puw.are_close(quantity_1, quantity_2)
    assert close

    quantity_1 = puw.quantity(4, openmm_unit.millimeter, form="openmm.unit")
    quantity_2 = puw.quantity(0.4, openmm_unit.centimeter, form="openmm.unit")
    close = puw.are_close(quantity_1, quantity_2)
    assert close

    quantity_1 = puw.quantity(4, openmm_unit.millimeter, form="openmm.unit")
    quantity_2 = puw.quantity(0.41, openmm_unit.centimeter, form="openmm.unit")
    close = puw.are_close(quantity_1, quantity_2)
    assert not close

    quantity_1 = puw.quantity(1, openmm_unit.meter, form="openmm.unit")
    quantity_2 = puw.quantity(1, openmm_unit.centimeter, form="openmm.unit")
    close = puw.are_close(quantity_1, quantity_2)
    assert not close

def test_are_close_unyt_quantity():
    puw.configure.reset()
    puw.configure.load_library(['unyt'])

    quantity_1 = puw.quantity(0.4, unyt.cm, form="unyt")
    quantity_2 = puw.quantity(0.4, unyt.cm, form="unyt")
    close = puw.are_close(quantity_1, quantity_2)
    assert close

    quantity_1 = puw.quantity(4, unyt.mm, form="unyt")
    quantity_2 = puw.quantity(0.4, unyt.cm, form="unyt")
    close = puw.are_close(quantity_1, quantity_2)
    assert close

    quantity_1 = puw.quantity(4, unyt.mm, form="unyt")
    quantity_2 = puw.quantity(0.41, unyt.cm, form="unyt")
    close = puw.are_close(quantity_1, quantity_2)
    assert not close

    quantity_1 = puw.quantity(4, unyt.m, form="unyt")
    quantity_2 = puw.quantity(4, unyt.cm, form="unyt")
    close = puw.are_close(quantity_1, quantity_2)
    assert not close










