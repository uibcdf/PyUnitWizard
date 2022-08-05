
class LibraryNotFoundError(NotImplementedError):
    """Exception raised when a library required by the user is not found.

    Some libraries are not considered as dependencies by PyUnitWizard. These libraries are required if
    the user choose to work with a specific quantities' package. In this case, the user hat to
    install it previousy. It that's not the case, the method will raise this exceptions suggesting
    the manual installation.

    Parameters
    ----------
    argument : str
        The name of the not found library.

    Raises
    ------
    LibraryNotFoundError
        A message is printed out with the name of the class or the method raising the exception,
        the name of the not found library, the link to the API documentation, and the link to the
        issues board of PytUnitWizard's GitHub repository.

    Examples
    --------
    >>> from pyunitwizard._private.exceptions import LibraryNotFoundError
    >>> def method_name(item, argument='pint'):
    ...    if argument == 'pint':
    ...       try:
    ...          import pint
    ...       except:
    ...          raise LibraryNotFoundError('pint')
    ...    pass

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> LibraryNotFoundError <developer:exceptions:LibraryNotFoundError>`

    """

    def __init__(self, library):

        from pyunitwizard import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        api_doc = ''

        message = (
                f"The python library {library} was not found. "
                f"Although {library} is not considered a dependency, it needs "
                f"to be installed to execute the {caller_name} method the way you require. "
                f"If you still need help, open a new issue in {__github_issues_web__}."
                )

        super().__init__(message)

class LibraryWithoutParserError(NotImplementedError):
    """Exception raised when a library can not parse strings.

    Some libraries cannot convert strings to quantities. This error will be raised by the API methods
    `string_to_quantity` and `string_to_unit` of those libraries without strings' parser.

    Parameters
    ----------
    argument : str
        The name of the library without parser.

    Raises
    ------
    LibraryWithoutParserError
        A message is printed out with the name of the library wihtout parser, the link to the
        section in the documentation regarding parser regarding parsers, and the link to the
        issues board of PytUnitWizard's GitHub repository.

    Examples
    --------
    >>> import pyunitwizard as puw
    >>> from pyunitwizard._private.exceptions import LibraryWithoutParserError
    >>> from pyunitwizard._private.exceptions import LibraryWithoutParserError
    >>> def method_name(item, argument='pint'):
    ...    if argument == 'pint':
    ...       try:
    ...          import pint
    ...       except:
    ...          raise LibraryNotFoundError('pint')
    ...    pass

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> LibraryWithoutStringsParserError <developer:exceptions:LibraryWithoutStringsParserError>`

    """

    def __init__(self, library):

        from pyunitwizard import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        api_doc = ''

        message = (
                f"The python library {library} was not found. "
                f"Although {library} is not considered a dependency, it needs "
                f"to be installed to execute the {caller_name} method the way you require. "
                f"If you still need help, open a new issue in {__github_issues_web__}."
                )

        super().__init__(message)


