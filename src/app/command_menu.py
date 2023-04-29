from pathlib import Path
from retrying import retry
from prettytable import PrettyTable
from typing import Callable, Optional, List, NoReturn

from src.settings import CONFIG
from src.model import DB_MANAGER
from src.app.ffmpeg_control import check_ffmpeg_sys
from src.app.utilities.command import clear_screen
from src.app.utilities.yml_handler import save_yaml
from src.app.utilities.errors import NoFolder, IncorrectAnswer
from src.app.utilities.validators import path_validator, answer_validator


class MenuVariable:
    value: Optional[str] = None
    result: Optional[str] = None

    def __init__(
        self,
        text_name: str,
        msg: str,
        validator: Callable,
        config_key: Optional[str] = None,
    ):
        self.text_name = text_name
        self.msg = msg
        self.validator = validator
        self.config_key = config_key

    @retry(stop_max_attempt_number=3)
    def in_console(self) -> Optional[NoReturn]:
        try:
            self.value = input(self.msg)
            self._validator()
        except (NoFolder, IncorrectAnswer) as error:
            print(error.message)
            raise error
        except Exception as error:
            print(f"An error has occurred = {error}")

    def _validator(self):
        self.result = self.validator(self.value)


class MenuVariableAnswer(MenuVariable):
    result: Optional[bool] = None

    def __init__(
        self,
        text_name: str,
        msg: str,
        validator: Callable,
        config_key: Optional[str] = None,
    ):
        super().__init__(text_name, msg, validator, config_key)


def _save_config(in_lines: List[MenuVariable]):
    print("Cache data will be deleted (if any)")
    in_save = MenuVariableAnswer(
        text_name="save config",
        msg="Save configuration? (y/n):",
        validator=answer_validator,
    )
    in_save.in_console()
    if in_save.result:
        path_yaml = Path.cwd() / "config.yaml"
        config_param = {}
        for line in in_lines:
            if line.config_key:
                config_param[line.config_key] = line.result
        if save_yaml(config_param, path_yaml):
            print("Configuration saved")
            DB_MANAGER.init()
            print("Failed to save configuration")


def init_config():
    result_table = PrettyTable()
    result_table.field_names = ["Configuration variables", "Set values"]
    in_scann_path = MenuVariable(
        text_name="scann path",
        msg="Specify the folder to search for video files (full path): ",
        validator=path_validator,
        config_key="scann_path",
    )
    in_save_path = MenuVariable(
        text_name="save path",
        msg="Specify the folder to save video files (full path): ",
        validator=path_validator,
        config_key="save_path",
    )
    in_save_structure = MenuVariableAnswer(
        text_name="save structure",
        msg="Save folder structure? (y/n): ",
        validator=answer_validator,
        config_key="save_structure",
    )
    in_copy_all = MenuVariableAnswer(
        text_name="copy all",
        msg="Copy all video files? (y/n): ",
        validator=answer_validator,
        config_key="copy_all",
    )
    in_lines = [in_scann_path, in_save_path, in_save_structure, in_copy_all]

    for line in in_lines:
        line.in_console()
        result_table.add_row([line.text_name, line.result])
    clear_screen()
    print(result_table)
    _save_config(in_lines)


def init_start_job():
    init_check = True
    if CONFIG:
        print("Configuration loaded - ok")
    else:
        print("Set configuration parameters (command - 'init')")
        init_check = False
    if check_ffmpeg_sys():
        print("FFmpeg installed in the system - ok")
    else:
        print("You need to install the FFmpeg")
        init_check = False

    if init_check:
        return True
    return False
