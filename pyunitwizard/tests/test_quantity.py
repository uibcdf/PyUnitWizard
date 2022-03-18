import pyunitwizard as puw

def test_quantity_openmm_unit():
    puw.configure.reset()
    puw.configure.load_library(['openmm.unit'])

    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    quantity = puw.quantity(10, openmm_unit.kilojoule/openmm_unit.mole)
    q_true = 10 * openmm_unit.kilojoule/openmm_unit.mole
    assert puw.similarity(quantity, q_true)

def test_quantity_pint():
    puw.configure.reset()
    puw.configure.load_library(['pint'])

    ureg = puw.forms.api_pint.ureg
    assert puw.quantity(2.5, 'nanometers/picoseconds') == ureg.Quantity(2.5, 'nanometers/picoseconds')
