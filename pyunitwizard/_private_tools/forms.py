forms = ['simtk.unit', 'pint', 'unyt', 'string']

def digest_form(form):

    from pyunitwizard import kernel

    output = None

    if form is None:
        output=kernel.default_form
    elif form is 'string':
        output = form
    elif form.lower() in forms:
        output = form.lower()
    else:
        raise ValueError

    return output

def digest_to_form(to_form):

    output = None

    if to_form is not None:
        output = digest_form(to_form)

    return output

