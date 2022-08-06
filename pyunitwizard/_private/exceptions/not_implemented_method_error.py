from ..webs import github_issues_web
from ..functions import caller_name

class NotImplementedMethodError(Exception):
    """Exception raised when a method has not been fully implemented yet.

    This exception is raised when a method has been already defined but its code was not fully
    implemented yet. Maybe the method was just included in a developing version to be coded in the
    future. Or maybe the method works already for certain values of the input arguments, but not
    for others yet.

    Note
    ----
    This exception does not require input arguments.

    Raises
    ------
    NotImplementedMethodError
        A message is printed out with the name of the method raising the exception, the link to
        the API documentation, and the link to the issues board of PyUnitWizard's GitHub repository.

    Examples
    --------
    >>> from pyunitwizard._private.exceptions import NotImplementedMethodError
    >>> def method_name(a, b=True):
    ...    raise NotImplementedMethodError
    ...    pass

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> NotImplementedMethodError <developer:exceptions:NotImplementedMethodError>`

    """

    def __init__(self, method=None, caller=None, message=None):

        if not caller:
            caller = caller_name()

        full_message = f"The \"{caller_name}\" method has not been implemented yet in the way you are using it. "

        if message:
            full_message += message

        api_doc = ''

        full_message += (
            f"Check {api_doc} for more information. "
            f"If you still need help, open a new issue in {github_issues_web}."
        )

        super().__init__(message)

