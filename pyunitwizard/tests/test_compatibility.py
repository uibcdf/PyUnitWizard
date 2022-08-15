import pyunitwizard as puw
import openmm.unit as openmm_unit
import unyt

def test_compatibility_pint():

    q1 = puw.quantity(2.5, 'nanometers/picoseconds', form="pint")
    q2 = puw.convert(q1, to_unit='angstroms/picoseconds', to_form="pint")
    assert puw.compatibility(q1, q2)

    q1 = puw.quantity(2.5, 'joules/picoseconds',    form="pint")
    q2 = puw.quantity(2.8, 'angstroms/picoseconds', form="pint")
    assert not puw.compatibility(q1, q2)

def test_compatibility_openmm():

    q1 = puw.quantity(2.5, openmm_unit.nanometer/openmm_unit.picosecond, form="openmm.unit")
    q2 = puw.quantity(3.0, openmm_unit.angstrom/openmm_unit.second,  form="openmm.unit")
    assert puw.compatibility(q1, q2)

    q1 = puw.quantity(2.5, openmm_unit.joule/openmm_unit.second, form="openmm.unit")
    q2 = puw.quantity(3.0, openmm_unit.angstrom/openmm_unit.second,  form="openmm.unit")
    assert not puw.compatibility(q1, q2)

def test_compatibility_unyt():

    q1 = puw.quantity(2.5, unyt.nm/unyt.ps, form="unyt")
    q2 = puw.quantity(3.0, unyt.m/unyt.second,  form="unyt")
    assert puw.compatibility(q1, q2)

    q1 = puw.quantity(2.5, unyt.J/unyt.second, form="unyt")
    q2 = puw.quantity(3.0, unyt.m/unyt.second,  form="unyt")
    assert not puw.compatibility(q1, q2)
