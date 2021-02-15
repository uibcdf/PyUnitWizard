from . import default

forms = ['simtk.unit', 'pint', 'unyt']

def digest_form(form):

    output = None

    if form is None:
        output=default.form
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

