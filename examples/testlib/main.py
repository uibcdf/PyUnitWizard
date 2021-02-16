from ._pyunitwizard import puw

def sum_quantities(a, b, form=None):

    aa = puw.string_to_quantity(a, to_form=form)
    bb = puw.string_to_quantity(b, to_form=form)
    output = aa+bb

    return output

def get_form(quantity):

    return puw.get_form(quantity)

def libraries_loaded():

    return puw.libraries_loaded()

