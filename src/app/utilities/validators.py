import os
from typing import Union, NoReturn

from src.app.utilities.errors import NoFolder, IncorrectAnswer


def path_validator(in_path: str) -> Union[str, NoReturn]:
    check_folder = os.path.isdir(in_path)
    if check_folder:
        return in_path
    raise NoFolder


def answer_validator(in_answer: str) -> Union[bool, NoReturn]:
    if 3 >= len(in_answer) > 0:
        if in_answer.lower()[0] == "y":
            return True
        elif in_answer.lower()[0] == "n":
            return False
    raise IncorrectAnswer
