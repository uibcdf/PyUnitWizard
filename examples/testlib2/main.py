from testlib2 import _puw

def sum_quantities(a='3m', b='7m' , form=None):

    aa = _puw.string_to_quantity(a, to_form=form)
    bb = _puw.string_to_quantity(b, to_form=form)
    output = aa+bb

    return output

def get_form(quantity):

    return _puw.get_form(quantity)

def libraries_loaded():

    return _puw.libraries_loaded()

