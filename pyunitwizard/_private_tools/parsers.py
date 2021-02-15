parsers = ['simtk.unit', 'pint', 'unyt']

def digest_parser(parser):

    output = None

    if parser is not None:
        if parser.lower() in parsers:
            output = parser.lower()
        else:
            raise ValueError

    return output

