import os
from typing import List, Optional
import subprocess


class ErrorComandConsole(BaseException):
    ...


class ConsoleResult(object):
    def __init__(
        self,
        success: bool,
        result: Optional[str] = None,
        error: Optional[str] = None,
    ):
        self.success = success
        self.result = result
        self.error = error


def console_execute(console_args: List, result_return=False) -> ConsoleResult:
    console_obj = subprocess.Popen(console_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    consose_result, consose_error = console_obj.communicate()
    console_obj.wait()
    if console_obj.returncode != 0:
        raise ErrorComandConsole
    console_data = ConsoleResult(success=True)
    if result_return:
        console_data.result = consose_result
    return console_data


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
