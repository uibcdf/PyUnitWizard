class BadCallError(ValueError):
    def __init__(self):
        message = 'Wrong way of invoking this method. Check the online documentation for more information: http://uibcdf/PyUnitWizard'
        super().__init__(message)

class PintNotFoundError(ImportError):
    def __init__(self):
        message = 'This method needs the library Pint to work.'
        super().__init__(message)

class NotImplementedError(NotImplementedError):
    def __init__(self):
        message = 'It has not been implemeted yet.\n Write a new issue in https://github.com/uibcdf/PyUnitWizard/issues asking for it.'
        super().__init__(message)


