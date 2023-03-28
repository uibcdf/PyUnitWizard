from pyunitwizard._private.exceptions import LibraryWithoutParserError
import pyunitwizard as puw
import pytest
import openmm.unit as openmm_unit
import unyt
import numpy as np

def test_stack_1():
    puw.configure.reset()
    puw.configure.load_library(['pint', 'openmm.unit'])

    list_list_quantities = [ [puw.quantity(ii, 'nm') for ii in range(3)] for jj in range(4)]
    quantity = puw.stack(list_list_quantities, type_value='numpy.ndarray')
    value = puw.get_value(quantity)
    assert value.shape==(4, 3)


