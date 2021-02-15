from ._pyunitwizard import puw

def sum_quantities(a='3m', b='7m' , form=None):

    aa = puw.string_to_quantity(a, to_form=form)
    bb = puw.string_to_quantity(b, to_form=form)
    output = aa+bb

    return output

def get_form(quantity):

    return puw.get_form(quantity)

