from pyunitwizard._private.exceptions import LibraryWithoutParserError
import pyunitwizard as puw
import pytest
import openmm.unit as openmm_unit
import unyt
import numpy as np

def test_concatenate_1():
    puw.configure.reset()
    puw.configure.load_library(['pint', 'openmm.unit'])

    list_quantities = [ puw.quantity(np.zeros([6,3]), 'nm') for ii in range(10)]
    quantity = puw.concatenate(list_quantities, type_value='numpy.ndarray')
    value = puw.get_value(quantity)
    assert value.shape==(10, 6, 3)










