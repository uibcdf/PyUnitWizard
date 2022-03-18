from ._private_tools.exceptions import *
from ._private_tools.forms import digest_to_form
from ._private_tools.parsers import digest_parser
from .forms import dict_string_to_quantity
from .forms import dict_to_string
from .forms import dict_translate
import ast
from typing import Optional

def _parse_with_pint(string: str):
    """ Parses a string and returns a pint quantity.

        Parameters
        ----------
        string : str
            A string quantity.
        
        Returns
        -------
        pint.quantity
            A pint quantity.
    """
    # Check if it's a non scalar quantity
    if string.startswith('[') or string.startswith('('):

        end_list = max(string.rfind(')')+1, string.rfind(']')+1)
        value_string = string[:end_list]
        unit_string = string[end_list:]

        return ast.literal_eval(value_string)*dict_string_to_quantity['pint'](unit_string)
    else:
       return dict_string_to_quantity['pint'](string)

def parse(string: str, parser: Optional[str]=None, to_form: Optional[str]=None):
    """ Parses a string and returns a quantity.

        Parameters
        ----------
        string : str
            A string quantity.
        
        parser : str
            The parser that will be used.

        to_form; str, optional
            The form of the quantity. Can be pint, openmm.unit or
            string.

        Returns
        -------
        QuantityLike
            A quantity.
    """
    if not isinstance(string, str):
        raise BadCallError('string')

    parser = digest_parser(parser)
    to_form = digest_to_form(to_form)

    if parser == 'pint':

        if to_form == 'pint':

            return _parse_with_pint(string)

        elif to_form == 'openmm.unit':

            pint_quantity = _parse_with_pint(string)
            return dict_translate['pint']['openmm.unit'](pint_quantity)

        elif to_form == 'string':

            pint_quantity = _parse_with_pint(string)
            return dict_to_string['pint'](pint_quantity)

        else:

            raise NotImplementedParsingError(parser, to_form)

    elif parser == 'openmm.unit':

        raise LibraryWithoutParserError('openmm.unit')

    else:

        raise NotImplementedParsingError(parser, to_form)