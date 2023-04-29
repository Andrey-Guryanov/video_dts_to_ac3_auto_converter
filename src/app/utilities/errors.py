class NoFolder(BaseException):
    message = "Folder not found :("


class IncorrectAnswer(BaseException):
    message = "Incorrect answer :( Possible values - 'y'(yes) or 'n'(no)"
