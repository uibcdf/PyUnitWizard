class NotImplementedMethodError(NotImplementedError):
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
    >>> from pyuniwizard._private_tools.exceptions import NotImplementedMethodError
    >>> def method_name(a, b=True):
    ...    raise NotImplementedMethodError
    ...    pass

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> NotImplementedMethodError <developer:exceptions:NotImplementedMethodError>`

    """

    def __init__(self):

        from pyuniwizard import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        api_doc = ''

        message = (
                f"The \"{caller_name}\" method has not been implemented yet in the way you are using it. "
                f"Check {api_doc} for more information. "
                f"If you still want to suggest its implementation, open a new issue in {__github_issues_web__}"
                )

        super().__init__(message)


class NotImplementedClassError(NotImplementedError):
    """Exception raised when a class has not been fully implemented yet.

    This exception is raised when a class has being already defined but its code was not fully
    implemented yet. Maybe the class was just included in a developing version to be coded in the
    future. Or maybe the class can be instantated already for certain values of the input
    arguments, but not for others yet.

    Note
    ----
    This exception does not require input arguments.

    Raises
    ------
    NotImplementedClassError
        A message is printed out with the name of the class raising the exception, the link to
        the API documentation, and the link to the issues board of PyUnitWizard's GitHub repository.

    Examples
    --------
    >>> from pyuniwizard._private_tools.exceptions import NotImplementedClassError
    >>> class ClassName():
    ...    def __init__(self):
    ...       raise NotImplementedClassError
    ...       pass

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> NotImplementedClassError <developer:exceptions:NotImplementedClassError>`

    """

    def __init__(self):

        from pyuniwizard import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        api_doc = ''

        message = (
                f"The \"{caller_name}\" class has not been implemented yet in the way you are using it. "
                f"Check {api_doc} for more information. "
                f"If you still want to suggest its implementation, open a new issue in {__github_issues_web__}."
                )

        super().__init__(message)

class BadCallError(ValueError):
    """Exception raised when a method, or a class, was not properly called or instantiated.

    This exception is raised when a method or a class was not properly called or instantiated.

    Parameters
    ----------
    argument : str, optional
        The name of the possible wrong input argument.

    Raises
    ------
    BadCallError
        A message is printed out with the name of the class or the method raising the exception,
        the possible wrong argument, the link to the API documentation, and the link to the
        issues board of PyUnitWizard's GitHub repository.

    Examples
    --------
    >>> from pyuniwizard._private_tools.exceptions import BadCallError
    >>> def method_name(item, a=True):
    ...    if type(a) not in [int, float]:
    ...       raise BadCallError('a')
    ...    pass

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> BadCallError <developer:exceptions:BadCallError>`

    """

    def __init__(self, argument=None):

        from pyuniwizard import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        api_doc = ''

        message = f"The \"{caller_name}\" method or class was not properly invoked"
        if argument is not None:
            message += f", probably due to the \"{argument}\" input argument"
        message += (
                f". Check {api_doc} for more information. "
                f"If you still need help, open a new issue in {__github_issues_web__}."
                )

        super().__init__(message)

class NoStandardError(ValueError):
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

    def __init__(self):

        from pyuniwizard import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        api_doc = ''

        message = (f"The input quantity method has no standard. "
                   f"A complete set of standard units need to be defined. "
                   f"Check {api_doc} for more information. "
                   f"If you still need help, open a new issue in {__github_issues_web__}."
                   )
        super().__init__(message)


class UnknownFormError(ValueError):
    """Exception raised when the input quantity or unit has an unknown form and thereby not supported.

    This exception is raised when PyUnitWizard does not recognize a quantity or unit as a supported form.

    Note
    ----
    This exception does not require input arguments.

    Raises
    ------
    UnknownFormError
        A message is printed out with the name of the class or the method raising the exception,
        the link to the API documentation with the list of supported forms, and the link to the
        issues board of PyUnitWizard's GitHub repository.

    Examples
    --------
    >>> from pyunitwizard._private_tools.exceptions import UnknownFormError
    >>> from pyunitwizard import get_form
    >>> try:
    ...    _ = get_form(item)
    ... except:
    ...    raise UnknownFormError

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> UnknownFormError <developer:exceptions:UnknownFormError>`

    """

    def __init__(self):

        from sabueso import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        api_doc = ''

        message = (
                f"The input quantity in \"{method_name}\" has an unknown form. "
                f"Check {api_doc} for more information. "
                f"If you still need help, open a new issue in {__github_issues_web__}."
                )

        super().__init__(message)


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
    >>> from pyunitwizard._private_tools.exceptions import LibraryNotFoundError
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



