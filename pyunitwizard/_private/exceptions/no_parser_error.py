from ..webs import github_issues_web
from ..functions import caller_name

class NoParserError(Exception):

    def __init__(self, caller=None, message=None):

        if not caller:
            caller = caller_name()

        full_message = (f"There is no parser loaded."
                   )

        if message:
            full_message += message

        api_doc = ''

        full_message += (
            f"Check {api_doc} for more information. "
            f"If you still need help, open a new issue in {github_issues_web}."
        )

        super().__init__(message)

