import os
from pathlib import Path


def crete_dir_structure(path_scann: Path, path_file: Path, path_save: Path):
    len_scann = len(path_scann.parents)
    repeat = len(path_file.parents) - len_scann - 1
    check_path = path_save
    if repeat > 0:
        count_dir = repeat
        for _ in range(repeat):
            count_dir -= 1
            dir_name = path_file.parents[count_dir].stem
            check_path = check_path / dir_name
            if not os.path.isdir(check_path):
                os.makedirs(check_path)
    return check_path
