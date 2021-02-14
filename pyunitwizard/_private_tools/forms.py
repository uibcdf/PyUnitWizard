forms = {
    'simtk.unit': 'simtk.unit',
    'pint': 'pint',
    'unyt': 'unyt'
}

def digest_form(form):

    output = None

    if form.lower() in forms:
        output = forms[form.lower()]
    else:
        raise ValueError

    return output

def digest_to_form(to_form):

    output = None

    if to_form is not None:
        output = digest_form(to_form)

    return output

