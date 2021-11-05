import pytest
import pyunitwizard as puw

def test_libraries_supported():
    assert puw.configure.get_libraries_supported()==['pint', 'openmm.unit']

def test_libraries_found():
    assert puw.configure.get_libraries_found()==['pint', 'openmm.unit']

def test_load_library():
    puw.configure.reset()
    puw.configure.load_library(['pint', 'openmm.unit'])
    assert puw.configure.get_libraries_loaded()==['pint', 'openmm.unit']

def test_default_form():
    puw.configure.reset()
    puw.configure.load_library(['pint', 'openmm.unit'])
    assert puw.configure.get_default_form()=='pint'

def test_default_parser():
    puw.configure.reset()
    puw.configure.load_library(['pint', 'openmm.unit'])
    assert puw.configure.get_default_parser()=='pint'



