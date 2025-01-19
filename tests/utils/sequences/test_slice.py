# This file contains test for get_unit, get_value, and get_dimensionality
import pyunitwizard as puw
import pytest

def test_get_value_pint():

    item = puw.quantity([0,1,2,3,4,5], 'm', 'pint')
    item2 = puw.utils.sequences.slice(item, [1,3,4,5])
    output = puw.quantity([1,3,4,5], 'm', 'pint')

    assert puw.are_equal(item2, output, same_form=True)

