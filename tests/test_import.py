"""
Unit and regression test for the pyunitwizard package.
"""

# Import package, test suite, and other packages as needed
import pyunitwizard
import pytest
import sys

def test_pyunitwizard_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "pyunitwizard" in sys.modules
