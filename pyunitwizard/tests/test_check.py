import pytest
import pyunitwizard as puw
import numpy as np

def test_1():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    aa = puw.quantity(0.4,'cm')
    output = puw.check(aa, value_type=float)
    assert output == True

def test_2():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    aa = puw.quantity(0.4,'cm')
    output = puw.check(aa, unit='cm')
    assert output == True

def test_3():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    aa = puw.quantity(0.4,'cm')
    output = puw.check(aa, dimensionality={'[L]':1})
    assert output == True

def test_4():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    aa = puw.quantity(np.zeros([3,3]),'nm/ps')
    output = puw.check(aa, dimensionality={'[L]':1, '[T]':-1}, value_type=np.ndarray, dtype_name='float64')
    assert output == True

def test_5():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    aa = puw.quantity(np.zeros([3,3]),'nm/ps')
    output = puw.check(aa, dimensionality={'[L]':1, '[T]':-1}, value_type=np.ndarray, dtype_name='int')
    assert output == False

def test_6():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    aa = puw.quantity([0,0,0], 'nm/ps')
    output = puw.check(aa, dimensionality={'[L]':1, '[T]':-1}, value_type=np.ndarray, shape=(3,))
    assert output == True

