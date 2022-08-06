from ..webs import github_issues_web
from ..functions import caller_name

class NoStandardsError(Exception):
    """Exception raised when a quantity needs to be standardized but there are no standards
    declared.

    This exception is raised when a quantity needs to be standardized but the conversion can not be
    executed. There is at least a unit involved without standard declared.

    Raises
    ------
    NoStandardError
        A message is printed out with the name of the class or the method raising the exception,
        the possible wrong argument, the link to the API documentation, and the link to the
        issues board of PyUnitWizard's GitHub repository.

    Examples
    --------
    >>> import pyunitwizard as puw
    >>> puw.configure.set_standard_units(['nm', 'ps', 'kJ'])
    >>> standard = get_standard_units('10 litres')
    >>> if standard is None:
    ...    raise NoStandardError()

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> BadCallError <developer:exceptions:NoStandardError>`

    """

    def __init__(self, dimensionality=None, caller=None, message=None):


        if not caller:
            caller = caller_name()

        full_message = (f"The input quantity method has no standard. "
                   f"A complete set of standard units need to be defined. "
                   )

        if message:
            full_message += message

        api_doc = ''

        full_message += (
            f"Check {api_doc} for more information. "
            f"If you still need help, open a new issue in {github_issues_web}."
        )

        super().__init__(message)

