import pyunitwizard as puw

puw.configure.reset()
puw.configure.load_library(['pint', 'openmm.unit'])

def test_compatibility_pint():

    q1 = puw.quantity(2.5, 'nanometers/picoseconds', form="pint")
    q2 = puw.convert(q1, to_unit='angstroms/picoseconds', to_form="pint")
    assert puw.compatibility(q1, q2)


def test_compatibility_openmm():
    
    q1 = puw.quantity(2.5, 'nanometers/picoseconds', form="openmm.unit")
    q2 = puw.quantity(3.0, 'angstroms/seconds',  form="openmm.unit")
    assert puw.compatibility(q1, q2)