from pyunitwizard._private_tools.exceptions import LibraryWithoutParserError
import pyunitwizard as puw
import pytest
import openmm.unit as openmm_unit

def test_similarity_parsing_error():
    
    with pytest.raises(LibraryWithoutParserError):
        puw.configure.reset()
        puw.configure.load_library(['openmm.unit'])
        puw.similarity('1 meter', '1 meter')

def test_similarity_string_quantity():
    puw.configure.reset()
    puw.configure.load_library(['pint', 'openmm.unit'])

    similar = puw.similarity('1 meter', '1 kilometer')
    assert not similar

    similar = puw.similarity('1 meter', '1 cm')
    assert not similar

    similar = puw.similarity('1 meter', '100 cm')
    assert similar

def test_similarity_pint_quantity():
    puw.configure.reset()
    puw.configure.load_library(['pint'])

    quantity_1 = puw.quantity(0.4,'cm', form="pint")
    quantity_2 = puw.quantity(0.4,'cm', form="pint")
    similar = puw.similarity(quantity_1, quantity_2)
    assert similar

    quantity_1 = puw.quantity(4,'mm', form="pint")
    quantity_2 = puw.quantity(0.4,'cm', form="pint")
    similar = puw.similarity(quantity_1, quantity_2)
    assert similar

    quantity_1 = puw.quantity(4,'mm', form="pint")
    quantity_2 = puw.quantity(0.41,'cm', form="pint")
    similar = puw.similarity(quantity_1, quantity_2)
    assert not similar

    quantity_1 = puw.quantity(4,'mm', form="pint")
    quantity_2 = puw.quantity(0.4,'cm', form="pint")
    similar = puw.similarity(quantity_1, quantity_2)
    assert similar

def test_similarity_openmm_quantity():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])

    quantity_1 = puw.quantity(0.4, openmm_unit.centimeter, form="openmm.unit")
    quantity_2 = puw.quantity(0.4, openmm_unit.centimeter, form="openmm.unit")
    similar = puw.similarity(quantity_1, quantity_2)
    assert similar

    quantity_1 = puw.quantity(4, openmm_unit.millimeter, form="openmm.unit")
    quantity_2 = puw.quantity(0.4, openmm_unit.centimeter, form="openmm.unit")
    similar = puw.similarity(quantity_1, quantity_2)
    assert similar

    quantity_1 = puw.quantity(4, openmm_unit.millimeter, form="openmm.unit")
    quantity_2 = puw.quantity(0.41, openmm_unit.centimeter, form="openmm.unit")
    similar = puw.similarity(quantity_1, quantity_2)
    assert not similar

    quantity_1 = puw.quantity(4, openmm_unit.millimeter, form="openmm.unit")
    quantity_2 = puw.quantity(0.4, openmm_unit.centimeter, form="openmm.unit")
    similar = puw.similarity(quantity_1, quantity_2)
    assert similar









