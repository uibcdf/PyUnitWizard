import pyunitwizard as puw
import unyt

def test_quantity_openmm_unit():

    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    quantity = puw.quantity('10 kilojoule/mole', form='openmm.unit')
    quantity = puw.change_value(quantity, 20)
    quantity_true = 20 * openmm_unit.kilojoule/openmm_unit.mole
    assert puw.similarity(quantity, quantity_true)

def test_quantity_pint():

    ureg = puw.forms.api_pint.ureg
    quantity = puw.quantity(10, 'nanometers/picoseconds')
    quantity = puw.change_value(quantity, 20)
    quantity_true = ureg.Quantity(20, 'nanometers/picoseconds')
    assert puw.similarity(quantity, quantity_true)


def test_quantity_unyt():

    quantity = puw.quantity(10, unyt.J/unyt.s, form="unyt")
    quantity = puw.change_value(quantity, 20)
    quantity_true = 20 * unyt.J/unyt.s
    assert puw.similarity(quantity, quantity_true)
