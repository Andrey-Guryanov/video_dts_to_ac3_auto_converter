import yaml
from typing import Dict
from pathlib import Path


def save_yaml(param: dict, path_yaml: Path) -> bool:
    try:
        with open(path_yaml, "w+") as file:
            yaml.dump(param, file)
        return True
    except Exception as error:
        print(f"An error has occurred - {error}")
        return False


def read_yaml(path_yaml: Path) -> Dict:
    try:
        with open(path_yaml) as file:
            read_yaml = yaml.load(file, Loader=yaml.FullLoader)
            return read_yaml
    except Exception as error:
        print(f"An error has occurred - {error}")
        return False
