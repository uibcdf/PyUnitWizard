from ._private_tools.exceptions import *
from ._private_tools.forms import digest_to_form
from ._private_tools.parsers import digest_parser
from .forms import dict_string_to_quantity
from .forms import dict_to_string
from .forms import dict_translate

def _parse_with_pint(string):

    if string.startswith('[') or string.startswith('('):

        import ast

        end_list = max(string.rfind(')')+1, string.rfind(']')+1)
        value_string = string[:end_list]
        unit_string = string[end_list:]

        output=ast.literal_eval(value_string)*dict_string_to_quantity['pint'](unit_string)

    else:

        output=dict_string_to_quantity['pint'](string)

    return output

def parse(string, parser=None, to_form=None):

    if type(string) is not str:
        raise BadCallError('string')

    parser = digest_parser(parser)
    to_form = digest_to_form(to_form)

    output = None

    if parser == 'pint':

        if to_form == 'pint':

            output = _parse_with_pint(string)

        elif to_form == 'openmm.unit':

            pint_quantity = _parse_with_pint(string)
            output = dict_translate['pint']['openmm.unit'](pint_quantity)

        elif to_form == 'string':

            pint_quantity = _parse_with_pint(string)
            output = dict_to_string['pint'](pint_quantity)

        else:

            raise NotImplementedParsingError(parser, to_form)

    elif parser is 'openmm.unit':

        raise LibraryWithoutStringParserError('openmm.unit')

    else:

        raise NotImplementedParsingError(parser, to_form)

    return output

