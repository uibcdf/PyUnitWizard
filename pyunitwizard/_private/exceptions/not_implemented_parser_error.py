from ..webs import github_issues_web
from ..functions import caller_name

class NotImplementedParserError(Exception):
    """Exception raised when parsing a string with the parser and to the parser choosen has not been
    implemented yet.

    This exception is raised when parsing a strint with the parser and to the parser choosen by the
    user, has not been implemented yet.

    Parameters
    ----------
    parser : str
        The name of the parser choosen by the user.
    to_parser : str
        The name of target parser choosen by the user.

    Raises
    ------
    NotImplementedMethodError
        A message is printed out with the link to the documentation section about parsing strings,
        and the link to the issues board of PyUnitWizard's GitHub repository.

    Examples
    --------
    >>> from pyunitwizard._private.exceptions import NotImplementedParsingError
    >>> def method_name(string, parser='pint', to_parser='new_parser'):
    ...    if parser=='pint' and to_parser='new_parser':
    ...       raise NotImplementedParsingError('pint', 'new_parser')
    ...    pass

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> NotImplementedParsingError <developer:exceptions:NotImplementedParsingError>`

    """

    def __init__(self, parser=None, caller=None, message=None):

        if not caller:
            caller = caller_name()

        full_message = (
                f"The \"{parser}\" has not been implemented yet. "
                )

        if message:
            full_message += message

        api_doc = ''

        full_message += (
            f"Check {api_doc} for more inparseration. "
            f"If you still need help, open a new issue in {github_issues_web}."
        )

        super().__init__(message)

