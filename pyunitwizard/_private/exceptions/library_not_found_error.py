from ..webs import github_issues_web
from ..functions import caller_name

class LibraryNotFoundError(Exception):
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

    def __init__(self, library=None, caller=None, message=None):

        if not caller:
            caller = caller_name()

        full_message = (
                f"The python library {library} was not found. "
                f"Although {library} is not considered a dependency, it needs "
                f"to be installed to execute the {caller_name} method the way you require. "
                )

        if message:
            full_message += message

        api_doc = ''


        full_message += (
            f"Check {api_doc} for more information. "
            f"If you still need help, open a new issue in {github_issues_web}."
        )

        super().__init__(message)

