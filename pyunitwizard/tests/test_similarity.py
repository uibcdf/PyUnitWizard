import pytest
import pyunitwizard as puw

def test_1():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    output = puw.similarity('1 meter', '1 meter')
    assert output == True

def test_2():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    output = puw.similarity('1 meter', '1 kilometer')
    assert output == False

def test_3():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    output = puw.similarity('1 meter', '1 cm')
    assert output == False

def test_4():
    puw.configure.reset()
    puw.configure.load_library(['simtk.unit'])
    output = puw.similarity('1 meter', '100 cm')
    assert output == True

def test_5():
    puw.configure.reset()
    puw.configure.load_library(['pint','simtk.unit'])
    aa = puw.quantity(0.4,'cm')
    bb = puw.quantity(0.4,'cm')
    output = puw.similarity(aa, bb)
    assert output == True

def test_5():
    puw.configure.reset()
    puw.configure.load_library(['pint','simtk.unit'])
    aa = puw.quantity(4,'mm')
    bb = puw.quantity(0.4,'cm')
    output = puw.similarity(aa, bb)
    assert output == True

def test_6():
    puw.configure.reset()
    puw.configure.load_library(['pint','simtk.unit'])
    aa = puw.quantity(4,'mm')
    bb = puw.quantity(0.41,'cm')
    output = puw.similarity(aa, bb)
    assert output == False



